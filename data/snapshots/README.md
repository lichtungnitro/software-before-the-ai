# Browse historical versions

These tables record versions reported in 2017–2019. Each row identifies a software release to investigate. For the last release before a built-in generative feature, check the [reviewed index](../../research/INDEX.md). The same app may appear in multiple tables.

| Source | Records | Browse by the first character of the recorded title |
| --- | ---: | --- |
| iOS App Store · 2017 | 7,197 | [A–F](ios-a-f.csv) · [G–P](ios-g-p.csv) · [Q–Z](ios-q-z.csv) · [Numbers, symbols and other scripts](ios-other.csv) |
| Android Google Play · 2018 | 8,581 | [A–F](android-a-f.csv) · [G–P](android-g-p.csv) · [Q–Z](android-q-z.csv) · [Numbers, symbols and other scripts](android-other.csv) |
| Android F-Droid · December 31, 2019 | 57 | [Browse packages and version codes](fdroid.csv) |
| Windows Scoop Extras · December 31, 2019 | 457 | [Browse desktop apps](windows.csv) |

On GitHub, open a CSV and use the page's search or your browser's Find command. Mobile survey tables are ordered by historical rating count or install tier within each file. Search all tables locally with `python3 scripts/lookup.py "app name"` from the repository root. The output expands the source reference into a link to the original row or manifest.

## How to read a row

- **Name and edition.** Mobile survey titles retain their period spelling. An Apple numeric store ID identifies a listing across renames. The Google Play survey records display titles and has no package-ID column. A title match across stores needs independent confirmation.
- **Observed version.** The version is a string. Preserve leading zeroes, vendor suffixes and build labels. Android’s `listing_updated` is the update date from the archived listing. A package snapshot date is the date of the catalog revision.
- **Source reference.** For the mobile surveys, `source_ref` gives the one-based physical line in the pinned CSV, including the header. For F-Droid and Scoop it gives the path inside a pinned Git revision. [Source URL templates](sources.json)
- **Distribution.** The tables contain version metadata. Publisher-provided historical download pages, when substantiated, appear in the reviewed JSON records.

## Provenance

**iOS.** Ramanathan Perumal's *Mobile App Store (7200 apps)* collected iTunes storefront metadata in 2017. These tables retain the title, numeric ID, version, genre and total rating count, then add the source line and reorder the rows. They include all 7,197 distinct IDs in the referenced CSV, including games and delisted products. The iOS tables carry the source dataset's GPL 2 terms. [Original dataset](https://www.kaggle.com/datasets/ramamet4/app-store-apple-data-set-10k-apps) · [Pinned CSV](https://github.com/divaymohan/apple-apps/blob/659a2dea8c8f3633c83ed0c51df9110feb6fee03/AppleStore.csv) · [GPL 2](licenses/GPL-2.0.txt)

**Google Play.** L. Gupta, *Google Play Store Apps*, February 2019, compiled from 2018 storefront listings. The Android survey tables are distributed under CC BY-SA 4.0. The adaptation selects fields, converts dates to ISO format and install tiers to lower bounds, adds source lines and reorders rows. It keeps one observation per exact trimmed title with a version containing a digit, numeric review and install counts, and an Android requirement. Among qualifying observations it keeps the most recent listing update. One title had conflicting versions on the same latest date and was excluded. Matching versions on that date use the largest install tier, then the first source row. The source's device-dependent or missing versions and its shifted row do not enter the results. [Original dataset and attribution](https://www.kaggle.com/lava18/google-play-store-apps) · [Pinned CSV](https://github.com/kishan0725/Google-Play-Store/blob/55bb1e1a22e0b5fe738a431a6d5e1845dd1a1e49/googleplaystore.csv) · [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

**F-Droid.** The selected Android packages cover mail, calendars, navigation, media, reading, sync and utilities. Each record matches both the version name and version code of an enabled build recipe to its package's current metadata at the dated revision. A build recipe records packaging history. The upstream metadata repository supplies the GNU AGPL v3. [Pinned metadata tree](https://github.com/f-droid/fdroiddata/tree/7dd43b663f45e7691070027259a9cd95ba8d70f0/metadata) · [Field reference](https://f-droid.org/docs/Build_Metadata_Reference/) · [Upstream license](licenses/AGPL-3.0.txt)

**Windows.** The selected Scoop Extras desktop applications cover creative tools, offices, readers, science, development, communication, games and Windows utilities. Each version comes directly from its package manifest at the December 31 revision. Floating `nightly` labels were excluded. Display names and categories were curated for browsing. [Pinned manifests](https://github.com/ScoopInstaller/Extras/tree/812ff4cbf1fc09f51624a2ba3673bc0af9001894/bucket) · [Upstream license](licenses/Unlicense.txt)
