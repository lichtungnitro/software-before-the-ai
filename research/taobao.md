# Taobao / 淘宝

**10.23.10 is a documented version to investigate on both iPhone and Android. The exact last release free of built-in generative AI remains unresolved on both platforms.** This entry covers the main mainland Chinese consumer app. The separately listed Taobao HD, Lite, Deals and international editions have their own histories.

| Question | iPhone | Android |
| --- | --- | --- |
| Which release was observed before the April 2023 image-generation event? | **10.23.10**, documented April 26 on an iPhone 12 running iOS 15.4.1. [Device report](https://jingyan.baidu.com/article/a3a3f81114a5f0cca2eb8a8a.html) | **10.23.10**, documented April 26 on a Xiaomi 12 running MIUI 14.0.22. [Device report](https://jingyan.baidu.com/article/3065b3b645ad6dffcff8a483.html) |
| Which release was observed before public reports of the Wenwen LLM assistant? | **10.27.30**, documented September 2 on an iPhone 12. [Device report](https://jingyan.baidu.com/article/ce4366496363de7673afd392.html) | **10.27.40**, documented September 7 on a vivo S17. [Device report](https://read01.com/zh-cn/RAN7LGy.html) |
| Can a particular release be certified as the last qualifying one? | Unresolved · publisher minimum build and account eligibility unknown | Unresolved · publisher minimum build and account eligibility unknown |

The dated device reports identify which version the author used for ordinary shopping tasks. They establish that a client existed by that date. They give no test results for the AI features. A separate April 28 report identifies iPhone 10.23.0 as build 29319083. An Android guide lists the newer 10.23.20 on April 29 itself. Neither source ties those builds to activation. [iPhone build metadata](https://github.com/PlayCover/PlayCover/issues/930) · [Android 10.23.20 device report](https://jingyan.baidu.com/article/7c6fb428cbca81c1652c906d.html)

## What counts as AI here

| Date in China | What shoppers could access | Evidence |
| --- | --- | --- |
| April 29, 2023 | The Maker Festival's **AI BUY** mini-program generated a product picture from a typed description. Taobao exposed it through in-app search and event navigation. The event rules called for an up-to-date app and gave no version number. | [Contemporaneous launch report and event rules](https://www.ithome.com/0/689/987.htm) · [April 28 event preview](https://city.sina.com.cn/news/2023-04-28/detail-imyrxrfr2853554.shtml) |
| By July 24, 2023 | The **AI 创作小助手** generated profile portraits inside Taobao. | [Contemporaneous report](https://www.ithome.com/0/707/795.htm) |
| By September 8, 2023 | **淘宝问问** was in beta. Early users could apply through in-app search or join with an invitation. Alibaba identifies it as an embedded LLM shopping assistant. | [September 8 report](https://www.36kr.com/newsflashes/2422963571827460) · [How the early beta worked](https://www.ithome.com/0/717/945.htm) · [Alibaba's account](https://home.alibabagroup.com/en-US/document-1738398759789789184) |

The repository counts both first-party image generation and LLM assistants. Someone interested specifically in the launch of Wenwen can use the September observations. Both September versions postdate the image-generation rollout. A community iOS guide also describes 10.59.20 as preceding a later shopping-assistant interface. The 2023 records establish earlier in-app generative features. [Community iOS version notes](https://qianling.pw/ios-app/)

## Find the result in the repo

On GitHub, open the [reviewed index](INDEX.md) and find **Taobao**. The [machine-readable records](../data/apps.json) use `app_id: taobao`, `region: CN` and one row per mobile platform. Read `last_pre_llm_version` for the cutoff, `observed_versions` for device sightings and `documented_rollouts` for features. Here both cutoff fields are `null` and both statuses are `ambiguous`.

From a checkout of the repo:

```sh
python3 scripts/lookup.py taobao --platform ios
python3 scripts/lookup.py taobao --platform android
```

The [2017 iOS store observation](https://github.com/divaymohan/apple-apps/blob/659a2dea8c8f3633c83ed0c51df9110feb6fee03/AppleStore.csv#L501) also records **6.7.2** for the same App Store ID. That is an older reference point for the main app.

## Getting a copy

The catalog's `download_url` is empty on both platforms. No public, version-pinned publisher installer for the April candidate was established. The official product identifiers are Apple App Store **387682726** and Android **com.taobao.taobao**. An existing copy displaying 10.23.10 can be matched to the device observations above. Its ability to sign in, pay, or avoid later server-delivered features has not been tested. [Apple's mainland listing](https://apps.apple.com/cn/app/id387682726) · [Publisher's Google Play listing](https://play.google.com/store/apps/details?id=com.taobao.taobao)
