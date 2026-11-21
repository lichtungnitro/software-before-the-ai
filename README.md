# Software Before the AI

Find the last release of an iOS, Android or Windows app before it gained a built-in LLM assistant, generative writing, summarization or image generation. Traditional recommendations, OCR and predictive typing still qualify.

**Start with an app.** [Taobao / 淘宝](research/taobao.md) traces two releases on either side of a shopping event and explains why a build number alone cannot settle the question. [Reviewed apps](research/INDEX.md) lists the decisions, including official archives where available. [Browse historical versions](data/snapshots/README.md) covers 16,292 version observations from the App Store, Google Play, F-Droid and Scoop.

| App and edition | Last qualifying release | What establishes the boundary |
| --- | --- | --- |
| calibre · Windows stable | [8.10.0](https://download.calibre-ebook.com/8.10.0/) | The tagged 8.11.0 changelog adds Ask AI to the viewer. |
| PowerToys · Windows stable | [0.80.1](https://github.com/microsoft/PowerToys/releases/tag/v0.80.1) | The next release introduced the optional OpenAI prompt in Advanced Paste. |
| GitHub Desktop · Windows stable | [3.4.21](https://github.com/desktop/desktop/releases/tag/release-3.4.21) | Copilot commit messages reached stable in 3.5.0. The beta channel had them earlier. |
| Firefox Lockwise · iOS / Android | [1.8.1 / 4.0.3](https://support.mozilla.org/en-US/kb/end-of-support-firefox-lockwise) | Mozilla identifies the final release of each standalone app. |
| Taobao · mainland China, iOS / Android | [Unresolved](research/taobao.md) | Device guides document specific builds, while the in-app campaign and invitation-based launches have no published minimum build. |

## Look up a release

From a checkout, search by name or identifier and optionally choose a platform. Python 3 and its standard library are sufficient.

```sh
python3 scripts/lookup.py taobao --platform ios
python3 scripts/lookup.py 淘宝 --platform android
python3 scripts/lookup.py calibre --platform windows
```

Each result identifies the edition, the strength of the cutoff evidence and the available source links. An **observed version** is a version recorded by a store, device report or package maintainer. Only a **verified** decision establishes the last qualifying version for the stated scope.

The catalog links to publisher archives when available. Old software can contain security vulnerabilities or depend on retired services. [Research methodology](docs/METHODOLOGY.md) · [Coverage and data sources](docs/COVERAGE.md)

Run `python3 scripts/validate.py` to check all datasets.
