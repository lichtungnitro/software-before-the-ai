# Catalog coverage

Reviewed November 21, 2026. Counts use different units. A product can have several editions and can appear in a historical snapshot as well as in the reviewed catalog.

| Dataset | Contents | Unit |
| --- | ---: | --- |
| [Reviewed decisions](../research/INDEX.md) | 30 | App, platform, edition and market. Covers 22 app identifiers. |
| [iOS App Store](../data/snapshots/README.md) | 7,197 | Distinct App Store IDs with a recorded version. |
| [Android Google Play](../data/snapshots/README.md) | 8,581 | Distinct historical listing titles with a concrete version. This survey omits package IDs. |
| [Android F-Droid](../data/snapshots/fdroid.csv) | 57 | Package IDs with a matching enabled build recipe. |
| [Windows Scoop](../data/snapshots/windows.csv) | 457 | Selected desktop packages with a numbered manifest version. |

The snapshots contain **16,292 historical version observations**. Product names, paid editions, store listings and package identities can differ across sources. The project reports each source's unit separately.

## Decision records

[data/apps.json](../data/apps.json) contains reviewed decisions and some original research targets. [data/expanded-candidates.json](../data/expanded-candidates.json) contains the rest of the research queue. Together these files contain 1,133 scoped records across 384 catalog IDs. Of those records, 12 have verified cutoffs, 5 have probable cutoffs, 13 have ambiguous cutoffs and 1,103 await research. The original queue includes three proposed platforms for many apps. A row marked `platform_availability: not_checked` still needs independent platform evidence.

The two search paths serve different questions. Start with the [reviewed index](../research/INDEX.md) for a cutoff. Use [historical versions](../data/snapshots/README.md) to establish that a particular release was recorded and to trace the next release that needs investigation. The lookup command searches both.

## Evidence needed for a new cutoff

1. Match the product, platform, edition, market and distribution channel.
2. Identify a user-facing, first-party generative feature and find evidence of actual availability.
3. Check the preceding official build and look for separately shipped beta or maintenance branches.
4. Record the scope, sources and uncertainty. An account flag, embedded mini-program or hosted user interface may cross client-version boundaries.
5. Link a publisher archive when it contains the reported release. An app store listing identifies a product and may only offer its current release.
