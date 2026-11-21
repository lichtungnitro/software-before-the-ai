#!/usr/bin/env python3
"""Check the decision records, research queue, and version snapshots."""

import csv
from collections import Counter
from datetime import date
from urllib.parse import urlsplit

from lookup import records, snapshot_tables


def require(condition, message):
    if not condition:
        raise ValueError(message)


def https(url):
    parts = urlsplit(url)
    return parts.scheme == "https" and bool(parts.netloc)


def check_decisions():
    seen = set()
    statuses = Counter()
    for row in records():
        key = (row["app_id"], row["platform"], row["edition"], row["region"])
        require(all(key) and key not in seen, f"Missing or duplicate identity: {key}")
        seen.add(key)
        require(row["platform"] in {"ios", "android", "windows"}, f"Invalid platform: {key}")
        status = row["status"]
        require(status in {"unknown", "probable", "verified", "ambiguous"}, f"Invalid status: {key}")
        statuses[status] += 1

        urls = row["evidence_urls"]
        require(all(https(url) for url in urls), f"Invalid evidence URL: {key}")
        if status != "unknown":
            require(urls and row["reviewed_at"], f"Missing evidence or review date: {key}")
        if status == "verified":
            require(row["last_pre_llm_version"], f"Missing verified version: {key}")
        for field in ("last_pre_llm_release_date", "first_llm_rollout_date", "reviewed_at"):
            if row.get(field):
                date.fromisoformat(row[field])
        if row.get("download_url"):
            require(https(row["download_url"]) and row["download_source_type"],
                    f"Invalid download citation: {key}")
        if row.get("boundary_kind") == "final_release":
            require(not row["first_llm_feature_version"], f"Retired version has an AI successor: {key}")
        for field, value, dated in (("observed_versions", "version", "observed_by"),
                                    ("documented_rollouts", "feature", "documented_by")):
            for item in row.get(field, []):
                require(item[value] and item["source_url"] in urls, f"Unattributed {field}: {key}")
                date.fromisoformat(item[dated])
    print(f"Validated {len(seen):,} scoped records. " +
          ", ".join(f"{n:,} {status}" for status, n in sorted(statuses.items())))


def check_snapshots():
    identities, locators = set(), set()
    counts = Counter()
    for path, source_name, source in snapshot_tables():
        with path.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                identity = (source_name, row[source["identity_field"]])
                ref = row["source_ref"]
                location = (source_name, ref)
                require(identity[1] and identity not in identities, f"Duplicate identity: {identity}")
                require(ref and location not in locators, f"Duplicate evidence locator: {location}")
                identities.add(identity)
                locators.add(location)
                label = f"{path.name}: {row['name']}"
                require(row["name"] and row["category"] and any(c.isdigit() for c in row["observed_version"]),
                        f"Missing name, category or version: {label}")
                require(https(source["evidence_url"].format(source_ref=ref)), f"Invalid evidence URL: {label}")
                if source_name in {"ios", "android"}:
                    require(ref.isdecimal() and int(ref) >= 2, f"Invalid source line: {label}")
                if source_name == "ios":
                    require(row["store_id"].isdecimal() and row["rating_count"].isdecimal(), label)
                elif source_name == "android":
                    require(row["installs_at_least"].isdecimal(), label)
                    date.fromisoformat(row["listing_updated"])
                elif source_name == "fdroid":
                    require(ref == f"metadata/{row['package_id']}.yml" and row["version_code"].isdecimal(), label)
                elif source_name == "windows":
                    require(ref.startswith("bucket/") and ref.endswith(".json"), label)
                counts[source_name] += 1
    require(counts.keys() == {"ios", "android", "windows", "fdroid"}, "Missing snapshot source")
    print(f"Validated {sum(counts.values()):,} historical observations. " +
          ", ".join(f"{n:,} {source}" for source, n in sorted(counts.items())))


if __name__ == "__main__":
    check_decisions()
    check_snapshots()
