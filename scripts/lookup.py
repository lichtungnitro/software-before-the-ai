#!/usr/bin/env python3
"""Look up cutoff decisions and historical versions by app name or identifier."""

import argparse
import csv
import json
import unicodedata
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
SNAPSHOTS = DATA / "snapshots"


def records():
    for filename in ("apps.json", "expanded-candidates.json"):
        yield from json.loads((DATA / filename).read_text(encoding="utf-8"))


def snapshot_tables():
    sources = json.loads((SNAPSHOTS / "sources.json").read_text(encoding="utf-8"))
    for path in sorted(SNAPSHOTS.glob("*.csv")):
        source_name = path.stem.split("-")[0]
        yield path, source_name, sources[source_name]


def normalize(value):
    return unicodedata.normalize("NFKC", value).casefold().strip()


def describe(row):
    version = row["last_pre_llm_version"] or "unresolved"
    result = [f"{row['name']} | {row['platform']} | {row['edition']} | {row['region']}",
              f"  Last qualifying version: {version} [{row['status']}]"]
    if row.get("first_llm_feature"):
        feature_version = row.get("first_llm_feature_version") or "build unknown"
        result.append(f"  First documented integration: {row['first_llm_feature']} ({feature_version})")
    for entry in row.get("observed_versions", []):
        result.append(f"  Observed by {entry['observed_by']}: {entry['version']} — {entry['detail']}")
    for entry in row.get("documented_rollouts", []):
        result.append(f"  Documented by {entry['documented_by']}: {entry['feature']}")
    if row.get("notes"):
        result.append("  " + row["notes"])
    if row.get("download_url"):
        result.append("  Official archive: " + row["download_url"])
    result.extend("  Evidence: " + url for url in row["evidence_urls"])
    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="App name, substring, catalog ID, or store ID")
    parser.add_argument("--platform", choices=("ios", "android", "windows"))
    args = parser.parse_args()
    term = normalize(args.query)
    if not term:
        parser.error("Enter an app name or identifier")

    reviews, targets, observations = [], [], []
    matched_store_ids = set()
    for row in records():
        if args.platform and row["platform"] != args.platform:
            continue
        names = [row["name"], row["app_id"], row.get("store_id", ""), *row.get("aliases", [])]
        if any(term in normalize(name) for name in names):
            if row.get("store_id"):
                matched_store_ids.add((row["platform"], row["store_id"]))
            if row.get("reviewed_at"):
                reviews.append(describe(row))
            else:
                targets.append(f"{row['name']} | {row['platform']} | unchecked research target")

    for path, _, source in snapshot_tables():
        platform = source["platform"]
        if args.platform and platform != args.platform:
            continue
        with path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                identity = row[source["identity_field"]]
                if not (term in normalize(row["name"]) or term in normalize(identity)
                        or (platform, identity) in matched_store_ids):
                    continue
                url = source["evidence_url"].format(source_ref=row["source_ref"])
                observations.append(f"{row['name']} | {platform} | observed {row['observed_version']}"
                                    f" | {source['label']}\n  Evidence: {url}")

    for heading, lines in [("Reviewed cutoffs", reviews), ("Historical observations", observations),
                           ("Unreviewed targets", targets)]:
        if lines:
            print(heading)
            print("\n".join(lines))
            print()
    if not (reviews or observations or targets):
        print(f"No catalog match for {args.query!r}.")


if __name__ == "__main__":
    main()
