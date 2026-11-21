# Research methodology

## Definition
Qualifying versions have no built-in user-facing LLM or generative-AI functionality. Traditional NLP, search ranking, recommendations, OCR, speech recognition, and classic ML remain in scope.

Disqualifying functionality includes integrated LLM chat assistants, Copilot-style experiences, generative writing, LLM summaries, and generative image features.

## Verification
Research each app/platform/edition/region independently. Identify the first dated LLM feature announcement and its actual rollout, then determine the last release demonstrably preceding it. Distinguish client updates from server-side flags and optional integrations.

Use statuses:
- verified: primary documentation supports both cutoff and preceding version
- probable: credible evidence but incomplete release chronology
- ambiguous: server-side rollout or edition/region variations prevent a unique answer
- unknown: no reliable conclusion

Never infer a version number from an announcement date. Record evidence URLs, review date, and any uncertainty.

## Download links
Prefer official vendor archives and signed release assets. If a reliable historical download cannot be found, leave it blank. Do not host proprietary binaries or bypass licensing/signatures. Warn users that old versions may be insecure or unsupported.

## Reading the expanded catalog

The historical CSV files store `observed_version` separately from the reviewed JSON field `last_pre_llm_version`. A dated sighting establishes that a version existed by that date. A release date requires its own evidence. The snapshots have separate [provenance and selection notes](../data/snapshots/README.md).

A stable channel, an early-access channel and a community fork can have different cutoffs. Built-in features that require opt-in or a user-supplied API key count as integrations. Independently installed third-party plugins are outside the stock edition. A first-party generative experience reached through the host app's own navigation counts even when a server delivers it. Its delivery mechanism belongs in the record.

For a discontinued app, `boundary_kind: final_release` records the publisher's final qualifying version in the specified edition. The first-AI fields remain empty. A retirement date and a release date can differ by years.

The optional `observed_versions` and `documented_rollouts` arrays record dated build sightings and feature reports individually. `observed_by` and `documented_by` express the latest date by which the cited evidence shows an observation. A source covering a product family may leave OS-specific eligibility unresolved. `download_url` points to a publisher's release or archive page when a relevant historical installer is listed.
