#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "data" / "apps.json"
rows = json.loads(p.read_text(encoding="utf-8"))
seen = set()
for row in rows:
    key = (row["app_id"], row["platform"], row.get("edition", "consumer"), row.get("region", "global"))
    assert key not in seen, f"duplicate: {key}"
    seen.add(key)
    assert row["platform"] in ("ios", "android", "windows")
    assert row["status"] in ("unknown", "probable", "verified", "ambiguous")
    if row["status"] == "verified":
        assert row.get("last_pre_llm_version") and row.get("evidence_urls")
    if row.get("download_url"):
        assert row["download_url"].startswith("https://")
print(f"Validated {len(rows)} platform records across {len(set(r['app_id'] for r in rows))} apps")
