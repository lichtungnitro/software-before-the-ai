# Coverage and limitations

The repository currently has two datasets:
- `data/apps.json`: initial 21 applications / 63 candidate platform rows
- `data/expanded-candidates.json`: 352 additional applications / 1056 candidate platform rows

Total: **373 named applications / 1119 candidate platform rows**.

Candidate rows deliberately include all three target platforms, even where a native app may not exist. `platform_availability: not_checked` means **not verified**, not available. Exclude nonexistent platform editions during research.

A catalog entry is **not a verified pre-LLM version** until it has primary or strong historical release evidence. The dataset currently has **no verified version claims**. Do not advertise 1119 downloadable builds.

## Research workflow
1. Verify the app identity and whether it has a native iOS, Android or Windows edition.
2. Find first actual user-facing LLM feature and deployment, not just marketing announcement.
3. Verify the immediately preceding build for that edition/region, including server-side rollout caveats.
4. Link official historical releases where possible; otherwise leave download URL empty.
5. Record primary sources and confidence. Avoid unofficial binaries with uncertain provenance.
6. Recheck licensing, signatures, and compatibility; older builds can be insecure.

Some apps are AI-native and may have **no pre-LLM version**; label this explicitly rather than inventing one.
