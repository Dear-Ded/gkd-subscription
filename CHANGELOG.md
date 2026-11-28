# 更新日志

本订阅的显著变更记录在此。版本号与订阅文件 `dist/gkd.json5` 内的 `version` 字段一致：由每日自动合并任务在内容发生变化时递增，无变化不升版。

## [35] - 2026-11-28

### 内容

对照 v34（1120 应用 / 5136 规则组 / 7983 规则 / 16 全局组，2,897,037 字节），本版为 1120 应用 / 5136 规则组 / 7983 规则 / 16 全局组，订阅文件约 2.8 MB（2,897,717 字节）。修复 Codex 在 PR #30 合并后审出的 3 个 P2 问题；上游版本未变（Lin-arm 仍为 v647，其余十四源不变），未改上游 dist，只改自有层与合并脚本。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组，也没有改开屏组。

- 组 key 稳定：`scripts/merge.py` 新增 `stabilize_keys`，按上一版已发布 dist 固定组 key——同名组沿用旧 key，新组取未用过的最大 key+1。v34 里上游插入新组导致 4 个应用共 65 组 key 顺移（番茄免费小说 20 组、京东 13 组、微博 27 组、雪球 5 组），订阅者保存的每组开关会落到别的组上；本版把这 65 组恢复到 v33 的 key，新组排到最后（番茄免费小说「功能类-自动[展开]简介」key 44、京东「功能类-自动进入[快速验证]」key 32、微博「其他-关闭关注提示」key 57、雪球新增 4 组 key 9–12）。其余应用的 key 与 v34 完全一致。注意：本版的 key 修复以 v33 为参照做了一次性校正；今后每日合并以最近一版为参照，插入新组不再顺移。
- GitHub（`com.github.android`）「功能类-自动批准授权验证」：自有层覆写，只补回 `matchRoot: true`，其余与上游 v647 一致。v34 的上游 perf 改写去掉 `matchRoot` 后，2FA 输码时事件节点是 EditText，默认匹配从事件节点向下找子孙，到不了根部的 `android:id/content`，批准按钮会 miss。
- 番茄免费小说（`com.dragon.read`）「功能类-自动[展开更多]评论」：自有层覆写，去掉上游新增的通用 `[text="展开"]` 匹配——它不限定评论区，在小说阅读页与短剧页会把简介的「展开」也点开，与同批新增的「功能类-自动[展开]简介」冲突；恢复为只匹配「展开」开头、「回复」/「更多」结尾的节点。其余与上游 v647 一致，待上游给出带评论区限定的选择器后再跟进。

背景：PR #30 在 2026-11-28 01:52 UTC 合并后，Codex 审阅于 02:00 UTC 完成，3 个问题已随 v34 发布，本版为修复跟进。

## [34] - 2026-11-28

### 内容

对照 v33（1120 应用 / 5129 规则组 / 7969 规则 / 16 全局组，2,890,834 字节），本版为 1120 应用 / 5136 规则组 / 7983 规则 / 16 全局组，订阅文件约 2.8 MB（2,897,037 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组，也没有改开屏组。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v645 → v647。v33 所用 dist 是 v645（chore: 🚀v645，2026-11-26T01:52:47Z，commit c4e146ce），文件 1,398,848 字节。中间还有一版 v646（chore: 🚀v646，2026-11-27T01:50:23Z，commit caad668a），文件 1,404,195 字节。本次拉取的 v647 dist 为 1,406,182 字节，与 a16813b1（chore: 🚀v647，2026-11-28T01:32:36Z）的 `dist/gkd.json5` 逐字节相同，与 c4e146ce、caad668a 都逐字节不同。主分支最新提交就是 a16813b1，没有比 v647 更新、尚未打进 dist 的提交。对照 v645 与 v647 的 dist，只动了七个应用。番茄免费小说、GitHub、京东、微博、雪球进入合并结果；闲鱼、小红书被底座同名组挡住。雪球原有的三组也在 dist 里改了，同样被底座同名组挡住，新增的四组进来了。荣耀桌面整份应用与 v645 dist 相同，没有进入这次差异。

v645 与 v647 之间的提交：fix 小红书「权限提示-通知权限」（2026-11-26T13:07:25Z，d013d8d1，#507）、fix 微博发现页弹窗另一种样式（2026-11-26T13:52:38Z，b57eace3，#505）、fix 荣耀桌面「功能类-[不]添加小部件到桌面」（2026-11-26T14:16:08Z，0a29c98e）以及随后的 Revert（2026-11-26T14:50:18Z，83fb86a0）、fix 闲鱼「功能类-自动点击[查看原图]」（2026-11-26T14:59:00Z，2f915ded）、perf GitHub「功能类-自动批准授权验证」（2026-11-26T15:58:36Z，f3809110）、雪球六笔（2026-11-26T16:18:05Z d4a5220f、16:22:00Z a8d47603、16:47:41Z 71ae09c4、16:59:39Z c1dbf8a1、17:04:42Z ef7513c6、17:06:52Z f58a6563）、feat 京东「功能类-自动进入[快速验证]」（2026-11-27T03:57:48Z，85da1563）、feat 番茄免费小说「功能类-自动[展开]简介」（2026-11-27T07:10:06Z，9a1acfa6，#508）。荣耀桌面那笔 fix 被 Revert 抵消，v647 dist 里没有留下改动。#508 的补丁同时改了「功能类-自动[展开更多]评论」。其余这些都进了 v647 dist。v646 的 dist 已经包含小红书、微博、闲鱼、GitHub 和雪球；v647 在此之上加上京东和番茄免费小说。下面按 v647 dist 的最终内容写，不把后来又改过的中间选择器当成已发布结果。

其余十四个来源的版本与 v33 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v131、言木七 v54、AIsouler 自用续订 v124、Ling v16、GK-Lemon-D v59、火山虾 v78、YaChengMu v155。合并结果里只有番茄免费小说、GitHub、京东、微博、雪球这五个应用有变化。

Lin-arm v647 实际并入：

- 番茄免费小说（`com.dragon.read`）「功能类-自动[展开更多]评论」（序号仍是 23）由 1 条改为 2 条。说明由「小说段评区/短剧评论区, 点击[展开更多/展开n条回复]」改为「小说段评区/评分区; 短剧评论区/剧评区, 点击[展开/展开更多/展开n条回复]」。`fastQuery` 和 `actionCd: 500` 从原来那条规则挪到组上，两条都不再单独写。组没有 `enable: false`，功能类默认关闭，不会自动点击。各源里只有 Lin-arm 有这个组名，合并结果与 v647 这组一致，只是组序号按合并排成 23，上游 key 是 21
  - key 1「①[展开]点评」：活动页 `com.dragon.community.impl.comment.playlet.list.page.CSSPlayletCommentListActivity` 和 `com.dragon.community.impl.list.page.CSSBookCommentListActivity`。选择器没有 `@`，GKD 点最后一段，也就是可点击的「展开」。它的祖先是 ViewGroup，这个 ViewGroup 后面隔一个兄弟是 LinearLayout，LinearLayout 的直接子节点是以「后点评」结尾的文字（`[text$="后点评"] < LinearLayout -2 ViewGroup > [text="展开"][clickable=true]`）。快照 [35494357](https://i.gkd.li/i/35494357)、[35494382](https://i.gkd.li/i/35494382)，示例 [5ffee787](https://e.gkd.li/5ffee787-dca6-4e91-b908-96bf8f896e47)、[f81b3c2e](https://e.gkd.li/f81b3c2e-5b56-4dab-8eac-ba38396ab972)
  - key 2「②[展开]评论/回复」：活动页仍是 `.reader.ui.ReaderActivity`、`.pages.main.MainFragmentActivity`、`.ad.openingscreenad.OpeningScreenADActivity`、`.component.shortvideo.impl.ShortSeriesActivity`。两条 `matches` 都要出现。第一条仍是评论区那个变高的 `android:id/content`。第二条改成两边取一：可点击节点里面有可见、以「展开」开头、以「回复」或「更多」结尾的文字（`@` 在这个可点击节点上）；或者文字就是「展开」的可点击节点（`(@[clickable=true] > [visibleToUser=true][text^="展开"][text$="回复" || text$="更多"]) || ([clickable=true][text="展开"])`）。`matches` 是数组时点最后一条。快照仍有 [35147917](https://i.gkd.li/i/35147917)、[35147919](https://i.gkd.li/i/35147919)、[35173217](https://i.gkd.li/i/35173217)、[35203330](https://i.gkd.li/i/35203330)、[35203316](https://i.gkd.li/i/35203316)，新增 [35494237](https://i.gkd.li/i/35494237)。排除快照仍是 [35165101](https://i.gkd.li/i/35165101)、[35173220](https://i.gkd.li/i/35173220)。示例仍有 [e0c12712](https://e.gkd.li/e0c12712-4b1e-4b75-a9ec-d1a8042156f6)、[0d2d257a](https://e.gkd.li/0d2d257a-abda-4255-b971-faf06b565cb7)，新增 [4fc71629](https://e.gkd.li/4fc71629-5b01-4c60-a356-0b89c3b7e162)
- 番茄免费小说新增「功能类-自动[展开]简介」（2 条，序号 24）。说明是「小说/短剧简介, 点击1次[展开]」。组上 `actionMaximum: 1`、`resetMatch: "match"`。各源里只有 Lin-arm 有这个组名，合并结果与 v647 这组一致，上游 key 是 22。组没有 `enable: false`，功能类默认关闭，不会自动点击。两条都没有 `@`，点的都是「展开」
  - key 1「①[展开]短剧简介」：规则上 `fastQuery`。活动页 `.reader.ui.ReaderActivity`、`.component.shortvideo.impl.ShortSeriesActivity`。以「简介」结尾的 `vid="title"` 的下一个兄弟是 ViewGroup，点这个 ViewGroup 里面可点击、可见的「展开」（`[vid="title"][text$="简介"] + ViewGroup > [text="展开"][clickable=true][visibleToUser=true]`）。快照 [35494458](https://i.gkd.li/i/35494458)、[35494462](https://i.gkd.li/i/35494462)，示例 [20fe96c0](https://e.gkd.li/20fe96c0-f378-4a0d-8146-7bc089b7c864)、[e4e767e6](https://e.gkd.li/e4e767e6-5d15-46af-8065-dffdcd42da09)
  - key 2「②[展开]小说简介」：这条没有 `fastQuery`。活动页 `.reader.detail.BookDetailActivity`。「简介」后面若干个兄弟里有一个 2 个子节点的 View，点它里面可见、可点击的「展开」（`TextView[text="简介"] +n View[childCount=2] > TextView[clickable=true][text="展开"][visibleToUser=true]`）。快照 [35494527](https://i.gkd.li/i/35494527)，示例 [c88a8d15](https://e.gkd.li/c88a8d15-fb17-44d3-b350-7d73df73e566)
- 番茄免费小说序号 -1、0–6、10、16–22 的十六组未改。新组占了序号 24，原先序号 24–43 的二十组改为 25–44，选择器未改。从「局部广告-首页-右侧红包浮窗」到「全屏广告-VIP免费领弹窗」。该应用现为 38 组
- GitHub（`com.github.android`）「功能类-自动批准授权验证」（仍为 2 条，序号仍是 1）。说明仍是「输入2位数字后-> 批准-> 关闭」，活动页仍是 `.twofactor.TwoFactorActivity`。组上新增 `fastQuery`。组没有 `enable: false`，功能类默认关闭，不会自动点击。各源里只有 Lin-arm 有这个组名，合并结果与 v647 这组一致。另一组「功能类-PR自动展开详情」（序号 2，1 条）未改
  - key 0 改名为「①点击[批准]」。去掉 `matchRoot`。选择器改成快查写法：点可点击的 View，它的第一个子节点文字是「批准」。这个 View 前面隔一个兄弟是输入长度至少 2 的 EditText，EditText 前面再隔一个是「身份验证请求」，「身份验证请求」是另一个 View 的直接子节点，再走到 `android:id/content`（`@View[clickable=true][getChild(0).text="批准"] -2 EditText[text.length>=2] -2 [text="身份验证请求"] < View <<5 [id="android:id/content"]`）。旧选择器要求输入长度等于 2，并且画面上有包含「@」的文字。快照仍是 [28906388](https://i.gkd.li/i/28906388)，示例仍是 [86a9d677](https://e.gkd.li/86a9d677-6f59-4a3a-81d0-8bb0d6847ca9)
  - key 1 改名为「②点击[关闭]」。`preKeys` 仍是 `[0]`。点可点击、且第一个子节点是可见「关闭」的 View。它前面 1 到 2 位是「登录已批准」「无法批准」或「未找到登录请求」，这段文字是另一个节点的直接子节点，再走到 `android:id/content`（`@View[clickable=true][getChild(0).text="关闭" && visibleToUser=true] -(1,2) [text="登录已批准" || text="无法批准" || text="未找到登录请求"] < * <<5 [id="android:id/content"]`）。快照仍是 [25366553](https://i.gkd.li/i/25366553)、[25366549](https://i.gkd.li/i/25366549)、[32758660](https://i.gkd.li/i/32758660)。示例仍是 [e18eed95](https://e.gkd.li/e18eed95-993a-4148-b486-27e64e709188)、[c165be1d](https://e.gkd.li/c165be1d-f0d4-47d0-8a39-3aac562885b1)、[4bb620ca](https://e.gkd.li/4bb620ca-a35a-40c1-ad80-8c777bf86d02)
- 京东（`com.jingdong.app.mall`）新增「功能类-自动进入[快速验证]」（1 条，序号 19）。说明是「一般查看 购物车/订单 时会弹验证, 点击1次[快速验证]」。各源里只有 Lin-arm 有这个组名，合并结果与 v647 这组一致，上游 key 是 18。组没有 `enable: false`，功能类默认关闭，不会自动点击。`actionMaximum: 1`、`resetMatch: "match"`、`fastQuery` 写在这条规则上，不在组上。活动页 `.bundle.jdrhsdk.JDRiskHandleActivity`。点可点击的「快速验证」（`[text="快速验证"][clickable=true]`）。快照 [35494504](https://i.gkd.li/i/35494504)，示例 [a8907154](https://e.gkd.li/a8907154-923b-4957-918f-2323e2fa767a)。序号 0–2、4–6、10–18 的十五组未改。新组占了序号 19，原先序号 19–31 的十三组改为 20–32，选择器未改。从「通知提示」到「持续-应用提示弹窗-还款免密弹窗」。该应用现为 29 组
- 微博（`com.sina.weibo`）「全屏广告-发现页弹窗」（仍为 1 条，序号仍是 29）。说明由「点击×关闭发现页的发布会/直播推广弹窗」改为「点击×关闭发现页的弹窗」。`matchRoot`、`actionMaximum: 1`、`resetMatch: "match"` 仍写在规则上，活动页仍是 `.MainTabActivity`。点击目标改成宽小于 114 且高小于 114 的可点击节点（`@[clickable=true][width<114 && height<114] < [index=parent.childCount.minus(1)] <n * -> FrameLayout[childCount=1][getChild(childCount.minus(1)).desc="广告"][visibleToUser=true] -n * <<(10-n) [id="android:id/content"]`）。这条路径要经过可见、且最后一个子节点 desc 为「广告」的 FrameLayout，再走到 `android:id/content`。快照仍有 [35392878](https://i.gkd.li/i/35392878)，新增 [35441180](https://i.gkd.li/i/35441180)。示例仍是 [6156ade7](https://e.gkd.li/6156ade7-09c6-48f6-897e-4e701f648b2e)。各源里只有 Lin-arm 有这个组名，合并结果与 v647 这组一致。组没有 `enable: false`，全屏广告默认关闭，不会自动点击
- 微博新增「其他-关闭关注提示」（2 条，序号 30）。说明是「点击×关闭推荐关注横幅和铁粉关系提示」。组上 `fastQuery`，活动页 `.search.searchv3.SearchActivityV2`。各源里只有 Lin-arm 有这个组名，合并结果与 v647 这组一致，序号也是 30。组没有 `enable: false`，「其他」分类默认关闭，不会自动点击。两条都没有 `@`，GKD 点最后一段
  - key 0「推荐关注」：点可点击的 `vid="close_layout"`。它的前一个兄弟有 3 个子节点，直接子节点里有可见的 `vid="wbAvatar"`。`wbAvatar` 后面是一个 2 个子节点的兄弟，再后面是可点击的 `vid="btnFollow"`（`[vid="btnFollow"][clickable=true] - [childCount=2] - [vid="wbAvatar"][visibleToUser=true] < [childCount=3] + [vid="close_layout"][clickable=true]`）。快照 [35419581](https://i.gkd.li/i/35419581)，示例 [aeacd3ec](https://e.gkd.li/aeacd3ec-8c8a-44ed-9908-a466c7067046)
  - key 1「铁粉关系」：点可点击的 `vid="ivClose"`。它前面是可见、包含「铁粉关系」且以「查看详情」结尾的 `vid="tvTipMsg"`，再前面是 `vid="ivTipIcon"`（`[vid="ivTipIcon"] + [vid="tvTipMsg"][text*="铁粉关系" && text$="查看详情"][visibleToUser=true] + [vid="ivClose"][clickable=true]`）。没有快照，没有示例链接
- 微博序号 8、9、14、17–28 的十四组未改。新组占了序号 30，原先序号 30–56 的二十七组改为 31–57，选择器未改。从「全屏广告-兴趣领域推荐」到「评价提示」。该应用现为 43 组
- 雪球（`com.xueqiu.android`）新增四组。都没有 `enable: false`。局部广告、全屏广告、功能类、「其他」默认关闭，不会自动点击。各源里只有 Lin-arm 有这四个组名，合并结果与 v647 一致，序号也与上游 key 相同。原先序号 4–8 的五组改为 8–12，选择器未改：「全屏广告-首页广告」「局部广告-首页信息流广告」「局部广告-评论区信息流广告」「持续-页面内广告-信息流广告」「持续-页面内广告-评论区广告」。雪球现为 12 组
  - 「局部广告」（5 条，序号 4）。说明是「卡片/横幅/AI_Tooltip」。组上 `fastQuery`。五条都没有 `@`，点各自最后一段
    - key 0「首页顶部卡片」：活动页 `.mainnesting.view.MainNestingActivity`。「点击领取」在 `vid="tv_fund_obtain"` 里面，这个节点的下一个兄弟是可点击的 `vid="iv_fund_big_card_close"`，点关闭（`[text="点击领取"] <<(6-n) [vid="tv_fund_obtain"] + [vid="iv_fund_big_card_close"][clickable=true]`）。快照 [35472886](https://i.gkd.li/i/35472886)，示例 [d21fab74](https://e.gkd.li/d21fab74-c83d-4ccf-9141-48fb7309023c)
    - key 1「横幅」：活动页 `.mainnesting.view.MainNestingActivity`、`.stockmodule.stockdetail.RipplingStockDetailActivity`、`.common.search.USearchActivity`。两条 `anyMatches`。一条点可点击的 `vid="iv_ad_bee_close"`，它前面是 `vid="btn_ad_bee_action"`。另一条点可点击的 `vid="iv_close"`，前面经过 `vid="btn_go_open"`、`vid="tvSubDesc"` 和 `vid="ivIcon"`。快照 [35473208](https://i.gkd.li/i/35473208)、[35474651](https://i.gkd.li/i/35474651)、[35474361](https://i.gkd.li/i/35474361)，示例 [354a3d80](https://e.gkd.li/354a3d80-979b-40cd-a7f0-d491220ee07e)、[dd3310db](https://e.gkd.li/dd3310db-e561-4ee0-aefa-f3322ca6410b)、[d207e603](https://e.gkd.li/d207e603-dfaf-4c87-9ca2-5f5271f6e3be)
    - key 2「AI_Tooltip」：活动页 `.mainnesting.view.MainNestingActivity`。可见的 `vid="home_ai_guide_tip"` 后面是可点击的 `vid="home_ai_guide_close_img"`，点后者。示例 [f1004a22](https://e.gkd.li/f1004a22-94d9-4b8a-99e2-a572921a0ffc)。没有快照
    - key 3「文章尾部卡片」：活动页 `.community.StatusDetailActivityWithNewWeb`。可见的 `vid="ad_image"` 后面隔一个兄弟是可点击的 `vid="iv_close"`，点后者。快照 [35473510](https://i.gkd.li/i/35473510)、[35474156](https://i.gkd.li/i/35474156)，示例 [707d9e43](https://e.gkd.li/707d9e43-52f9-42b7-9a37-82fb66f27e4e)
    - key 4「搜索页卡片」：活动页 `.common.search.USearchActivity`。可见的 `vid="mark_ad"` 前面是可点击的 `vid="ib_close_ad"`，点后者（`[vid="mark_ad"][visibleToUser=true] - [vid="ib_close_ad"][clickable=true]`）。快照 [35473705](https://i.gkd.li/i/35473705)，示例 [a9905b8f](https://e.gkd.li/a9905b8f-109f-41ca-bd8b-a21a88a20199)
  - 「全屏广告-开通股票账户」（1 条，序号 5）。说明是「进入某股票 -> 股票开通股票账户 -> x掉」。规则上 `fastQuery`。活动页 `.stockmodule.stockdetail.RipplingStockDetailActivity`。没有 `@`，点可点击的 `vid="image_close"`，它后面是「开通股票账户」（`[text="开通股票账户"] - [vid="image_close"][clickable=true]`）。快照 [35475071](https://i.gkd.li/i/35475071)，示例 [d4323015](https://e.gkd.li/d4323015-34d0-473c-b2a9-334f0cb6a22c)
  - 「功能类-自动点击[查看原图]」（1 条，序号 6）。组上没有说明。规则上 `fastQuery`。活动页 `.common.imagebrowse.inner.ui.ImageBrowseActivity`。点可点击的「查看原图」（`[text="查看原图"][clickable=true]`）。快照 [35474051](https://i.gkd.li/i/35474051)，示例 [b9848418](https://e.gkd.li/b9848418-42d3-4fa7-abb5-75f363c9b7dc)
  - 「其他-关闭关注Tip」（1 条，序号 7）。说明是「某人主页,底部弹出[关注TA...] -> x掉」。规则上 `fastQuery`。活动页 `.community.UserProfileActivity`。`@` 在可点击的 `vid="designImageClose"` 上，它在 `vid="designContentContainer"` 里面。后面是一个 2 个子节点的兄弟，再后面是文字「关注」（`[vid="designContentContainer"] > @[vid="designImageClose"][clickable=true] + [childCount=2] + [vid="designRightText"][text="关注"]`）。快照 [35475314](https://i.gkd.li/i/35475314)，示例 [c0f2825f](https://e.gkd.li/c0f2825f-ee37-4324-a479-db705300c9f1)

被更高层同名组挡住、未进入合并结果：

- 闲鱼（`com.taobao.idlefish`）「功能类-自动点击[查看原图]」：Lin-arm 由 1 条改为 2 条。活动页挪到组上，在原来两个 FlutterBoost 页之外加上 `.photo.DetailPhotoGalleryActivity`。key 0「直接」点 `vid="origin_image_btn"` 里可见、文字非空的 `vid="origin_image_text"`（`@[vid="origin_image_btn"][clickable=true] > TextView[vid="origin_image_text"][text!=null][visibleToUser=true]`）。快照 [35469352](https://i.gkd.li/i/35469352)，示例 [0da230d0](https://e.gkd.li/0da230d0-77ed-45a1-b366-c193ef7f8c3c)。key 1「反射法」加上 `actionCdKey: 0`，选择器收成可点击的 `desc="查看原图"`，并要求走到 `vid="fish_layer_container_id"`。快照仍是 [15463399](https://i.gkd.li/i/15463399)、[27207770](https://i.gkd.li/i/27207770)。AIsouler 底座有同名组（序号 6，1 条）：活动页只有 `com.idlefish.flutterbridge.flutterboost.boost.FishFlutterBoostActivity`，选择器仍是可见的 `desc="查看原图"`，快照仍是 [15463399](https://i.gkd.li/i/15463399)，示例仍是 [12b60303](https://m.gkd.li/57941037/12b60303-4fb8-4786-b636-4efef10f3d78)。同名组以底座为准，合并结果与 v33 相同。功能类默认关闭，但这组本来就在，点的仍是底座那一条
- 小红书（`com.xingin.xhs`）「权限提示-通知权限」：Lin-arm 由 2 条改为 3 条。活动页从两条规则挪到组上。key 0 加上名称「全屏弹窗1」和示例 [09ce8f07](https://e.gkd.li/09ce8f07-c7b6-4ce5-bd85-c8082295f7d9)，选择器未改。key 1 加上名称「底部横幅」和示例 [e390e4d3](https://e.gkd.li/e390e4d3-3101-46a2-9496-27a6bc1c89cd)，选择器未改，活动页仍是 `.index.v2.IndexActivityV2`。新增 key 2「全屏弹窗2」：两条 `matches` 都要出现，可见的「打开推送通知」，以及可点击的「取消」。没有写 `@`，GKD 点最后一条，也就是「取消」。快照 [35457404](https://i.gkd.li/i/35457404)，示例 [2cc4ec49](https://e.gkd.li/2cc4ec49-84b8-45fc-922c-2de4317cf26c)。AIsouler 底座有同名组（序号 1，2 条），与 Lin-arm v645 这组相同：活动页还在规则上，没有名称，没有 key 2，没有快照 35457404。组上仍是 `actionMaximum: 1`、`fastQuery`、`resetMatch: "app"`。同名组以底座为准，合并结果与 v33 相同。权限提示默认关闭，但这组本来就在，点的仍是底座那 2 条
- 雪球「局部广告-信息流广告」（序号 1）：Lin-arm 仍是 1 条，仍点 `vid="ad_close"`。活动页在首页之外加上 `.stockmodule.stockdetail.RipplingStockDetailActivity`，快照在 [13388227](https://i.gkd.li/i/13388227) 之外加上 [35474041](https://i.gkd.li/i/35474041)、[35474228](https://i.gkd.li/i/35474228)。AIsouler 底座有同名组（序号 1，1 条）：活动页仍是完整类名 `com.xueqiu.android.mainnesting.view.MainNestingActivity`，选择器仍是 `[id="com.xueqiu.android:id/ad_close"]`，快照仍是 [13388227](https://i.gkd.li/i/13388227)，示例仍是 [d05d1eec](https://m.gkd.li/33366298/d05d1eec-cda5-4d37-a494-8eef7b7871dd)。同名组以底座为准，合并结果与 v33 相同
- 雪球「局部广告-评论区广告」（序号 2）：Lin-arm 仍是 1 条。选择器由只点 `vid="ad_card_close"` 放宽为 `vid="ad_card_close"` 或 `vid="ad_banner_close"`，快照加上 [35473004](https://i.gkd.li/i/35473004)。AIsouler 底座有同名组（序号 2，1 条）：活动页仍是 `com.xueqiu.android.community.StatusDetailActivity`，选择器仍是 `[id="com.xueqiu.android:id/ad_card_close"]`，快照仍是 [13388361](https://i.gkd.li/i/13388361)。同名组以底座为准，合并结果与 v33 相同
- 雪球「全屏广告」（序号 3）：Lin-arm 由 1 条改为 2 条。`fastQuery` 挪到组上。原来写在组上的 `matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"` 挪到 key 0「首页」，选择器仍点可见的 `vid="image_cancel"`，快照仍是 [22995479](https://i.gkd.li/i/22995479)。新增 key 1「小雪理财课」，活动页 `.community.guide.PaddyUserGuideActivity`，点可点击的 `vid="tv_skip"`，它前面是 `vid="xue_video_container"`。快照 [35474964](https://i.gkd.li/i/35474964)，示例 [389ced96](https://e.gkd.li/389ced96-2385-4349-8ef3-87cb71c0cb88)。AIsouler 底座有同名组（序号 3，1 条），与 Lin-arm v645 这组相同：次数限制仍在组上，没有 key 1，没有快照 35474964。同名组以底座为准，合并结果与 v33 相同。全屏广告默认关闭，但这组本来就在，点的仍是底座那一条

荣耀桌面（`com.hihonor.android.launcher`）不在这次 dist 差异里。fix 把不触发的问题改了一版，Revert 又退了回去。v647 这份应用与 v645 相同：「功能类-[不]添加小部件到桌面」仍是 1 条，`matchTime: 5000`、`actionMaximum: 1`，两条 `matches` 仍是可见的「添加到主屏幕」和可点击的「取消」，快照仍是 [34847270](https://i.gkd.li/i/34847270)。这次没有新内容可并入。

没有新的组被守卫丢掉。误触守卫挡住的组（合计 2155 组，与 v33 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源的版本都没变，丢掉的组与 v33 相同。

净变化：应用数不变，规则组 +7，规则 +14。全局组仍为 16。文件比 v33 大了 6,203 字节。

## [33] - 2026-11-27

### 内容

对照 v32（1119 应用 / 5124 规则组 / 7963 规则 / 16 全局组，2,888,388 字节），本版为 1120 应用 / 5129 规则组 / 7969 规则 / 16 全局组，订阅文件约 2.8 MB（2,890,834 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v644 → v645（chore: 🚀v645，2026-11-26T01:52:47Z，commit c4e146ce）。v32 所用 dist 是 v644，文件 1,396,696 字节。本次拉取的 v645 dist 为 1,398,848 字节，与 c4e146ce 的 `dist/gkd.json5` 逐字节相同，与 v644 逐字节不同。对照两版 dist，只动了五个应用。测测、微博、红果免费短剧进入合并结果；豆瓣、腾讯文档被底座同名组挡住。v644 之后、已打进 v645 dist 的提交：feat 测测「权限提示 / 全屏广告 / 局部广告」（2026-11-25T13:23:47Z，42e16b93，#502）、feat 微博「全屏广告 +2」（2026-11-25T14:11:02Z，135bd919，#501）、fix 腾讯文档「开屏广告」（2026-11-25T14:20:55Z，898ca087，#503）、perf 红果免费短剧「功能类-[上滑]继续看短剧」（2026-11-25T14:42:07Z，85c0d950）、perf 豆瓣「开屏广告」（2026-11-25T15:50:08Z，c12b2adf）。ci 加个图标（2026-11-25T16:54:48Z，e316bb6a）只改了构建工作流的提交说明，把 `chore: v版本号` 换成 `chore: 🚀v版本号`，没有改规则；v645 的提交说明因此带上火箭符号。

其余十三个来源的版本与 v32 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v131、言木七 v54、AIsouler 自用续订 v124、Ling v16、GK-Lemon-D v59、火山虾 v78、YaChengMu v155。合并结果里只有测测、微博、红果免费短剧这三个应用有变化。

Lin-arm v645 实际并入：

- 测测（`com.xxwolo.cc5`）新增应用，3 组（4 条）。各源里只有 Lin-arm 有这个包名，整份并入，应用名、组名和序号都与上游 dist 一致。三组都没有 `enable: false`。权限提示、全屏广告、局部广告默认关闭，不会自动点击
  - 「权限提示-通知权限」（2 条，序号 0）。说明是「点击[×掉/取消]」。活动页 `com.cece.app.MainActivity` 写在组上。key 0「底部横幅」：`matchRoot`、`actionCd: 3000` 写在这条规则上。出现 desc 包含「开启系统通知」时，点它下面可点击、desc 为空、宽小于 106 且高小于 107 的节点，这个节点旁边是 desc「去开启」（`[desc*="开启系统通知"] > @[clickable=true][desc=null][width<106][height<107] + [desc="去开启"]`）。快照 [35392398](https://i.gkd.li/i/35392398)，示例 [94819262](https://e.gkd.li/94819262-26e5-458b-ba2b-a633924d6456)。点的是「去开启」旁的小叉。key 1「弹窗」：`matchTime: 10000`、`actionMaximum: 3` 写在这条规则上，不在组上。点可点击的 desc「取消」，旁边是可点击的 desc「打开通知」（`@[desc="取消"][clickable=true] + [desc="打开通知"][clickable=true]`）。快照 [35392498](https://i.gkd.li/i/35392498)，示例 [26d36064](https://e.gkd.li/26d36064-b217-4a49-993a-83a60d86ea0a)。点的是「取消」
  - 「全屏广告-小组件弹窗」（1 条，序号 1）。说明是「点击[关闭]」。`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"` 写在组上。规则上 `fastQuery`，活动页仍是 `com.cece.app.MainActivity`。点可点击的 desc「关闭」，它的祖先里有以「添加小组件」开头的 View，再往上走到 `android:id/content`（`@[desc="关闭"][clickable=true] <n View[desc^="添加小组件"] < * < * < [id="android:id/content"]`）。快照 [35392522](https://i.gkd.li/i/35392522)，示例 [2d688ba5](https://e.gkd.li/2d688ba5-7c0f-4737-b764-7efc744600e0)
  - 「局部广告-右下角浮窗」（1 条，序号 2）。说明是「点击×掉」。组上 `matchRoot`、`forcedTime: 10000`、`actionCd: 3000`。活动页 `com.cece.app.MainActivity`。点没有子节点、可点击、宽高都小于 80 且可见的 ImageView，它的父节点有 2 个子节点、可点击、宽高都小于 350 且可见。快照 [35392429](https://i.gkd.li/i/35392429)。没有示例链接
- 微博（`com.sina.weibo`）新增两组，都没有 `enable: false`，全屏广告默认关闭，不会自动点击。这两组更高层没有同名组，合并结果与 Lin-arm v645 一致，序号也与上游 key 相同。原先序号 28–54 的 27 组改为 30–56，选择器未改。序号 8、9、14、17–20、22–27 的十三组未改。微博现为 42 组
  - 「全屏广告-小组件弹窗」（1 条，序号 28）。说明是「点击[暂不添加]跳过组件引导」。规则上 `fastQuery`，活动页 `.extlibui.appwidget.business.install.WidgetInstallDialogActivity`。两条 `matches` 都要出现：可见且包含「小组件」的文字，以及可点击的 `vid="tv_refuse"`。没有写 `@`，GKD 点最后一条，也就是 `vid="tv_refuse"`。快照 [35392812](https://i.gkd.li/i/35392812)，示例 [41feacfb](https://e.gkd.li/41feacfb-053c-410f-880f-ac8b8d31d607)
  - 「全屏广告-发现页弹窗」（1 条，序号 29）。说明是「点击×关闭发现页的发布会/直播推广弹窗」。`matchRoot`、`actionMaximum: 1`、`resetMatch: "match"` 写在规则上。活动页 `.MainTabActivity`。点没有子节点的可点击节点，这条路径的另一头是 desc「广告」（`@[clickable=true][childCount=0] <1 [childCount=2] <2 * <1 * >2 [desc="广告"]`）。快照 [35392878](https://i.gkd.li/i/35392878)，示例 [6156ade7](https://e.gkd.li/6156ade7-09c6-48f6-897e-4e701f648b2e)
- 红果免费短剧（`com.phoenix.read`）「功能类-[上滑]继续看短剧」（仍为 2 条，序号仍是 1）只改了说明。由「①读秒结束后[上滑] ②未显示[选集]时,每5秒[上滑]1次」改为「出现 广告/直播间 时上滑跳过, ①读秒结束后[上滑] ②未显示[选集]时,每5秒[上滑]1次」。选择器、活动页、快照、排除快照、示例和上滑参数都没变。这组 v32 已由 Lin-arm 进入，更高层没有同名组，所以说明写进了合并结果，合并结果与 Lin-arm v645 这组一致。组没有 `enable: false`，功能类默认关闭，不会自动上滑。其余三组的序号和选择器未改：Lin-arm 的「权限提示-通知权限」（序号 2），甘霖的「局部广告-阅读-底部卡片广告」（序号 3，写了 `enable: false`）和「全屏广告-阅读-视频广告」（序号 4，写了 `enable: false`）

被更高层同名组挡住、未进入合并结果：

- 豆瓣（`com.douban.frodo`）「开屏广告」：Lin-arm 仍是 9 条（key 0–4、10–13）。组上的说明、`fastQuery`、`matchRoot`、`matchTime: 10000`、`actionMaximum: 2`、`resetMatch: "app"`、`priorityTime: 10000`、`order: -10` 都没变。key 0–3 未改。key 4 加上 `actionCdKey: 3`，选择器未改，仍是点宽高小于 170 的 View，祖先里有 `vid="sdk_view"`。坐标四条（key 10–13）由两条 `anyMatches` 改成一条 `matches`：`[vid="ad_view" || vid="sdk_view"][visibleToUser=true][width>=720][childCount!=0]`。旧的第二条是 `vid="sdk_view"` 里面的 `vid="animation_view"`，这次改成 `ad_view` 或 `sdk_view` 自身可见、宽至少 720 且有子节点。坐标没变。key 10 也加上 `actionCdKey: 3`。key 12「点击坐标③」补快照 [35417943](https://i.gkd.li/i/35417943)。AIsouler 底座有同名组（序号 -1，6 条，key 0–5）：`matchTime: 10000`、`resetMatch: "app"`、`actionMaximumKey: 0`、`priorityTime: 10000`、`order: -10`，没有这次的 `actionCdKey`，也没有快照 35417943。同名组以底座为准，合并结果与 v32 相同。开屏分类默认开启，但这组本来就在，点的仍是底座那 6 条
- 腾讯文档（`com.tencent.docs`）「开屏广告」：Lin-arm 把相邻关系由 `-` 放宽为 `-(1,2)`，文字由以「互动广告」开头放宽为以「互动广告」开头或全文就是「广告」（`@LinearLayout[clickable=true] -(1,2) [text^="互动广告" || text="广告"][visibleToUser=true]`），并补快照 [35394224](https://i.gkd.li/i/35394224)。组上 `fastQuery`、`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"`、`priorityTime: 10000`、`order: -10` 未改。AIsouler 底座有同名组（序号 0），与 Lin-arm v644 这组相同：选择器仍是 `@LinearLayout[clickable=true] - [text^="互动广告"][visibleToUser=true]`，快照仍是 [13198082](https://i.gkd.li/i/13198082)、[23557410](https://i.gkd.li/i/23557410)。同名组以底座为准，合并结果与 v32 相同。开屏分类默认开启，但这组本来就在，点的仍是旧选择器

没有新的组被守卫丢掉。误触守卫挡住的组（合计 2155 组，与 v32 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源的版本都没变，丢掉的组与 v32 相同。

v645 打版之后，Lin-arm 主分支上又有提交。已发布 dist 仍与 c4e146ce 的 `dist/gkd.json5` 逐字节相同，版本号仍是 645。主分支最新提交是 f58a6563（2026-11-26T17:06:52Z），其后没有新的 chore。下面这些都没有进入合并结果：

- fix 小红书（`com.xingin.xhs`）「权限提示-通知权限」适配新样式（2026-11-26T13:07:25Z，d013d8d1，#507）。源码把活动页从两条规则上移到组上，给 key 0、key 1 加上名称「全屏弹窗1」「底部横幅」并补示例，新增 key 2「全屏弹窗2」：出现可见的「打开推送通知」时点可点击的「取消」，快照 [35457404](https://i.gkd.li/i/35457404)，示例 [2cc4ec49](https://e.gkd.li/2cc4ec49-84b8-45fc-922c-2de4317cf26c)。已发布 dist 仍是 2 条，活动页还在规则上，没有名称，没有 key 2，没有这张快照
- fix 微博「全屏广告-发现页弹窗」另一种样式（2026-11-26T13:52:38Z，b57eace3，#505）。源码把说明改成「点击×关闭发现页的弹窗」，选择器换成宽高小于 114 的可点击节点，并补快照 [35441180](https://i.gkd.li/i/35441180)。同时新增 key 30「其他-关闭关注提示」（推荐关注、铁粉关系两条），快照 [35419581](https://i.gkd.li/i/35419581)，示例 [aeacd3ec](https://e.gkd.li/aeacd3ec-8c8a-44ed-9908-a466c7067046)。已发布 dist 这组仍是 v645 的旧说明和旧选择器，没有 key 30，没有这两张快照。本版并入的发现页弹窗是打版时的那一版
- fix 荣耀桌面（`com.hihonor.android.launcher`）「功能类-[不]添加小部件到桌面」不触发（2026-11-26T14:16:08Z，0a29c98e），以及随后的 Revert（2026-11-26T14:50:18Z，83fb86a0）。fix 把 `matchTime` 从 5000 改成 12000、`actionMaximum` 从 1 改成 2，选择器改成从标题「添加到主屏幕」走到 `android:id/button2`。Revert 把源码退回 fix 之前。已发布 dist 仍是退回后的那一版：`matchTime: 5000`、`actionMaximum: 1`，两条 `matches` 分别是可见的「添加到主屏幕」和可点击的「取消」，快照仍是 [34847270](https://i.gkd.li/i/34847270)。这次改动没有进入合并结果
- fix 闲鱼（`com.taobao.idlefish`）「功能类-自动点击[查看原图]」（2026-11-26T14:59:00Z，2f915ded）。源码把活动页挪到组上，并加上 `.photo.DetailPhotoGalleryActivity`。原规则改成 key 1「反射法」，选择器收紧并加上 `actionCdKey: 0`；新增 key 0「直接」，点 `vid="origin_image_btn"`，快照 [35469352](https://i.gkd.li/i/35469352)，示例 [0da230d0](https://e.gkd.li/0da230d0-77ed-45a1-b366-c193ef7f8c3c)。已发布 dist 仍是 1 条，选择器仍是可见的 `desc="查看原图"`，活动页仍只有两个 FlutterBoost 页，没有这张快照
- perf GitHub（`com.github.android`）「功能类-自动批准授权验证」（2026-11-26T15:58:36Z，f3809110）。源码给组加上 `fastQuery`，去掉 key 0 的 `matchRoot`，两条都加上名称，选择器改成快查写法（批准那条要求可见的「身份验证请求」，输入长度由等于 2 放宽为至少 2）。已发布 dist 仍是旧选择器，key 0 仍有 `matchRoot: true`，组上没有 `fastQuery`，两条都没有名称
- feat 雪球（`com.xueqiu.android`）一串提交，都还在源码里。已发布 dist 仍是原来的三组：「局部广告-信息流广告」（序号 1，仍只点 `vid="ad_close"`，活动页仍只有首页，快照仍是 [13388227](https://i.gkd.li/i/13388227)）、「局部广告-评论区广告」（序号 2，仍只点 `vid="ad_card_close"`，快照仍是 [13388361](https://i.gkd.li/i/13388361)）、「全屏广告」（序号 3，`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"` 仍在组上，仍点 `vid="image_cancel"`，快照仍是 [22995479](https://i.gkd.li/i/22995479)）。没有序号 4 及以后的新组
  - feat 局部广告（2026-11-26T16:18:05Z，d4a5220f）。评论区那条加上 `vid="ad_banner_close"`，补快照 [35473004](https://i.gkd.li/i/35473004)。新增 key 4「局部广告」（首页顶部卡片、横幅、AI_Tooltip），快照 [35472886](https://i.gkd.li/i/35472886)、[35473208](https://i.gkd.li/i/35473208)
  - feat 文章尾部卡片（2026-11-26T16:22:00Z，a8d47603）。给上面这组加 key 3「文章尾部卡片」，快照 [35473510](https://i.gkd.li/i/35473510)
  - feat 局部广告（2026-11-26T16:47:41Z，71ae09c4）。信息流那条加上股票详情页，补快照 [35474041](https://i.gkd.li/i/35474041)、[35474228](https://i.gkd.li/i/35474228)。横幅改成两条 `anyMatches`，文章尾部补活动页和快照 [35474156](https://i.gkd.li/i/35474156)，并加 key 4「搜索页卡片」，快照 [35473705](https://i.gkd.li/i/35473705)
  - feat 全屏广告（2026-11-26T16:59:39Z，c1dbf8a1）。原「全屏广告」把次数限制挪到 key 0「首页」，并加 key 1「小雪理财课」，快照 [35474964](https://i.gkd.li/i/35474964)。新增 key 5「全屏广告-开通股票账户」，快照 [35475071](https://i.gkd.li/i/35475071)
  - feat 功能类-自动点击[查看原图]（2026-11-26T17:04:42Z，ef7513c6）。新增 key 6，点可点击的「查看原图」，快照 [35474051](https://i.gkd.li/i/35474051)
  - feat 其他-关闭关注Tip（2026-11-26T17:06:52Z，f58a6563）。新增 key 7，点关注条上的关闭，快照 [35475314](https://i.gkd.li/i/35475314)

净变化：应用 +1，规则组 +5，规则 +6。全局组仍为 16。文件比 v32 大了 2,446 字节。

## [32] - 2026-11-26

### 内容

对照 v31（1118 应用 / 5122 规则组 / 7959 规则 / 16 全局组，2,887,059 字节），本版为 1119 应用 / 5124 规则组 / 7963 规则 / 16 全局组，订阅文件约 2.8 MB（2,888,388 字节）。v31 是同日早些时候的 12306 指纹排除，应用、规则组、规则条数与 v30（2,879,618 字节）相同。本版是在 v31 之上的例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v643 → v644（chore: v644，2026-11-25T02:39:08Z，commit f17adf25）。v31 所用 dist 是 v643，文件 1,395,258 字节。本次拉取的 v644 dist 为 1,396,696 字节，与 f17adf25 的 `dist/gkd.json5` 逐字节相同，与 v643 逐字节不同。对照两版 dist，只动了四个应用。番茄小说海外包、应用包管理组件进入合并结果；大麦、淘宝被底座同名组挡住。v643 之后、已打进 v644 dist 的提交：perf 大麦「开屏广告」（2026-11-24T04:12:25Z，aa10e7f3）、fix 淘宝「全屏广告-弹窗广告」（2026-11-24T11:18:25Z，d00e4b86，#497）、feat (小米)应用包管理组件「功能类-关闭[未验证应用]提示」（2026-11-24T13:03:54Z，de292071，#498）、feat 番茄小说「权限提示-通知权限」（2026-11-24T13:26:13Z，7014842c；提交说明末尾多了一个引号）。
- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v130 → v131（chore: 🐔v131，2026-11-25T16:41:58Z，commit 1fbed478）。v31 所用 dist 是 v130，文件 166,410 字节。本次拉取的 v131 dist 为 166,472 字节，与 1fbed478 的 `dist/gkd.json5` 逐字节相同。对照两版 dist，只动了起点读书的两组，都进入合并结果。v130 之后、已打进 v131 dist 的提交：perf 7.读书（2026-11-25T16:39:20Z，373a7a05）。

其余十三个来源的版本与 v31 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、言木七 v54、AIsouler 自用续订 v124、Ling v16、GK-Lemon-D v59、火山虾 v78、YaChengMu v155。合并结果里只有番茄小说海外包、应用包管理组件、起点读书这三个应用有变化，没有别的应用、规则组或全局组变化。

v644 打版之后，Lin-arm 主分支上又有提交，但已发布 dist 仍与这次 chore 产物逐字节相同，下面这些都没有进入合并结果：

- feat 测测（`com.xxwolo.cc5`）权限提示、全屏广告、局部广告（2026-11-25T13:23:47Z，42e16b93，#502）。源码是新文件，三组：权限提示-通知权限（底部横幅点「去开启」旁的小叉，快照 [35392398](https://i.gkd.li/i/35392398)，示例 [94819262](https://e.gkd.li/94819262-26e5-458b-ba2b-a633924d6456)；弹窗点「取消」，快照 [35392498](https://i.gkd.li/i/35392498)，示例 [26d36064](https://e.gkd.li/26d36064-b217-4a49-993a-83a60d86ea0a)）、全屏广告-小组件弹窗（点「关闭」，快照 [35392522](https://i.gkd.li/i/35392522)，示例 [2d688ba5](https://e.gkd.li/2d688ba5-7c0f-4737-b764-7efc744600e0)）、局部广告-右下角浮窗（点小图，快照 [35392429](https://i.gkd.li/i/35392429)）。已发布 dist 没有 `com.xxwolo.cc5`
- feat 微博（`com.sina.weibo`）全屏广告 +2（2026-11-25T14:11:02Z，135bd919，#501）。源码新增 key 28「全屏广告-小组件弹窗」（点 `vid="tv_refuse"`，快照 [35392812](https://i.gkd.li/i/35392812)，示例 [41feacfb](https://e.gkd.li/41feacfb-053c-410f-880f-ac8b8d31d607)）和 key 29「全屏广告-发现页弹窗」（点「广告」旁没有子节点的可点击节点，快照 [35392878](https://i.gkd.li/i/35392878)，示例 [6156ade7](https://e.gkd.li/6156ade7-09c6-48f6-897e-4e701f648b2e)）。已发布 dist 没有这两组
- fix 腾讯文档（`com.tencent.docs`）开屏广告（2026-11-25T14:20:55Z，898ca087，#503）。源码把 key 0 的相邻关系由 `-` 放宽为 `-(1,2)`，文字由以「互动广告」开头放宽为「互动广告」或以「广告」为全文，补快照 [35394224](https://i.gkd.li/i/35394224)。已发布 dist 仍是旧选择器，没有这张快照
- perf 红果免费短剧（`com.phoenix.read`）「功能类-[上滑]继续看短剧」（2026-11-25T14:42:07Z，85c0d950，Relates to #504）。只改说明，前面加上「出现 广告/直播间 时上滑跳过」。已发布 dist 仍是旧说明
- perf 豆瓣（`com.douban.frodo`）开屏广告（2026-11-25T15:50:08Z，c12b2adf）。源码给 key 4 和坐标点击 key 10 加上 `actionCdKey: 3`，坐标那几条由两条 `anyMatches` 改回一条 `matches`（`vid="ad_view"` 或 `vid="sdk_view"`，可见、宽至少 720、有子节点），并给其中一条补快照 [35417943](https://i.gkd.li/i/35417943)。已发布 dist 没有这张快照，也没有这次的 `actionCdKey`
- ci 加个图标（2026-11-25T16:54:48Z，e316bb6a）。只改构建说明，与规则无关

Lin-arm v644 实际并入：

- 番茄小说（`com.dragon.read.oversea.gp`）新增应用，1 组（3 条）「权限提示-通知权限」（序号 1）。这是海外包，不是已有的番茄免费小说（`com.dragon.read`）。各源里只有 Lin-arm 有这个包名，整份并入，应用名和序号都与上游 dist 一致。说明是「点击"取消"」。组上 `fastQuery`，活动页是 `.widget.ConfirmDialogBuilder`、`.pages.main.MainFragmentActivity` 和 `com.dragon.read.pages.main.MainFragmentActivity`。组没有 `enable: false`，权限提示默认关闭，不会自动点击。三条都没有示例链接
  - key 0「首页」：`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"` 写在这条规则上，不在组上，所以另外两条不受这个次数限制。出现可见的「开启推送提醒」时，点可见的「取消」。不另写活动页，用组上的三个。没有快照
  - key 1「小说阅读页」：活动页改成阅读页 `.reader.ui.ReaderActivity`，覆盖组上的活动页。出现可见的「开启推送通知」时，点可见的「取消」。没有快照
  - key 2：没有规则名。点「暂不开启」的可点击父节点，再往上走到 `android:id/content`（`TextView[text="暂不开启"] < @[clickable=true] <n View < View < ComposeView < * < * < [id="android:id/content"]`）。用组上的活动页。快照 [35333111](https://i.gkd.li/i/35333111)。点的是「暂不开启」
- (小米)应用包管理组件在上游的应用名是「(小米)应用包管理组件」，合并后应用名仍是底座的「应用包管理组件」（`com.miui.packageinstaller`）。新增「功能类-关闭[未验证应用]提示」（1 条，序号 20）。说明是「点击[仍然安装]」。组上 `fastQuery`，活动页 `com.miui.packageInstaller.NewInstallerPrepareActivity`。出现「未验证应用提醒」、并且下一个节点以「该应用未通过」开头时，点「仍然安装」（`[text="未验证应用提醒"] + [text^="该应用未通过"]`，点击目标是另一条 `[text="仍然安装"]`）。快照 [35331944](https://i.gkd.li/i/35331944)，示例 [8838fcbd](https://e.gkd.li/8838fcbd-1967-481b-9a1f-7bf3f8264c74)。组没有 `enable: false`，功能类默认关闭，不会自动点击。打开该分类后，这条点的是「仍然安装」。这个应用原先序号 20–25 的六组改为 21–26，选择器未改：奥怪的「功能类-备案信息弹窗」（1 条）、甘霖的「功能类-自动第三方安装应用」（2 条）、「功能类-自动安装应用」（7 条）、「功能类-自动更新应用」（4 条），梦念逍遥的「功能类-已了解此应用存在风险」（2 条），Adpro 的「功能类-澎湃-自动安装/更新」（6 条）。序号 7 和 13–19 的八组未改。该应用现为 15 组

少年阿鲲 v131 实际并入：

- 起点读书（`com.qidian.QDReader`）「功能类-自动[签到]并跳转[福利中心]」（仍为 2 条，序号仍是 51）。说明仍是「①点击[签到] ②进福利中心(❗配合QD模块用)」。组上仍写了 `enable: false`，并有 `fastQuery`、`resetMatch: "app"`，活动页仍是 `.ui.activity.MainGroupActivity`。组上的 `actionMaximum: 1` 拿掉了，次数改写到两条规则上。选择器、快照和排除快照未改。组本身 `enable: false`，功能类默认也是关闭的，不会自动点击
  - key 1「①点击[签到]」改为 key 1501，并写上 `actionMaximum: 1`。仍是点 `vid="btnCheckIn"` 里可见的「签到」，排除可见的 `vid="tvTipNum"` 且文本为「--」。`actionDelay: 500` 未改。快照仍是 [22634962](https://i.gkd.li/i/22634962)、[33878350](https://i.gkd.li/i/33878350)，排除快照仍是 [23211622](https://i.gkd.li/i/23211622)
  - key 2「②点击[领福利]」改为 key 1502。`preKeys` 从 `[1]` 改为 `[1501, 1502]`，点过自己之后还能再匹配自己。新增 `actionMaximum: 2`。选择器未改，仍是可点击的 `vid="btnCheckIn"` 或 `vid="newBtnCheckIn"`。快照仍是 [23210761](https://i.gkd.li/i/23210761)、[33876754](https://i.gkd.li/i/33876754)
- 起点读书「功能类-自动[投推荐票]给《观山！》」（仍为 7 条，序号仍是 53）。说明、`enable: false`、`fastQuery`、`order: 3`、`matchDelay: 5000`、`actionMaximum: 1`、`resetMatch: "app"` 和活动页都没变。七条的选择器、快照、排除快照、`preKeys` 和 key 21 的返回动作都没变。新增两处关联字段。组本身 `enable: false`，功能类默认也是关闭的，不会自动点击，key 21 的返回键也不会自动按
  - 组上新增 `scopeKeys: [15]`。GKD 用它把另一个组的规则纳进本组，好让 `actionCdKey` 引用那边的规则 key。少年阿鲲源文件里序号 15 就是上面的签到组。合并只重排组序号，不改写 `scopeKeys`。订阅里序号 15 是另一组「功能类-自动签到」（没有 `enable: false`，功能类默认关闭），它的规则 key 是 0 和一条没写 key 的规则，没有 1502。签到组在订阅里是序号 51
  - key 10「①点击指定书名的[更多]」新增 `actionCdKey: 1502`，打算和签到组的「②点击[领福利]」共用冷却。本组自己的规则 key 是 10、20、21、30、31、40、41，没有 1502；`scopeKeys` 又指向序号 15 而不是 51，所以这条在订阅里对不上「②点击[领福利]」。选择器未改，仍是书名为「观山！」时点 `vid="ivMore"`。快照仍是 [31840578](https://i.gkd.li/i/31840578)、[31865741](https://i.gkd.li/i/31865741)、[31865742](https://i.gkd.li/i/31865742)、[33532939](https://i.gkd.li/i/33532939)，排除快照仍是 [31840584](https://i.gkd.li/i/31840584)、[22634962](https://i.gkd.li/i/22634962)、[33534248](https://i.gkd.li/i/33534248)、[33630474](https://i.gkd.li/i/33630474)

起点读书其余 52 个组的序号和选择器未改，仍是 54 组。这两组更高层没有同名组，合并结果与少年阿鲲 v131 这两组一致，只是组序号按合并排成 51 和 53。

被更高层同名组挡住、未进入合并结果：

- 大麦（`cn.damai`）「开屏广告」：Lin-arm 只改了说明，由「该规则需要在高级设置中开启[启用优化]才能生效」改为「⚠️该规则需在工作模式中开启[触摸优化],点击才能生效」。选择器仍是 `[vid="homepage_advert_pb"]`，动作仍是 `clickCenter`，仍有 `forcedTime: 8000`。快照仍是 [14585402](https://i.gkd.li/i/14585402)，示例仍是 [6680a0b8](https://m.gkd.li/57941037/6680a0b8-0796-4165-88fc-1f16cd6c67dd)。AIsouler 底座有同名组（序号 0）：说明仍是前一句，带 `priorityTime: 10000`，没有 `forcedTime`，选择器相同。同名组以底座为准，合并结果与 v31 相同
- 淘宝（`com.taobao.taobao`）「全屏广告-弹窗广告」：Lin-arm 在原有 key 0–5 之外新增 key 6。`fastQuery`，活动页 `com.taobao.tao.welcome.Welcome`，点 `vid="poplayer_inner_view"` 里宽小于 150、可见的 jpg 图（`@Image[text*=".jpg"][width<150][visibleToUser=true] < [childCount=1][height<150] - [height>500] <<n [vid="poplayer_inner_view"]`）。快照 [35306359](https://i.gkd.li/i/35306359)。没有示例链接。AIsouler 底座有同名组（序号 1，5 条，key 0–4），合并结果仍是底座那一版，与 v31 相同。Lin-arm v643 多出来的 key 5 本来就没进来，这次的 key 6 也没有写入

没有新的组被守卫丢掉。误触守卫挡住的组（合计 2155 组，与 v31 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源的版本都没变，丢掉的组与 v31 相同。

净变化：应用 +1，规则组 +2，规则 +4。全局组仍为 16。文件比 v31 大了 1,329 字节（比 v30 大 8,770 字节，其中 v31 的指纹排除占 7,441 字节）。

## [31] - 2026-11-26

### 内容

对照 v30（1118 应用 / 5122 规则组 / 7959 规则 / 16 全局组，2,879,618 字节），本版仍是 1118 应用 / 5122 规则组 / 7959 规则 / 16 全局组，订阅文件 2,887,059 字节。这不是一日上游合并。只修铁路 12306 指纹登录框被自动关掉。没有新增默认开启的组。开屏广告默认仍是开启的，其余分类默认仍是关闭的。

铁路 12306 国内包是 `com.MobileTicket`，国际包是 `com.chinarailway.globalticketing`。国内包应用规则里，默认会点的只有「开屏广告」，目标是 `vid="tv_main_splash_skip"` 或 `vid="tv_skip"`。横幅那条点 `vid="iv_tip_close"` 且 `desc` 以「关闭」开头，属于局部广告，默认不执行。没有一条应用规则去点指纹框上的「取消」。

会点「取消」的是三条默认开启的全局组。国内包没有名称以「通知提示」或「更新提示」开头的应用组，`disableIfAppGroupMatch` 关不掉它们：

- 「通知提示-全局关闭应用的通知提示」（Mrlc）。没有 `matchTime`，应用开着就会看。同一窗口里只要还有「广告 / 立即 / 开启 / 定位 / 免费」或 `id` 以 `image` 结尾，就会点 `text="取消"`（`top>200`）或「关闭」。12306 首页很容易满足前半句。系统指纹框文案是「请验证已有手机指纹」，里面没有「登录」，原有的 `text*="登录"` 排除挡不住。这是最可能的那条
- 「更新提示-全局」（底座 / Lin-arm）。画面上同时有「更新 / 升级 / 体验 / 新版」和较短的「确定 / 确认 / 查看 / 更新」时，点 `text^="取消"`
- 「更新提示-全局关闭应用的更新弹窗」（Mrlc）。画面上有「更新 / 体验 / 升级 / 新版」时，点 `text^="取消"`（`top>360`）

自有层 `globalExclude` 给这三条，以及用户若打开对应分类才会执行的「通知提示」「更新提示」「评价提示」「权限提示」「定位提示」「局部广告」「青少年模式」，每条规则追加一条 `excludeMatches`：可见文字或描述里有「指纹」「面容」或「生物识别」时，整条不点。点击选择器没有改。开屏三条全局组、`vid="ad_close"` 那条、12306 自己的开屏和横幅都没动。

没有这次指纹框的快照。若某一版对话框只写「请验证身份」、完全不出现上述三个词，这三条全局组仍可能去点「取消」。常见的「请验证已有手机指纹」「指纹登录」已经盖住。画面上如果正显示着含「指纹」的正文，这几条关闭弹窗的规则会先停一下，开屏跳过不受影响。

## [30] - 2026-11-25

### 内容

对照 v29（1117 应用 / 5119 规则组 / 7955 规则 / 16 全局组，2,878,330 字节），本版为 1118 应用 / 5122 规则组 / 7959 规则 / 16 全局组，订阅文件约 2.8 MB（2,879,618 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v642 → v643（chore: v643，2026-11-24T04:00:01Z，commit 204145ba）。v29 拉取时这份 dist 仍是 v642，文件 1,394,060 字节。本次 v643 dist 为 1,395,258 字节，与 v642 逐字节不同。对照两版 dist，只动了四个应用，四处都进入合并结果。v642 之后、已打进 v643 dist 的提交：fix 红果免费短剧「权限提示-通知权限」（2026-11-23T03:03:06Z，3e4c7dee，#494）、feat JavDB「更新提示」（2026-11-23T07:27:49Z，a40859d7，#495）、feat Luna「功能类-自动确认下载」（2026-11-23T07:34:16Z，67d50028，#496，新应用 `com.mt.luna`）、feat 豆包「全屏广告」（2026-11-23T07:49:13Z，5868e872）。上游 dist 变更记录与这次对照一致：新增 Luna、JavDB「更新提示」、豆包「全屏广告」，修订红果「权限提示-通知权限」。

其余十四个来源的版本与 v29 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v130、言木七 v54、AIsouler 自用续订 v124、Ling v16、GK-Lemon-D v59、火山虾 v78、YaChengMu v155。这十四个来源自 2026-11-23 起没有新的 dist 提交。少年阿鲲 2026-11-23T10:50:20Z 的 v130 已在 v29 并入。

v643 打版之后，Lin-arm 主分支上的 `dist/gkd.json5` 仍与这次 chore 产物逐字节相同，版本号仍是 643。下面四个提交只改了源码，还没有打进已发布 dist，没有进入合并结果：

- perf 大麦（`cn.damai`）「开屏广告」（2026-11-24T04:12:25Z，aa10e7f3，Relates to #489）。只改说明：由「该规则需要在高级设置中开启[启用优化]才能生效」改为「⚠️该规则需在工作模式中开启[触摸优化],点击才能生效」，用来适配 GKD 1.13.2。已发布 dist 里仍是前一句
- fix 淘宝（`com.taobao.taobao`）「全屏广告-弹窗广告」（2026-11-24T11:18:25Z，d00e4b86，#497）。源码新增 key 6：`fastQuery`，活动页 `com.taobao.tao.welcome.Welcome`，点 `vid="poplayer_inner_view"` 里宽小于 150、可见的 jpg 图。快照 [35306359](https://i.gkd.li/i/35306359)。已发布 dist 这组仍是 6 条（key 0–5），没有 key 6
- feat (小米)应用包管理组件（`com.miui.packageinstaller`）「功能类-关闭[未验证应用]提示」（2026-11-24T13:03:54Z，de292071，#498）。源码新增 key 20，说明是「点击[仍然安装]」，`fastQuery`，活动页 `com.miui.packageInstaller.NewInstallerPrepareActivity`。出现「未验证应用提醒」以及以「该应用未通过」开头的文字时点「仍然安装」。快照 [35331944](https://i.gkd.li/i/35331944)，示例 [8838fcbd](https://e.gkd.li/8838fcbd-1967-481b-9a1f-7bf3f8264c74)。已发布 dist 没有这组
- feat 番茄小说「权限提示-通知权限」（2026-11-24T13:26:13Z，7014842c）。提交说明末尾多了一个引号。这是新文件，应用包名是 `com.dragon.read.oversea.gp`，源码里的应用名是「番茄小说」。已发布 dist 没有 `com.dragon.read.oversea.gp`

Lin-arm v643 实际并入：

- Luna（`com.mt.luna`）新增应用，1 组（1 条）「功能类-自动确认下载」（序号 1）。说明是「弹窗, 点击[下载]」。各源里只有 Lin-arm 有这个应用，整份并入，序号就是上游的 key 1。活动页 `.activity.MainActivity`。点「下载」的可点击父节点，这个父节点前面还有可见的「下载文件」（`[text="下载"] < @[clickable=true] -n [visibleToUser=true][text="下载文件"]`）。快照 [35264146](https://i.gkd.li/i/35264146)，示例 [85733b49](https://e.gkd.li/85733b49-2631-4771-a112-5a7e53d736bb)。组没有 `enable: false`，功能类默认关闭，不会自动点击。打开该分类后，这条点的是「下载」
- 豆包（`com.larus.nova`）新增「全屏广告」（1 条，序号 2）。上游这组没有说明。规则上 `fastQuery`，活动页 `com.larus.home.impl.MainActivity`。出现包含「去体验」的文字时，点它前面可点击的 `vid="close_btn"`（`[text*="去体验"] -n [vid="close_btn"][clickable=true]`）。快照 [35264582](https://i.gkd.li/i/35264582)，示例 [ea9d7744](https://e.gkd.li/ea9d7744-425d-416d-913d-28e32e89c189)。组没有 `enable: false`，全屏广告默认关闭，不会自动点击。原有「功能类-自动创建新对话」（序号 1，3 条）未改。豆包现为 2 组。底座没有这个应用，两组都来自 Lin-arm，序号与上游一致
- JavDB（`xxx.pornhub.fuck`）新增「更新提示」（1 条，序号 2）。说明是「点击[下次提醒]」。`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"`，规则上没有 `fastQuery`。活动页只有 `.MainActivity`。出现可见、且 desc 含「更新」或「新版本」的节点时，点可点击的 desc「下次提醒」。快照 [35263945](https://i.gkd.li/i/35263945)。没有示例链接。底座这应用只有「通知提示-公告弹窗」，没有同名的「更新提示」，所以新组补了进来，序号按已有组往后排，正好也是 2。组没有 `enable: false`，更新提示默认关闭，不会自动点击。甘霖的「局部广告-公告弹窗」（写了 `enable: false`）只改了序号，由 2 改为 3，选择器未改。JavDB 现为 3 组
- 红果免费短剧（`com.phoenix.read`）「权限提示-通知权限」（仍为序号 2）由 1 条改为 2 条。说明由「点击[取消]」改为「点击[取消/暂不开启]」。组上仍是 `matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"`，并新增 `actionMaximumKey: 0`。组上的这些字段会落到没有单独写过的规则上：`actionMaximumKey` 表示和 key 为 0 的那条共用次数，任意一条点过之后两条一起休眠，重新进入应用才再计。组没有 `enable: false`，权限提示默认关闭，不会自动点击。这组 v29 已由 Lin-arm 进入，更高层没有同名组，所以修订写进了合并结果，合并结果与 Lin-arm v643 这组一致
  - key 0：选择器未改。出现包含「开启」、并且包含「提醒」或「通知」的文字时，点「取消」。规则上 `fastQuery`。不限活动页。快照仍是 [33926663](https://i.gkd.li/i/33926663)。v29 这条没有写 key，现在显式是 0。没有示例链接
  - key 1：新增。活动页 `com.dragon.read.pages.main.MainFragmentActivity`。点「暂不开启」的可点击父节点，这个父节点前面有可见、且包含「提醒」或「通知」的文字（`[text="暂不开启"] < @[clickable=true] -n [visibleToUser=true][text*="提醒" || text*="通知"]`）。这条没有 `fastQuery`。快照 [35252162](https://i.gkd.li/i/35252162)。没有示例链接。点的是「暂不开启」

红果其余三组的序号和选择器未改：Lin-arm 的「功能类-[上滑]继续看短剧」（序号 1，2 条），甘霖的「局部广告-阅读-底部卡片广告」（序号 3，2 条，写了 `enable: false`）和「全屏广告-阅读-视频广告」（序号 4，1 条，写了 `enable: false`）。

被更高层同名组挡住、未进入合并结果：

- JavDB「通知提示-公告弹窗」：Lin-arm v643 这组与 v642 相同，活动页仍是 `.MainActivity` 和 `.AppActivity`，选择器仍点公告旁可点击、可见的「知道了」，快照仍是 [14559882](https://i.gkd.li/i/14559882)、[35229398](https://i.gkd.li/i/35229398)。AIsouler 底座有同名组，合并结果仍是底座那一版（序号 1），与 v29 相同。这是 v28 就已经挡住的组，本版没有新的同名组被挡住
- 红果免费短剧「权限提示-通知权限」：YaChengMu 仍是 1 条旧选择器，组名与 Lin-arm 相同。该源只补缺口，同名组以先到的 Lin-arm 为准，这份旧选择器继续不写入。YaChengMu 版本仍是 v155，与 v29 相同

误触守卫挡住的组（合计 2155 组，与 v29 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源的版本都没变，丢掉的组与 v29 相同。

净变化：应用 +1，规则组 +3，规则 +4。全局组仍为 16。文件大了 1,288 字节。

## [29] - 2026-11-24

### 内容

对照 v28（1117 应用 / 5119 规则组 / 7955 规则 / 16 全局组，2,878,068 字节），本版为 1117 应用 / 5119 规则组 / 7955 规则 / 16 全局组，订阅文件约 2.8 MB（2,878,330 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组。合并结果里只有微信的两个组有变化，应用数、规则组数、规则条数都没变。

版本有变化的来源：

- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v129 → v130（chore: 🐔v130，2026-11-23T10:50:20Z）。对照 v129 dist 与 v130 dist，规则只动了微信的两组，都进入合并结果。v129 之后、已打进 v130 dist 的提交：fix 微信「🧩小程序-看完30s广告-x掉」（2026-11-23T05:08:12Z）、fix 微信「分段广告-视频号评论区内广告」（2026-11-23T07:20:03Z）。这两组只在少年阿鲲里有，更高层没有同名组，合并结果与该源 dist 一致（只是序号按合并重排，源里分别是 3 和 45，订阅里仍是 93 和 99）。

其余十四个来源的版本与 v28 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、言木七 v54、AIsouler 自用续订 v124、Ling v16、GK-Lemon-D v59、火山虾 v78、YaChengMu v155、[Lin-arm](https://github.com/Lin-arm/GKD_subscription) v642。本次拉取的 Lin-arm dist 与 2026-11-22T23:42:08Z 的 `chore: v642` 产物逐字节相同。v642 之后的四个提交（fix 红果免费短剧「权限提示-通知权限」、feat JavDB「更新提示」、feat Luna「功能类-自动确认下载」、feat 豆包「全屏广告」）还没有打进已发布 dist，没有进入合并结果。

少年阿鲲 v130 实际并入：

- 微信（`com.tencent.mm`）「分段广告-视频号评论区内广告」（仍为 8 条，序号仍是 99）。说明仍是「⚠️有概率误触」。组上 `fastQuery`，活动页仍是 `.plugin.finder.ui.FinderShareFeedRelUI` 和 `.plugin.finder.ui.FinderHomeAffinityUI`。组没有 `enable: false`，分段广告默认关闭，不会自动点击，key 101 的返回键也不会自动按。八条都还在，改的是名称、点击目标约束和触发顺序。后面从 `-n ImageView[desc="头像"]` 开始的链路没变：A 系列（key 1、25、50）的祖先仍是 `FrameLayout[index<parent.childCount.minus(1)]`，B 系列（key 2、26、51）的祖先仍是 `FrameLayout[index=parent.childCount.minus(1)]`，评论标题仍是 `TextView[text^="评论"][left<200]`。
  - key 1「①点击[广告](上面的)」改名为「①点击[广告]A」。点击目标去掉 `index=parent.childCount.minus(2)`，`top>getPrev(4).bottom` 放宽为 `top>getPrev(4).bottom.minus(30)`，并加上 `right>getPrev(4).right.minus(100)`。快照仍有 [24834498](https://i.gkd.li/i/24834498)、[24834499](https://i.gkd.li/i/24834499)，新增 [35262190](https://i.gkd.li/i/35262190)、[35263402](https://i.gkd.li/i/35263402)。排除快照仍有 [24835207](https://i.gkd.li/i/24835207)，新增 [35262964](https://i.gkd.li/i/35262964)
  - key 2「①点击[广告](下面的)」改名为「①点击[广告]B」。同样去掉 `index=parent.childCount.minus(2)`，并加上 `right>getPrev(4).right.minus(100)`，没有 top 限制。原先唯一的快照 [24834498](https://i.gkd.li/i/24834498) 从这条拿掉，仍挂在 key 1 上。这条现在不带快照
  - key 25「②点击下方的[关闭该广告]的坐标」改名为「②坐标点击[关闭该广告]A」。选择器与 key 1 相同。`preKeys` 从 `[1, 2]` 改为 `[1]`，只跟在 A 之后。坐标未改：`left: width * -0.7469`，`top: width * 2.4259`。快照仍有 [24834568](https://i.gkd.li/i/24834568)，新增 [35262192](https://i.gkd.li/i/35262192)
  - key 26「②点击上方的[关闭该广告]的坐标」改名为「②坐标点击[关闭该广告]B」。选择器与 key 2 相同。`preKeys` 从 `[1, 2]` 改为 `[2]`。坐标未改：`left: width * -0.7469`，`top: width * -1.2901`。快照仍是 [25476021](https://i.gkd.li/i/25476021)、[24835410](https://i.gkd.li/i/24835410)
  - key 50「③点击下方[直接关闭]的坐标」改名为「③坐标点击[直接关闭]A」。选择器与 key 1 相同。`preKeys` 从 `[25, 26]` 改为 `[25]`。坐标未改：`left: width * 0.1296`，`top: width * 1.1728`。快照仍有 [24834571](https://i.gkd.li/i/24834571)，新增 [35262195](https://i.gkd.li/i/35262195)
  - key 51「③点击上方的[直接关闭]的坐标」改名为「③坐标点击[直接关闭]B」。选择器与 key 2 相同。`preKeys` 从 `[25, 26]` 改为 `[26]`。坐标未改：`left: width * 0.1296`，`top: width * -2.5247`。快照仍是 [25476022](https://i.gkd.li/i/25476022)
  - key 100「④误触-返回评论区」、key 101「④误触输入框-返回键」选择器、活动页和动作都没变。`preKeys` 从 `[1, 2, 25, 26, 50, 51]` 改为 `[25, 26, 50, 51]`：点过广告本身不再接着跑这两条，只有坐标点过关闭菜单之后才跑。key 100 仍是三条 `anyMatches`（返回按钮、半屏页返回、`desc="返回"`），活动页仍是 `.plugin.webview.ui.tools.MMWebViewUI`、`.plugin.sns.ad.landingpage.ui.activity.HalfScreenVangoghPageUI`、`.ui.halfscreen.HalfScreenTransparentActivity`，快照仍是 [24836217](https://i.gkd.li/i/24836217)、[24834641](https://i.gkd.li/i/24834641)、[24836811](https://i.gkd.li/i/24836811)、[25476791](https://i.gkd.li/i/25476791)、[25477084](https://i.gkd.li/i/25477084)。key 101 仍是 `action: back`，匹配 `desc="表情"` 旁的评论区，快照仍是 [24835207](https://i.gkd.li/i/24835207)。这组没有示例链接
- 微信「🧩小程序-看完30s广告-x掉」（仍为 5 条，序号仍是 93）。说明由「①已完成 ②已获得」改为「(⚠️偶尔失效,gkd捉不到广告节点) ①已完成 ②已获得」。组上 `fastQuery`、`forcedTime: 60000` 未改。组没有 `enable: false`，名称也不落到默认关闭的分类，改过的两条仍会自动执行。第 1 条「①已完成-x掉」、第 2 条「②已获得奖励-x掉」、第 4 条「④直播-已获得奖励-x掉」未改
  - 第 3 条「③已获得奖励-关闭」：点「关闭」的路径由 `<<3` 改为先上一层可见节点、再两层（`@[text="关闭"] < [visibleToUser=true] <2 [index=parent.childCount.minus(1)] - FrameLayout >3 [text="已获得奖励"]`）。最后一层仍是父节点的最后一个子节点，旁边仍是「已获得奖励」。活动页在 `.plugin.appbrand.ui.AppBrandUI`、`.plugin.appbrand.ui.AppBrandPluginUI` 之外加上 `.plugin.appbrand.ipc.AppBrandProcessProxyUI`。快照仍有 [24545151](https://i.gkd.li/i/24545151)、[30338756](https://i.gkd.li/i/30338756)、[30339852](https://i.gkd.li/i/30339852)，新增 [35255348](https://i.gkd.li/i/35255348)。示例仍是 [1ec650be](https://e.gkd.li/1ec650be-9fa6-413f-88a5-f8118e836fa6)。这条会自动点「关闭」
  - 第 5 条「⑤已获得奖励-按[返回键]」：选择器未改，仍是 `@[text="已获得奖励"] < [childCount=1] + [visibleToUser=true] >2 [text="广告"]`，动作仍是返回（`action: back`，`actionDelay: 500`）。活动页同样加上 `.plugin.appbrand.ipc.AppBrandProcessProxyUI`。新增 `actionCdKey: 3`，与第 3 条共用冷却；组上没有另写 `actionCd`。快照仍是 [30339852](https://i.gkd.li/i/30339852)、[30341286](https://i.gkd.li/i/30341286)、[30388374](https://i.gkd.li/i/30388374)。这条会自动按返回键

微信其余 88 个组的序号和选择器未改，仍是 90 组。

没有新的同名组被挡住，也没有新的组被守卫丢掉。误触守卫挡住的组（合计 2155 组，与 v28 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源的版本都没变，丢掉的组与 v28 相同。

净变化：应用数不变，规则组数不变，规则条数不变。全局组仍为 16。文件大了 262 字节。

## [28] - 2026-11-23

### 内容

对照 v27（1116 应用 / 5117 规则组 / 7953 规则 / 16 全局组，2,877,103 字节），本版为 1117 应用 / 5119 规则组 / 7955 规则 / 16 全局组，订阅文件约 2.8 MB（2,878,068 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v641 → v642（chore: v642，2026-11-22T23:42:08Z）。v641 之后、已打进 v642 dist 的提交：perf 系统升级(VIVO)、UU远程（2026-11-22T05:22:17Z）、feat 快对AI「局部广告-讲解视频浮窗」（2026-11-22T10:14:13Z，#491）、fix JavDB「通知提示-公告弹窗」（2026-11-22T10:24:35Z，#492）、feat 小米服务框架「权限提示-b站申请通知权限」（2026-11-22T12:51:56Z）。对照 v641 与 v642 的 dist，规则只动了这四个应用。JavDB 被底座同名组挡住；系统升级、UU远程、快对AI、小米服务框架进入合并结果。perf 提交说明里的「其他...」没有再改别的应用。
- [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) v56 → v59（Match current Android accessibility settings layout，2026-11-22T09:47:59Z）。该源只补缺口、不并入全局组。父提交的 dist 仍是 version 56，这次 dist 为 version 59，规则只改了系统设置一组，被守卫丢掉，没有进入合并结果。

其余十三个来源的版本与 v27 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v129、言木七 v54、AIsouler 自用续订 v124、Ling v16、火山虾 v78、YaChengMu v155。少年阿鲲 2026-11-22T10:31:41Z 的「优化选择器库」没有改主 dist，文件与 v27 拉取时逐字节相同。Ling 在同一天有订阅 URL、依赖和文档提交，dist 里的 apps、globalGroups、categories 与 v27 拉取时相同，只有 author 从「Ling」改成了「⚠警告」，规则内容未变，没有新组进入。

Lin-arm v642 实际并入：

- 系统升级(VIVO)（`com.bbk.updater`）「通知提示-系统更新提示」改名为「更新提示」（仍为 1 条，序号仍是 1）。说明改为「按[返回键]」。选择器、动作和快照都没变：`fastQuery`，活动页 `com.bbk.launcher2.Launcher`，出现「下载并安装」时匹配旁边可点击、可见的「稍后提醒」，动作为返回（`action: back`）。快照 [26644663](https://i.gkd.li/i/26644663)，示例 [bdd7cc82](https://e.gkd.li/bdd7cc82-a138-4f0b-b865-0be3168a319e)。这个应用在各源里只有 Lin-arm 这一组，合并按当次 dist 重算，旧名不再有来源提供，订阅里只留下新名，新旧组不并存。组没有 `enable: false`。组名归到「更新提示」，该分类默认关闭，不会自动按返回键。v27 它归在「通知提示」，那个分类默认也是关闭的
- UU远程（`com.netease.uuremote`）「通知提示-更新提示」改名为「更新提示」（仍为 1 条，序号仍是 2）。说明改为「点击[暂不更新]」。选择器、活动页、快照和示例都与 v27 相同：`matchTime: 20000`、`actionMaximum: 1`、`resetMatch: "app"`，规则上 `fastQuery`。活动页 `com.remote.app.ui.activity.ComposeMainActivity`，出现以「更新」结尾的文字时，点以「不更新」结尾的可点击 View。快照 [35130030](https://i.gkd.li/i/35130030)，示例 [427b504d](https://e.gkd.li/427b504d-30f3-4e18-b525-5be6a6787801)。这组 v27 由 Lin-arm 并入，更高层没有同名组。改名后源里不再提供旧名，订阅里只留下「更新提示」，新旧组不并存。原有「权限提示-通知提示」（序号 1）仍是 AIsouler 底座的版本，未改。组没有 `enable: false`，归到「更新提示」，该分类默认关闭，不会自动点击
- 快对AI（`com.kuaiduizuoye.scan`）新增「局部广告-讲解视频浮窗」（1 条，序号 2）。说明是「x掉」。这个应用先由 Lin-arm 整份并入，Lin-arm 自带的序号会保留，所以新组用的就是上游的 key 2。活动页是拍搜页 `.activity.manyquestionsearch.activity.PicManySearchActivity`。点可见且宽小于 126 的 TextView；它前一个兄弟节点有 3 个子节点，其中是一个 TextView，后面紧跟文本长度大于 50、宽小于 143 且高大于 82 的 Image。快照 [35228963](https://i.gkd.li/i/35228963)，示例 [e37a46fe](https://e.gkd.li/e37a46fe-9464-405e-9a93-608a865a519f)。组没有 `enable: false`，局部广告默认关闭，不会自动点击。原先排在后面的三组只改了序号、选择器未改：甘霖的「全屏广告-首页广告弹窗」（写了 `enable: false`）由 2 改为 3，Adpro 的「未分类-首页广告弹窗」（写了 `enable: false`）由 3 改为 4，九千院的「开屏广告」（2 条，没有 `enable: false`）由 4 改为 5。开屏这组 v27 就在，开屏分类默认开启，不是本版新增的默认开启组。Lin-arm 原有的「分段广告」（序号 1）未改。快对AI 现为 5 组
- 小米服务框架（`com.xiaomi.xmsf`）新增应用，1 组（1 条）「权限提示-b站申请通知权限」（序号 1）。说明是「(⚠️仅限哔哩哔哩app) 点击[拒绝]」。`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"`，规则上 `fastQuery`。活动页 `com.xiaomi.xms.subscribe_remind.dialog.SubscribeDialogActivity`，出现包含「哔哩哔哩」的文字、后面跟着包含「通知」的文字时，点可点击的「拒绝」。快照 [35232368](https://i.gkd.li/i/35232368)，示例 [d8b8754f](https://e.gkd.li/d8b8754f-d66f-483a-b424-75951d782623)。组没有 `enable: false`，权限提示默认关闭，不会自动点击

被更高层同名组挡住、未进入合并结果：

- JavDB（`xxx.pornhub.fuck`）「通知提示-公告弹窗」：Lin-arm 把活动页从 `.MainActivity` 扩成 `.MainActivity` 和 `.AppActivity`，选择器从 `@Button[desc="知道了"][visibleToUser=true] <3 View < View < View < View < FrameLayout < [id="android:id/content"]` 改为 `View[desc="公告"] +n @Button[desc="知道了"][clickable=true][visibleToUser=true] <<n [id="android:id/content"]`，快照在 [14559882](https://i.gkd.li/i/14559882) 之外加上 [35229398](https://i.gkd.li/i/35229398)，示例改为 [a3782695](https://e.gkd.li/a3782695-5b94-4588-9c82-24989d4e04bd)。AIsouler 底座有同名组，而且与 Lin-arm v641 这组完全一致（说明「点击[知道了]」，`fastQuery`、`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"`，活动页仍只有 `.MainActivity`，快照 [14559882](https://i.gkd.li/i/14559882)，示例 [ae1792dd](https://m.gkd.li/57941037/ae1792dd-210b-4ac2-bfce-c2081ed03498)）。同名组以底座为准（序号 1）。合并结果与 v27 相同。甘霖的「局部广告-公告弹窗」（序号 2，写了 `enable: false`）未改

GK-Lemon-D v59 被守卫丢掉：

- 系统设置（`com.android.settings`）「功能类-快速开启无障碍」（5 条）相对 v56 只改了选择器，没有进入合并结果。选中「无障碍功能启动手势」、以及选中后返回这两条，CheckBox 和标题的相邻关系由 `+` 改为 `-`。开启服务、关掉快捷方式这两条，去掉 `Switch[desc^="使用“"] >2` 这段前缀，开关改为直接匹配 `Switch[id="android:id/switch_widget"]`。返回那条仍是 `action: back`。规则序号也重排了（返回由 3 改为 2，开启服务由 4 改为 3，关掉快捷方式由 2 改为 4）。组名仍是功能类，不含「关闭」或「弹窗」，组上仍写了 `enable: false`，活动页仍是 `.SubSettings`，仍然没有快照。守卫先按功能类丢掉整组，返回那条没有单独计成手势。这个应用在合并结果里仍是 v27 的 6 个组，没有「功能类-快速开启无障碍」

误触守卫挡住的组（合计 2155 组，与 v27 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源里只有 GK-Lemon-D 升了版本；系统设置那组仍算在功能类里，丢掉的组数和原因都与 v27 相同。

净变化：应用 +1，规则组 +2，规则 +2。全局组仍为 16。文件大了 965 字节。

## [27] - 2026-11-22

### 内容

对照 v26（1115 应用 / 5114 规则组 / 7948 规则 / 16 全局组，2,874,827 字节），本版为 1116 应用 / 5117 规则组 / 7953 规则 / 16 全局组，订阅文件约 2.8 MB（2,877,103 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版没有新增默认开启的组。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v640 → v641（chore: v641，2026-11-21T23:30:07Z）。v640 之后、已打进 v641 dist 的提交：feat vivo服务「功能类-自动关闭温度过低提示」（作者时间 2026-11-20T07:05:34Z，合入 2026-11-21T12:49:55Z）、feat UU远程「通知提示-更新提示」（2026-11-21T12:49:55Z）、fix 快手极速版「全屏广告」（2026-11-21T14:44:15Z）、fix 番茄免费小说「功能类-自动[展开更多]评论」（2026-11-21T14:50:25Z，Relates to #490）。四处都进入合并结果。快手是改名后的新组，底座里的旧名组仍在。

其余十四个来源的版本与 v26 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v129、言木七 v54、AIsouler 自用续订 v124、Ling v16、GK-Lemon-D v56、火山虾 v78、YaChengMu v155。

Lin-arm v641 实际并入：

- VIVO服务（`com.vivo.daemonService`；上游提交标题写的是 vivo服务）新增应用，1 组（1 条）「功能类-自动关闭温度过低提示」（序号 1）。说明是「温度过低... -> 点击确定」。`fastQuery`。出现以「温度过低」开头的标题时，从 `android:id/topPanel` 走到对话框底部，点最后一个只含一个按钮的 LinearLayout 里可点击的「确定」。快照 [35131038](https://i.gkd.li/i/35131038)，示例 [124e048b](https://e.gkd.li/124e048b-3ac5-4721-a357-b6bd2182c512)。组没有 `enable: false`，功能类默认关闭，不会自动点击
- UU远程（`com.netease.uuremote`）新增「通知提示-更新提示」（1 条，序号 2）：`matchTime: 20000`、`actionMaximum: 1`、`resetMatch: "app"`、`fastQuery`。活动页 `com.remote.app.ui.activity.ComposeMainActivity`，出现以「更新」结尾的文字时，点以「不更新」结尾的可点击 View。快照 [35130030](https://i.gkd.li/i/35130030)，示例 [427b504d](https://e.gkd.li/427b504d-30f3-4e18-b525-5be6a6787801)。组没有 `enable: false`，通知提示默认关闭，不会自动点击。原有「权限提示-通知提示」（序号 1）未改
- 快手极速版（`com.kuaishou.nebula`）新增「全屏广告」（3 条，序号 7）。上游把 v640 的「全屏广告-红包弹窗」改名为「全屏广告」，并新增 key 2。合并粒度是同应用同名组：底座的「全屏广告-红包弹窗」对不上这个新名字，所以新组整组补入，旧名组留在原地。组上 `fastQuery`，活动页是首页 `com.yxcorp.gifshow.HomeActivity` 和搜索页 `com.yxcorp.plugin.search.SearchActivity`。①点父节点的最后一个子节点，要求可点击且宽小于 128，旁边 1 到 2 位是含有「点击立得奖励」、以「邀请」开头或文本为「红包」的 ViewGroup，这些文字须可见。快照 [14879912](https://i.gkd.li/i/14879912)、[15061662](https://i.gkd.li/i/15061662)、[25200787](https://i.gkd.li/i/25200787)、[26675794](https://i.gkd.li/i/26675794)，排除快照 [26678562](https://i.gkd.li/i/26678562)，示例 [f7bbd1db](https://m.gkd.li/101449500/f7bbd1db-f519-4ff9-96cb-4cb5b2f483a2)。相对 v640 被挡住的同条，选择器末尾加上 `[visibleToUser=true]`。②点排在最前、宽高小于 107 的可点击 ImageView，旁边是以「红包」结尾、长度小于 10 的文字。快照 [26678562](https://i.gkd.li/i/26678562)、[28514398](https://i.gkd.li/i/28514398)。v640 这条的活动页只写了首页；收到组上之后，搜索页也会匹配。③新增 key 2：匹配「口令已复制」，点击位置在所在 ViewGroup 右缘外侧、略高于顶边（`left: width * 1.0557`，`top: height * -0.0569`）。快照 [35203973](https://i.gkd.li/i/35203973)，示例 [6030f5cb](https://e.gkd.li/6030f5cb-9d9d-4b0c-81f6-8b3912f90842)。组没有 `enable: false`，全屏广告默认关闭，不会自动点击。原先序号 7–59 的 53 个组改为 8–60，选择器未改。快手极速版现为 60 组
- 番茄免费小说（`com.dragon.read`）「功能类-自动[展开更多]评论」（仍为 1 条，序号 23）规则更新。这组 v26 已由 Lin-arm 进入，更高层没有同名组，所以仍以 Lin-arm 为准，补上的活动页和快照写进了合并结果。活动页在阅读页 `.reader.ui.ReaderActivity`、短剧页 `.pages.main.MainFragmentActivity` 之外，加上开屏页 `.ad.openingscreenad.OpeningScreenADActivity` 和短剧实现页 `.component.shortvideo.impl.ShortSeriesActivity`。选择器未改：先确认内容区足够高，再点以「展开」开头、以「回复」或「更多」结尾的文字的可点击父节点。快照新增 [35203330](https://i.gkd.li/i/35203330)、[35203316](https://i.gkd.li/i/35203316)；原快照 [35147917](https://i.gkd.li/i/35147917)、[35147919](https://i.gkd.li/i/35147919)、[35173217](https://i.gkd.li/i/35173217)，排除快照 [35165101](https://i.gkd.li/i/35165101)、[35173220](https://i.gkd.li/i/35173220)，示例 [e0c12712](https://e.gkd.li/e0c12712-4b1e-4b75-a9ec-d1a8042156f6)、[0d2d257a](https://e.gkd.li/0d2d257a-abda-4255-b971-faf06b565cb7) 仍在。组没有 `enable: false`，功能类默认关闭，不会自动点击。番茄免费小说其余组的序号和选择器未改

改名后旧组仍留在订阅里：

- 快手极速版「全屏广告-红包弹窗」（序号 3，1 条）仍是 AIsouler 底座的版本，与 v26 相同。只在首页 `com.yxcorp.gifshow.HomeActivity`，点可点击的 ImageView，旁边是「点击立得奖励」或以「邀请」开头的文字。快照 [14879912](https://i.gkd.li/i/14879912)、[15061662](https://i.gkd.li/i/15061662)、[25200787](https://i.gkd.li/i/25200787)，示例 [f7bbd1db](https://m.gkd.li/101449500/f7bbd1db-f519-4ff9-96cb-4cb5b2f483a2)。Lin-arm v640 的同名组是 2 条（就是上面①②的前身，当时还没有 `[visibleToUser=true]`，key 1 也只限首页），一直被这组挡住，没有进入 v26。v641 改名之后，Lin-arm 不再提供这个旧名，底座这 1 条继续留下。新组「全屏广告」另计。全屏广告默认关闭，两组都不会自动点击；打开该分类后，两组都会参与匹配红包弹窗

误触守卫挡住的组（合计 2155 组，与 v26 持平）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。五个守卫源的版本都没变，丢掉的组与 v26 相同。

净变化：应用 +1，规则组 +3，规则 +5。全局组仍为 16。文件大了 2,276 字节。

## [26] - 2026-11-21

### 内容

对照 v25（1114 应用 / 5110 规则组 / 7943 规则 / 16 全局组，2,872,875 字节），本版为 1115 应用 / 5114 规则组 / 7948 规则 / 16 全局组，订阅文件约 2.8 MB（2,874,827 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。本版新增两个默认开启的组：大连明珠卡、Blued极速版的「开屏广告」（都没有写 `enable: false`，开屏分类默认开启，会自动点击）。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v639 → v640（chore: v640，2026-11-21T00:04:18Z）。v639 之后、已打进 v640 dist 的提交：feat 快手极速版「权限提示-通讯录权限」（2026-11-20T01:33:54Z，v25 当时 dist 仍为 v639，这次进入）、feat 一淘「更新提示」（2026-11-20T03:30:46Z）、feat 大连明珠卡「开屏广告」（2026-11-20T03:41:46Z，#487）、feat Blued X「开屏广告」（2026-11-20T03:52:50Z，#488）、feat 番茄免费小说「功能类-自动[展开更多]评论」（2026-11-20T15:31:15Z，#490）、fix 拼多多「功能类-多多视频每日自动签到」（2026-11-20T16:54:35Z）、perf 番茄免费小说「功能类-自动[展开更多]评论」（2026-11-20T17:12:05Z，适配短剧评论区）。前六处里，拼多多签到被底座同名组挡住；其余五处进入合并结果，番茄那组是 feat 加 perf 之后的版本。
- [YaChengMu](https://github.com/YaChengMu/gkd_subscription_min) v154 → v155（feat: 更新订阅规则至 v155，2026-11-20T14:55:48Z）。该源只补缺口、不并入全局组。这次没有新内容进入合并结果。
- [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) v50 → v56（dist 与 version 文件均为 version 56）。v50 之后可见提交：Add quick accessibility setup rules（2026-11-20T03:06:50Z）、Refine accessibility shortcut setup（2026-11-20T03:17:07Z）。相对 v50 的订阅内容只多了系统设置一组，被守卫丢掉，没有进入合并结果。

其余十二个来源的版本与 v25 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v129、言木七 v54、AIsouler 自用续订 v124、Ling v16、火山虾 v78。

Lin-arm v640 实际并入：

- 大连明珠卡（`com.mzk.android`）新增应用，1 组（1 条）「开屏广告」（序号 1）：`fastQuery`、`matchTime: 10000`、`actionMaximum: 1`、`resetMatch: "app"`、`order: -10`，点可点击的 `vid="cll_splash_skip"`。快照 [35126804](https://i.gkd.li/i/35126804)。组没有 `enable: false`，开屏分类默认开启，这条会生效
- Blued极速版（`com.danlan.xiaolan`；上游应用名和提交标题写的是 Blued X，合并后应用名仍是底座的「Blued极速版」）新增「开屏广告」（2 条，序号 4）：`fastQuery`、`matchTime: 10000`、`actionMaximum: 1`、`actionMaximumKey: 0`、`resetMatch: "app"`、`order: -10`。①点长度小于 10、宽小于 500 且高小于 300 的「跳过」（这条没有快照）；②点「广告」旁宽高小于 156 的 ImageView，快照 [35126957](https://i.gkd.li/i/35126957)。组没有 `enable: false`，开屏分类默认开启，这两条会生效。原先序号 4–7 的 4 个组改为 5–8，选择器未改
- 番茄免费小说（`com.dragon.read`）新增「功能类-自动[展开更多]评论」（1 条，序号 23）。说明是「小说段评区/短剧评论区, 点击[展开更多/展开n条回复]」。`fastQuery`、`actionCd: 500`，活动页是阅读页 `.reader.ui.ReaderActivity` 和短剧页 `.pages.main.MainFragmentActivity`（短剧页是 perf 提交加上的）。先确认内容区足够高，再点以「展开」开头、以「回复」或「更多」结尾的文字的可点击父节点。快照 [35147917](https://i.gkd.li/i/35147917)、[35147919](https://i.gkd.li/i/35147919)、[35173217](https://i.gkd.li/i/35173217)，排除快照 [35165101](https://i.gkd.li/i/35165101)、[35173220](https://i.gkd.li/i/35173220)，示例 [e0c12712](https://e.gkd.li/e0c12712-4b1e-4b75-a9ec-d1a8042156f6)、[0d2d257a](https://e.gkd.li/0d2d257a-abda-4255-b971-faf06b565cb7)。组没有 `enable: false`，功能类默认关闭，不会自动点击。原先序号 23–42 的 20 个组改为 24–43，选择器未改
- 快手极速版（`com.kuaishou.nebula`）新增「权限提示-通讯录权限」（1 条，序号 11）。说明是「点击[以后再说]」。在 `com.yxcorp.gifshow.HomeActivity`，出现包含「通讯录」的文字时点「以后再说」。快照 [35119491](https://i.gkd.li/i/35119491)，示例 [3c25da6d](https://e.gkd.li/3c25da6d-bc0d-420d-9362-c8bb1edf322b)。组没有 `enable: false`，权限提示默认关闭，不会自动点击。原先序号 11–58 的 48 个组改为 12–59，选择器未改
- 一淘（`com.taobao.etao`）「更新提示」（仍为 1 条，序号 11）整组换成 Lin-arm 的版本。v25 这组是甘霖的：写了 `enable: false`，一条字符串选择器 `[text="更新提示"] <<2 * +2 * >2 [text="取消"]`，快照 [12684250](https://i.gkd.li/import/12684250)、[12727457](https://i.gkd.li/import/12727457)、[12684244](https://i.gkd.li/import/12684244)。Lin-arm 优先级更高，同名组以它为准。新组说明是「点击[取消]」（上游注明全局 10 秒时长不够，所以单独适配），`actionMaximum: 1`、`resetMatch: "app"` 仍在，活动页 `.maintab.MainTabActivity`，出现包含「更新」「新版本」或「升级」的文字时点「取消」。快照 [35125923](https://i.gkd.li/i/35125923)。新组没有写 `enable: false`；「更新提示」分类默认关闭，不会自动点击

被更高层同名组挡住、未进入合并结果：

- 拼多多（`com.xunmeng.pinduoduo`）「功能类-多多视频每日自动签到」：Lin-arm 把活动页从 `.ui.activity.HomeActivity` 扩成三条（再加上 `com.bbk.launcher2.Launcher` 和 `.ui.activity.MainFrameActivity`），两条选择器由 `>2` 放宽为 `>(1,2)`，规则名加上①②，第 1 条补快照 [35172532](https://i.gkd.li/i/35172532)。同名组仍以 AIsouler 底座为准（序号 9，2 条）：活动页是完整类名 `com.xunmeng.pinduoduo.ui.activity.HomeActivity`，选择器仍是 `>2`，没有新快照。合并结果与 v25 相同

YaChengMu v155 没有进入合并结果。和更高层现行内容相同、被同名组挡住的：快手极速版「权限提示-通讯录权限」（与本次 Lin-arm 并入的那组相同）、番茄免费小说「功能类-观看广告自动静音」、抖音「功能类-刷到推广视频时[上滑]」、淘宝「功能类-删除订单直接确认」「局部广告-横幅广告」「评价提示-商品评论区评价满意度」、拼多多「功能类-[上滑]继续看视频」「功能类-展开更多」「功能类-搜索页-长按词条直接删除」。抖音极速版两个「功能类-评论区-自动展开评论」组从该源删掉，v25 起合并结果里已经没有。拼多多「全屏广告-多多视频划到广告自动跳过」也从该源删掉，合并结果里仍是底座的 2 条版本（序号 10），与 v25 相同。

和底座不同、仍被同名组挡住的（合并结果都与 v25 相同，同名组仍是 AIsouler 底座）：

- 番茄免费小说「分段广告-阅读页面广告」（序号 5）：YaChengMu 跟进了 Lin-arm v639 的写法，其中一条排除「立即播放」（原来只排除「查看下载」），补快照 [35098348](https://i.gkd.li/i/35098348)。v25 已记下这条被底座挡住
- 支付宝（`com.eg.android.AlipayGphone`）「开屏广告-小程序开屏广告」（序号 24）：点「跳过」那条的层级由 `<(7,8)` 放宽为 `<(5+n)`，补快照 [34788907](https://i.gkd.li/i/34788907)
- 抖音（`com.ss.android.ugc.aweme`）「全屏广告」（序号 15）：第 1 条由一条 `matches` 改成两条 `anyMatches`（`+(1,2)` 放宽为 `+(1,2,5)`，并加上宽高受限的「不感兴趣」），补快照 [34876101](https://i.gkd.li/i/34876101)、[34942616](https://i.gkd.li/i/34942616)，示例 [f967dcd3](https://e.gkd.li/f967dcd3-2196-4095-b5f0-a2cae15bdf23)
- 微信（`com.tencent.mm`）「功能类-自动查看原图」（序号 9）：「查看」「原图」加上 `text!$="0K"`，第 2 条去掉活动页 `.ui.LauncherUI`，补排除快照 [34987211](https://i.gkd.li/i/34987211)。这是 Lin-arm 在 v637 就有、当时已被底座挡住的改动
- 拼多多「全屏广告-下单后出现的弹窗」（序号 12）：WebView 文本从「拼多多」放宽为「拼多多」或空文本，补快照 [34986289](https://i.gkd.li/i/34986289)。同样是 v637 已被底座挡住的改动
- QQ（`com.tencent.mobileqq`）「局部广告」（序号 1）：key 为 4 的那条规则加上 `actionDelay: 500`
- 哔哩哔哩（`tv.danmaku.bili`）「全屏广告-会员弹窗」（序号 12）：key 4 的选择器改成点「套餐」旁的可点击 View（`[vid="vip_panel"][height>500]`），补快照 [34776793](https://i.gkd.li/i/34776793)，排除快照 [34777480](https://i.gkd.li/i/34777480)，示例 [41a7f3ae](https://e.gkd.li/41a7f3ae-c01d-4f1e-a90a-5fefa4606393)；key 5 去掉 `fastQuery`
- 哔哩哔哩「分段广告-视频详情页下方推广」（序号 15）：课堂/纪录片那条补快照 [34722511](https://i.gkd.li/i/34722511)，并新增 key 51「②点击[不感兴趣]2」（快照 [34722513](https://i.gkd.li/i/34722513)），key 70 的 `preKeys` 加上 51
- 哔哩哔哩「分段广告-首页推荐视频卡片广告」（序号 10）：不感兴趣那条加上文案「不喜欢此商品」，补快照 [34849877](https://i.gkd.li/i/34849877)，规则名改为「②点击[不感兴趣/内容过多]等」；下一条命名为「③点击[xx内容过多]」

GK-Lemon-D v56 被守卫丢掉：

- 系统设置（`com.android.settings`）新增「功能类-快速开启无障碍」（5 条）。说明是「选中无障碍功能启动手势后返回，开启服务并确认授权，最后关闭快捷方式开关」。活动页 `.SubSettings`，组上写了 `enable: false`。五条依次是：允许开启无障碍服务、选中「无障碍功能启动手势」、选中后按返回（`action: back`）、快捷方式已开时打开服务开关、服务已开时关掉快捷方式。没有快照。组名是功能类且不含「关闭」或「弹窗」，守卫按功能类丢掉（返回那条也因此没有单独计成手势）。这个应用本来就有，这组没有写入

误触守卫挡住的组（合计 2155 组，v25 为 2153）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7），这两源与 v25 持平。GK-Lemon-D 11 组（名称命中拒绝词 6、功能类无「关闭/弹窗」2、选择器命中补充拒绝词 2、重复选择器 1），比 v25 多 1 组，多在功能类——系统设置「快速开启无障碍」。火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37），与 v25 持平。YaChengMu 388 组（重复选择器 234、功能类无「关闭/弹窗」115、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1），功能类比 v25 多 1：新出现的淘宝「删除订单直接确认」、拼多多「上滑继续看视频」「搜索页长按词条直接删除」三组按功能类丢掉（内容与已并入版本相同，即便过守卫也会被同名组挡住），同时不再计算已从该源删除的抖音极速版两个展开评论组，净增 1。

净变化：应用 +1，规则组 +4，规则 +5。全局组仍为 16。文件大了 1,952 字节。

## [25] - 2026-11-20

### 内容

对照 v24（1113 应用 / 5109 规则组 / 7942 规则 / 16 全局组），本版为 1114 应用 / 5110 规则组 / 7943 规则 / 16 全局组，订阅文件约 2.8 MB（2,872,875 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v638 → v639（chore: v639，2026-11-20 00:20:17Z）。v638 之后的内容提交：feat 拼多多「功能类-[上滑]继续看视频」（2026-11-19 02:56:47Z）、fix 拼多多「功能类-展开更多」（2026-11-19 03:23:11Z）、fix 快对 AI「分段广告」（2026-11-19 07:57:01Z）、feat 海岛奇兵「通知提示-未成年弹窗」（2026-11-19 09:43:10Z）、perf 抖音极速版移除自动展开评论的规则（2026-11-19 11:11:23Z）、fix 虎牙直播「局部广告-直播间悬浮广告」（2026-11-19 14:42:11Z，#484）、fix 番茄免费小说「分段广告-阅读页面广告」（2026-11-19 17:24:20Z，#485）。快手极速版「权限提示-通讯录权限」（2026-11-20 01:33:54Z）在 v639 打版之后，dist 仍为 v639，未进入本次合并。
- [AIsouler 自用续订](https://github.com/AIsouler/gkd-subscription) v123 → v124（feat: rules，2026-11-19 14:19:41Z；chore: v124，2026-11-19 14:21:11Z）。该源只补缺口、不并入全局组。
- [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) v49 → v50（netease music，2026-11-19 02:48:12Z）。

其余十二个来源的版本与 v24 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v129、言木七 v54、Ling v16、火山虾 v78、YaChengMu v154。

Lin-arm v639 实际并入：

- 海岛奇兵（`com.tencent.tmgp.supercell.boombeach`）新增应用，1 组（1 条）「通知提示-未成年弹窗」（序号 1）：活动页 `com.supercell.titan.tencent.GameAppTencentMidas`，点「未成年游戏教育」弹窗旁的小叉（宽高 <104 的 TextView），`actionMaximum: 1`、`resetMatch: "app"`。快照 [35075364](https://i.gkd.li/i/35075364)，示例 [beb30964](https://e.gkd.li/beb30964-2fbf-42a4-a325-8d6a4f209f65)。通知提示默认关闭，不会自动点击
- 拼多多（`com.xunmeng.pinduoduo`）新增「功能类-[上滑]继续看视频」（1 条，序号 23）：在 `HomeActivity` / `MainFrameActivity`，出现「上滑继续看视频」或「点击进入直播间」时从屏幕 70% 高度上滑到 30%（200ms），把广告/直播滑走。快照 [13791119](https://i.gkd.li/i/13791119)、[13446291](https://i.gkd.li/i/13446291)、[35063484](https://i.gkd.li/i/35063484)，示例 [136b0844](https://e.gkd.li/136b0844-1d93-4192-95c7-ad42129e86b9)。功能类默认关闭，不会自动上滑。同次提交把 Lin-arm 自带的「全屏广告-多多视频划到广告自动跳过」删了（改成上滑方案）；合并结果里这组仍是 AIsouler 底座的 2 条版本（序号 10），点「返回」刷新跳过广告，与 v24 相同
- 抖音极速版（`com.ss.android.ugc.aweme.lite`）删除「功能类-评论区-自动展开评论」和「功能类-评论区-自动展开评论_全部」（各 1 条）：上游 perf 提交移除自动展开评论的规则。两组都已不在合并结果里；抖音极速版现为 26 组，其余组未改（序号重排）
- 快对 AI（`com.kuaiduizuoye.scan`）「分段广告」（仍为 2 条，序号 1）：第 1 条选择器由 `>3` 改为 `>(2,3)`（点「关闭」），补快照 [35073276](https://i.gkd.li/i/35073276)
- 拼多多「功能类-展开更多」（仍为 4 条，序号由 24 改为 25）：第 1 条「通用[展开]_fastQ」的排除条件由「轻触照亮 / 相册」改为「相册 / 追剧」，排除快照增加 [35064077](https://i.gkd.li/i/35064077)、[35064076](https://i.gkd.li/i/35064076)（追剧）；原排除快照 [34986764](https://i.gkd.li/i/34986764) 仍在。功能类默认关闭，不会自动点击

被更高层同名组挡住、未进入合并结果：

- 番茄免费小说（`com.dragon.read`）「分段广告-阅读页面广告」：Lin-arm 给其中一条加排除「立即播放」（原来只排除「查看下载」），补快照 [35098348](https://i.gkd.li/i/35098348)。同名组仍以 AIsouler 底座的 4 条版本为准（序号 5），合并结果与 v24 相同
- 虎牙直播（`com.duowan.kiwi`）「局部广告-直播间悬浮广告」：Lin-arm 重构——原来分开的 `ad_close` / `game_header_close` 两条合成一条（`[vid="ad_close" || vid="game_header_close" || vid="iv_vertical_close"][clickable=true]`），补快照 [35090738](https://i.gkd.li/i/35090738)，示例 [8a375b99](https://e.gkd.li/8a375b99-4905-476c-8ff6-c27f4ef7a613)；第 2 条改为点 `desc="关闭"`（快照 [35090752](https://i.gkd.li/i/35090752)，示例 [178268bf](https://e.gkd.li/178268bf-af87-45b2-a41b-707b3bb5461a)）；第 4 条改选择器并补快照 [35090761](https://i.gkd.li/i/35090761)、示例 [fdb69898](https://e.gkd.li/fdb69898-e142-4bcb-be1c-408d6a9fd392)，活动页限定 `ChannelPage` / `Homepage`。同名组仍以底座的 4 条版本为准（序号 2），合并结果与 v24 相同

AIsouler 自用续订 v124 没有进入合并结果：

- 系统设置（`com.android.settings`）新增「功能类-WiFi无法联网时自动点击使用数据上网」（1 条）：在 `WifiAssistantDialog` 页点「使用数据流量上网」。快照 [35069641](https://i.gkd.li/i/35069641)。组名是功能类且不含「关闭」或「弹窗」，守卫丢掉
- 迅雷（`com.xunlei.downloadprovider`）「开屏广告」（2 条）：第 2 条改成 `anyMatches`（两条复杂选择器），快照 [35084444](https://i.gkd.li/i/35084444)。改后两条选择器都被更高层覆盖，守卫按重复选择器丢掉；v123 时这组是被同名组挡住（底座 3 条版本）。合并结果仍是底座版本，与 v24 相同
- 安全服务（`com.miui.securitycenter`）「功能类-自动允许启动应用」（1 条）：选择器里「InstallerX / Via」之后加上「Quetta」，补快照 [35069647](https://i.gkd.li/i/35069647)。组名是功能类且不含「关闭」或「弹窗」，守卫仍丢掉

GK-Lemon-D v50 实际并入：

- 网易云音乐（`com.netease.cloudmusic`）新增「权限提示-通知权限」（1 条，序号 37）：在 `MainActivity`，出现「开启推送通知」弹窗时点「取消」。选择器 `[vid="title"][text="开启推送通知"] < [vid="titleFrame"] +n [vid="buttonDefaultNegative"][text="取消"][clickable=true]`。权限提示默认关闭，不会自动点击

误触守卫挡住的组（合计 2153 组，v24 为 2151）：AIsouler 自用续订 150 组（重复选择器 75、功能类无「关闭/弹窗」28、名称命中拒绝词 29、滑动/返回 16、打开权限 2），比 v24 多 2 组——新增系统设置 WiFi 组（功能类）、迅雷「开屏广告」改后被判重复选择器。Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7）、GK-Lemon-D 10 组（名称命中拒绝词 6、功能类无「关闭/弹窗」1、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 387 组（重复选择器 234、功能类无「关闭/弹窗」114、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1），这四源与 v24 持平。

净变化：应用 +1，规则组 +1，规则 +1。全局组仍为 16。

## [24] - 2026-11-19

### 内容

对照 v23（1112 应用 / 5107 规则组 / 7938 规则 / 16 全局组），本版为 1113 应用 / 5109 规则组 / 7942 规则 / 16 全局组，订阅文件约 2.8 MB（2,872,841 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v637 → v638（chore: v638，2026-11-19 00:34:49Z）。v637 之后的内容提交：fix「小红书 功能类-自动[翻译]评论」（2026-11-18 06:35:03Z，Relates to #483）、perf 同组（2026-11-18 06:54:10Z，减少因上滑太快导致的误触）。另有 docs：加个 fastly.jsdelivr.net 订阅源（2026-11-18 13:30:27Z）。对照 v637 与 v638 的 dist，规则只有小红书这一组变化，文档提交没有进入订阅文件。改名后的组进入合并结果。
- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v128 → v129（chore: 🐔v129，2026-11-18 15:38:12Z）：feat Bettbox「功能类-自动[启动]后返回」、feat 系统界面「功能类-自动[右滑]清掉通话录音通知」，两处都进入合并结果。
- [Ling](https://github.com/cjy0812/Ling033_GKD_Rules) v15 → v16（chore: v16，2026-11-18 01:29:54Z；v23 拉源时未赶上）。该源只补缺口、不并入全局组。五处提交都没有进入合并结果。

其余十二个来源的版本与 v23 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、言木七 v54、AIsouler 自用续订 v123、GK-Lemon-D v49、火山虾 v78、YaChengMu v154。

Lin-arm v638 实际并入：

- 小红书（`com.xingin.xhs`）「功能类-评论自动翻译」改名为「功能类-自动[翻译]评论」（仍为 1 条，序号 20）。fix：不再点文本「回复 翻译」本身，改为点旁边的 ImageView（`ImageView[width<getPrev(1).height.plus(10)] < [childCount=2] - [text$="回复 翻译"][visibleToUser=true]`），并用坐标把点击位置右移（`left: width * 0.9`，`top: height * 0.5`），避开「回复」。活动页在笔记详情页 `com.xingin.matrix.notedetail.NoteDetailActivity` 之外加上短视频页 `com.xingin.matrix.detail.activity.DetailFeedActivity`，并加 `actionCd: 500`。快照仍有 [26643975](https://i.gkd.li/i/26643975)、[34877018](https://i.gkd.li/i/34877018)，新增 [35009573](https://i.gkd.li/i/35009573)、[35010199](https://i.gkd.li/i/35010199)。排除快照 [35009881](https://i.gkd.li/i/35009881)（误触回复）、[35010665](https://i.gkd.li/i/35010665)（高度不够会点到下方输入框；上游用点赞图标宽度做动态限制）。示例仍是 [fc8d70d4](https://e.gkd.li/fc8d70d4-f743-45df-a9d2-f343e419ccd9)。perf：说明改为「⚠️上滑太快可能有误触[收藏]情况」，并加 `actionDelay: 50`。组没有 `enable: false`，功能类默认关闭，不会自动点击。序号仍是 20，小红书其余组的序号和选择器未改

少年阿鲲 v129 实际并入：

- Bettbox（`com.appshub.bettbox`）新增应用，1 组（3 条）「功能类-自动[启动]后返回」（序号 1）。组写了 `enable: false`，并有 `matchRoot: true`、`matchTime: 5000`、`actionMaximum: 1`、`resetMatch: "app"`，活动页 `.MainActivity`。说明是进 app 后点「启动」再按返回。①已启动则本次不操作（`action: none`，desc 为「已开启」或包含「启动时间」），快照 [35034086](https://i.gkd.li/i/35034086)；②点「启动」（desc 为「已关闭」或包含「启动开关」），快照 [35034074](https://i.gkd.li/i/35034074)，示例 [2af99523](https://e.gkd.li/2af99523-a77d-4ffe-9969-486550d1a18a)；③在②之后按返回键（`action: back`，`actionDelay: 220`，`preKeys: [2]`）。功能类默认关闭，且组本身 `enable: false`，不会自动点击，也不会自动返回
- 系统界面（`com.android.systemui`）新增「功能类-自动[右滑]清掉通话录音通知」（1 条，序号 12）。组写了 `enable: false`。说明是「(⚠️仅适配 MIUI 13) 下拉通知栏后[右滑]清掉该通知」；上游注明 MIUI 13 以外没测试过。规则在展开的通知里匹配以「通话录音已完成」结尾的文本，然后向右滑（起点宽度 20% 到 80%，时长 200ms），`actionDelay: 1000`、`actionMaximum: 1`、`resetMatch: "app"`。快照 [35028500](https://i.gkd.li/i/35028500)，示例 [82046735](https://e.gkd.li/82046735-3d9d-4470-b8a5-e8b0f0402735)。功能类默认关闭，且组本身 `enable: false`，不会自动滑动。原先序号 1–11 的 11 个组未改

被守卫或名称拒绝词挡住、未进入合并结果：

- 微信（`com.tencent.mm`）「功能类-付款后自动延点完成/返回商家」：Ling 把 v15 的「功能类-付款后自动点击完成/返回商家」改成这个名字，把原来写在两条规则上的 `actionDelay: 6000` 提到组上，并加上组级 `fastQuery: true`。选择器、活动页和快照改成与 Lin-arm 现行版本一致：第 1 条仍点 `kinda_button_impl_wrapper` 上的「完成」或「返回商家」，并补快照 [33430797](https://i.gkd.li/i/33430797)；第 2 条活动页扩成三个 Lite 页，选择器放宽为「完成」「返回商家」或「Done」，快照增加 [29681932](https://i.gkd.li/i/29681932)、[31693084](https://i.gkd.li/i/31693084)、[33480728](https://i.gkd.li/i/33480728)。6 秒延时是 Ling 原来就有的，Lin-arm 这组没有这段延时。组名含「返回商家」，命中 HARD_DENY，守卫按名称拒绝词丢掉，没有写进合并结果。订阅里原有的「功能类-付款后自动点击完成/返回商家」仍是 AIsouler 底座的同名组（序号 26），与 v23 相同；Lin-arm 的同名组也仍被底座挡住
- 微信「功能类-快速切换账号」：Ling 新增。组名是功能类且不含「关闭」或「弹窗」，守卫丢掉。同名组仍以 Lin-arm 为准（序号 53）：`actionMaximum: 2`，说明是「适合俩账号的使用再多无法确认是否可行」，选择器没有 `index!=0`。Ling 这份要把 `actionMaximum` 改成 1、说明改成「排除第一个」、选择器加上 `[index!=0]`，并补快照 [34995719](https://i.gkd.li/i/34995719)，都没有写入。合并结果与 v23 相同
- 微信「功能类-交易-动态码(自动确认)」：Ling 新增，在转账动态码页（`.plugin.remittance.ui.RemittanceF2fDynamicCodeUI`）点「识别并支付」。快照 [34995049](https://i.gkd.li/i/34995049)、[34995351](https://i.gkd.li/i/34995351)，示例 [a0ef6a48](https://e.gkd.li/a0ef6a48-e469-412b-ac6a-493683b44341)。组名是功能类且不含「关闭」或「弹窗」，守卫丢掉。名称没有命中 HARD_DENY。微信的规则组与 v23 相同，没有这组
- 云·星穹铁道（`com.miHoYo.cloudgames.hkrpg`）「功能类-进游戏节点优选」：Ling 新增，2 条（「节点优选」「点击进入游戏」），按排队「空闲」优先于「少量」、再比延迟。组名是功能类且不含「关闭」或「弹窗」，守卫丢掉。这个应用在合并结果里原有另外 3 个组，与 v23 相同，没有这组
- 淘宝（`com.taobao.taobao`）「功能类-自动进取件列表」：Ling 新增，1 条，在「我的」页点以「取件」结尾的入口。活动页 `com.taobao.tao.welcome.Welcome`。快照 [34985860](https://i.gkd.li/i/34985860)，示例 [6dafd548](https://e.gkd.li/6dafd548-52c7-4904-8190-c6e24d2255a4)。组名是功能类且不含「关闭」或「弹窗」，守卫丢掉。淘宝的规则组与 v23 相同，没有这组

误触守卫挡住的组（合计 2151 组，v23 为 2147）：AIsouler 自用续订 148 组（重复选择器 74、功能类无「关闭/弹窗」27、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 38 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」7），比 v23 多 4 组，都在功能类——微信「快速切换账号」「交易-动态码(自动确认)」、云·星穹铁道「进游戏节点优选」、淘宝「自动进取件列表」。付款那组是改名：旧名和新名都含「返回商家」，名称拒绝词仍是 10 组。GK-Lemon-D 10 组（名称命中拒绝词 6、功能类无「关闭/弹窗」1、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 387 组（重复选择器 234、功能类无「关闭/弹窗」114、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1），这四源与 v23 持平。

净变化：应用 +1，规则组 +2，规则 +4。全局组仍为 16。

## [23] - 2026-11-18

### 内容

对照 v22（1112 应用 / 5106 规则组 / 7937 规则 / 16 全局组），本版为 1112 应用 / 5107 规则组 / 7938 规则 / 16 全局组，订阅文件约 2.8 MB（2,871,090 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v636 → v637（chore: v637，2026-11-18 01:04Z）。拼多多「功能类-搜索页-长按词条直接删除」和「功能类-展开更多」进入合并结果。小红书「分段广告-信息流广告」、拼多多「全屏广告-下单后出现的弹窗」、微信「功能类-自动查看原图」仍被底座同名组挡住。
- [AIsouler 自用续订](https://github.com/AIsouler/gkd-subscription) v122 → v123（perf: rules，2026-11-17 14:19Z；chore: v123，2026-11-17 14:21Z）。该源只补缺口、不并入全局组。三处规则改动都没有进入合并结果。
- [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) v48 → v49（Update bilibili rules，2026-11-17 02:25Z）。哔哩哔哩两条视频暂停广告规则进入合并结果。

其余十二个来源的版本与 v22 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v128、言木七 v54、Ling v15、火山虾 v78、YaChengMu v154。

Lin-arm v637 实际并入：

- 拼多多（`com.xunmeng.pinduoduo`）新增「功能类-搜索页-长按词条直接删除」（1 条）：搜索页（`.activity.NewPageActivity`）在「最近搜索」旁点可点击的删除按钮（文本「」，旁边是以「清除」开头的按钮）。快照 [34990299](https://i.gkd.li/i/34990299)，示例 [fbb6437e](https://e.gkd.li/fbb6437e-63fe-4b6e-8685-8ec5b5d32353)。组没有 `enable: false`，功能类默认关闭，不会自动点击。新组序号为 35。原先序号 35–57 的 23 个组改为 36–58，选择器未改
- 拼多多「功能类-展开更多」（仍为 4 条，序号 24）：第 1 条「通用[展开]_fastQ」增加排除，出现可点击的「轻触照亮」或文案以「相册」结尾时不再点「展开」。排除快照 [34986764](https://i.gkd.li/i/34986764)，原快照 [29405868](https://i.gkd.li/i/29405868) 仍在。其余三条（查看更多订单信息、订单页、商品评论）未改。功能类默认关闭，不会自动点击

GK-Lemon-D v49 实际并入：

- 哔哩哔哩（`tv.danmaku.bili`）「全屏广告-视频暂停广告倒计时」（1 条，序号 55）：去掉 `matchRoot: true`。两条选择器收成一条 `TextView[text="后将展示广告"] + @[text="取消"]`（原先分别点 TextView 和 Button 上的「取消」）。活动页仍是视频详情页和合集播放页。全屏广告默认关闭，不会自动点击
- 哔哩哔哩「全屏广告-视频暂停广告」（1 条，序号 56）：去掉 `matchRoot: true`，并去掉点 `desc="close"` 的选择器，只保留 `@View[clickable=true] > [desc="关闭暂停页"] + Button`。活动页未改。全屏广告默认关闭，不会自动点击

被更高层同名组挡住、未进入合并结果：

- 小红书（`com.xingin.xhs`）「分段广告-信息流广告」：Lin-arm 增加半屏搜索活动页 `com.xingin.alioth.search.GlobalSearchHalfScreenActivity`，并给长按卡片那条补快照 [34992416](https://i.gkd.li/i/34992416)。同名组仍以 AIsouler 底座为准，合并结果与 v22 相同
- 拼多多「全屏广告-下单后出现的弹窗」：Lin-arm 把 WebView 文本从「拼多多」放宽为「拼多多」或空文本，并补快照 [34986289](https://i.gkd.li/i/34986289)。同名组仍以底座为准，合并结果与 v22 相同
- 微信（`com.tencent.mm`）「功能类-自动查看原图」：Lin-arm 给「查看」和「原图」加上 `text!$="0K"`，第 2 条去掉规则上的活动页 `.ui.LauncherUI`，并补排除快照 [34987211](https://i.gkd.li/i/34987211)。同名组仍以底座为准，合并结果与 v22 相同

AIsouler 自用续订 v123 没有进入合并结果：

- 抖音（`com.ss.android.ugc.aweme`）「全屏广告」：上滑时长由 200ms 改为 300ms，一条用 `||` 拼起来的 `matches` 拆成三条 `anyMatches`。规则带上滑，误触守卫按滑动丢掉。同名组仍以底座为准
- 知乎（`com.zhihu.android`）「开屏广告」：一条用 `||` 拼起来的选择器拆成两条 `anyMatches`（`vid="btn_skip"`，以及带长度和宽高限制的「跳过」）。v122 时整段选择器已被更高层覆盖，守卫按重复选择器丢掉；拆开后不再算重复，但同名组仍以底座为准，没有写入合并结果
- 安全服务（`com.miui.securitycenter`）「功能类-应用信息页-自启动提示」：第 1 条由 `action: back` 改为点「知道了」或「确定」，并补快照 [34970577](https://i.gkd.li/i/34970577)。组名是功能类且不含「关闭」或「弹窗」，守卫仍丢掉。同名组仍以底座为准

误触守卫挡住的组（合计 2147 组，v22 为 2148）：AIsouler 自用续订 148 组（重复选择器 74、功能类无「关闭/弹窗」27、名称命中拒绝词 29、滑动/返回 16、打开权限 2），比 v22 少 1 组，少在重复选择器——知乎「开屏广告」拆开选择器后不再被判为重复，转而被同名组挡住。Ling 34 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」3）、GK-Lemon-D 10 组（名称命中拒绝词 6、功能类无「关闭/弹窗」1、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 387 组（重复选择器 234、功能类无「关闭/弹窗」114、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1），这四源与 v22 持平。

净变化：应用数不变，规则组 +1，规则 +1。全局组仍为 16。

## [22] - 2026-11-17

### 内容

对照 v21（1111 应用 / 5102 规则组 / 7930 规则 / 16 全局组），本版为 1112 应用 / 5106 规则组 / 7937 规则 / 16 全局组，订阅文件约 2.8 MB（2,870,603 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v635 → v636。v636（chore: v636，2026-11-17 00:21Z）：Avmini 新应用、网易BUFF 权限提示、抖音与学习通选择器修订进入合并结果。
- [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) v47 → v48：哔哩哔哩两条全屏广告规则补 key 与 matchRoot，进入合并结果。

其余十三个来源的版本与 v21 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v128、言木七 v54、AIsouler 自用续订 v122、Ling v15、火山虾 v78、YaChengMu v154。

Lin-arm v636 实际并入：

- Avmini（`com.hongjing.avmini`）新增应用，3 组（6 条）：「开屏广告」（1 条）：点带「广告」标识的关闭入口。快照 [34912905](https://i.gkd.li/i/34912905)。组没有 `enable: false`，开屏分类默认开启，这条会生效；「全屏广告」（2 条）：点全屏广告的关闭图标。快照 [34913673](https://i.gkd.li/i/34913673)、[34913869](https://i.gkd.li/i/34913869)、[34916377](https://i.gkd.li/i/34916377)。全屏广告默认关闭，不会自动点击；「局部广告」（3 条）：点各广告位的关闭按钮（`native_ad_close_iv`、「✕」、close_button）。快照 [34913988](https://i.gkd.li/i/34913988)、[34914899](https://i.gkd.li/i/34914899)、[34914902](https://i.gkd.li/i/34914902)、[34914896](https://i.gkd.li/i/34914896)、[34915691](https://i.gkd.li/i/34915691)。局部广告默认关闭，不会自动点击
- 网易BUFF（`com.netease.buff`）新增「权限提示-通知权限」（1 条）：出现通知权限标题时点「取消」。快照 [34897764](https://i.gkd.li/i/34897764)。权限提示默认关闭，不会自动点击；原「更新提示」组序号由 1 改为 2，选择器未改
- 学习通（`com.chaoxing.mobile`）「通知提示-剪贴板内容已更新」：去掉 activityIds 限制（不再限定在通知页、话题页等三个界面），并补快照 [34897863](https://i.gkd.li/i/34897863)、[34901303](https://i.gkd.li/i/34901303)。通知提示默认关闭，不会自动点击；「功能类-签到失败后弹窗」：匹配文本由「签到失败」放宽为「签到失败」或「已过期」，并补快照 [34916325](https://i.gkd.li/i/34916325)。功能类默认关闭，不会自动点击
- 抖音（`com.ss.android.ugc.aweme`）「功能类-刷到推广视频时[上滑]」：「广告」由后缀匹配放宽为包含匹配，并补快照 [34942307](https://i.gkd.li/i/34942307)。功能类默认关闭，不会自动上滑

GK-Lemon-D v48 实际并入：

- 哔哩哔哩（`tv.danmaku.bili`）「全屏广告-视频暂停广告倒计时」「全屏广告-视频暂停广告」：两条规则补 `key: 0` 与 `matchRoot: true`，选择器未改。全屏广告默认关闭

误触守卫挡住的组（合计 2148 组，与 v21 持平）：AIsouler 自用续订 149 组（重复选择器 75、功能类无「关闭/弹窗」27、名称命中拒绝词 29、滑动/返回 16、打开权限 2）、Ling 34 组（滑动/返回 21、名称命中拒绝词 10、功能类无「关闭/弹窗」3）、GK-Lemon-D 10 组（名称命中拒绝词 6、功能类无「关闭/弹窗」1、选择器命中补充拒绝词 2、重复选择器 1）、火山虾 1568 组（重复选择器 1322、功能类无「关闭/弹窗」127、过宽开屏 9、名称命中拒绝词 45、过宽图片 3、打开权限 25、滑动/返回 37）、YaChengMu 387 组（重复选择器 234、功能类无「关闭/弹窗」114、名称命中拒绝词 20、滑动/返回 13、打开权限 4、过宽开屏 1、过宽图片 1）。

净变化：应用 +1，规则组 +4，规则 +7。全局组仍为 16。

## [21] - 2026-11-16

### 内容

对照 v20（1110 应用 / 5095 规则组 / 7922 规则 / 16 全局组），本版为 1111 应用 / 5102 规则组 / 7930 规则 / 16 全局组，订阅文件约 2.8 MB（2,867,594 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示、权限提示、评价提示默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v633 → v635。v634（chore: v634，2026-11-14 22:37Z）：荣耀桌面新应用、网易云音乐两条功能类、以及番茄免费小说「观看广告自动静音」进入合并结果。哔哩哔哩（`tv.danmaku.bili`）「分段广告-首页推荐视频卡片广告」的改动被更高层同名组挡住。v635（chore: v635，2026-11-15 23:01Z）：小红书两条新组、淘宝两条新组、淘宝首页横幅选择器修订、以及小红书五条「自动倍速」进入合并结果。抖音「全屏广告」的改动被更高层同名组挡住。

其余十四个来源的版本与 v20 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、少年阿鲲 v128、言木七 v54、AIsouler 自用续订 v122、Ling v15、GK-Lemon-D v47、火山虾 v78、YaChengMu v154。

Lin-arm v634 实际并入：

- 荣耀桌面（`com.hihonor.android.launcher`）新增「功能类-[不]添加小部件到桌面」（1 条）：出现「添加到主屏幕」时点「取消」。快照 [34847270](https://i.gkd.li/i/34847270)。功能类默认关闭，不会自动点击
- 网易云音乐（`com.netease.cloudmusic`）新增「功能类-自动领取VIP成长值」（1 条）：点「一键领取」。快照 [34813013](https://i.gkd.li/i/34813013)。功能类默认关闭，不会自动领取
- 网易云音乐新增「功能类-自动打卡并关闭黑胶乐签」（2 条）：先点「打卡」，再关掉「黑胶乐签」弹窗。快照 [34813013](https://i.gkd.li/i/34813013)、[34813443](https://i.gkd.li/i/34813443)。功能类默认关闭，不会自动打卡。后面的组序号 +2，选择器未改
- 番茄免费小说（`com.dragon.read`）「功能类-观看广告自动静音」：①点击[静音] 的高度上限由 108 放宽到 130，并补快照 [34841008](https://i.gkd.li/i/34841008)、[34840554](https://i.gkd.li/i/34840554)；②坐标点击[静音] 的快照换成 [34847712](https://i.gkd.li/i/34847712)。功能类默认关闭，不会自动静音

Lin-arm v635 实际并入：

- 小红书（`com.xingin.xhs`）新增「功能类-评论自动翻译」（1 条）：点「回复 翻译」。快照 [26643975](https://i.gkd.li/i/26643975)、[34877018](https://i.gkd.li/i/34877018)。上游注明有可能误触「回复评论」，新版 app 暂无问题。功能类默认关闭，不会自动点击
- 小红书新增「权限提示-定位权限」（1 条）：出现定位权限标题时点取消。快照 [34877280](https://i.gkd.li/i/34877280)。权限提示默认关闭，不会自动点击
- 小红书「功能类-自动倍速⏩」五条（x0.75 / x1.25 / x1.5 / x2.0 / x3.0）：长按视频改为先确认进度条剩余秒数小于 3 秒，actionDelay 从组级 3000 改到规则级 1000。功能类默认关闭，不会自动切倍速
- 淘宝（`com.taobao.taobao`）新增「功能类-删除订单直接确认」（1 条）：在「确认删除订单?」弹窗点「确定」。快照 [34883506](https://i.gkd.li/i/34883506)。功能类默认关闭，不会自动确认删除
- 淘宝新增「评价提示-商品评论区评价满意度」（1 条）：评论区插入「你对看到的评价内容满意吗？」卡片时点关闭。评价提示默认关闭，不会自动点击
- 淘宝「局部广告-横幅广告」首页规则选择器由 `[desc.length=4] < * + @[clickable=true] > [text="뉜"]` 收紧为 `FrameLayout[childCount=4] > ImageView + LinearLayout[childCount=2] + [childCount=1] + @[clickable=true] > [text="뉜"]`，并补快照 [34881835](https://i.gkd.li/i/34881835)。局部广告默认关闭

被更高层同名组挡住、未进入合并结果：

- 哔哩哔哩（`tv.danmaku.bili`）「分段广告-首页推荐视频卡片广告」的选择器改动仍被更高层同名组挡住，合并结果与 v20 相同
- 抖音（`com.ss.android.ugc.aweme`）「全屏广告」的改动被更高层同名组挡住，合并结果与 v20 / 旧 v21 相同

净变化：应用 +1，规则组 +7，规则 +8。全局组仍为 16。

## [20] - 2026-11-14

### 内容

对照 v19（1110 应用 / 5094 规则组 / 7921 规则 / 16 全局组），本版为 1110 应用 / 5095 规则组 / 7922 规则 / 16 全局组，订阅文件约 2.8 MB（2,864,421 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、分段广告、功能类、通知提示默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v631 → v633。v632（chore: v632，2026-11-12 23:43Z）：学习通签到失败弹窗、签到成功后返回、剪贴板提示，以及移动爱家局部广告进入合并结果。上游删掉的 OPPO/一加「功能类-自动[勾选]已知悉风险」同步去掉。v633（chore: v633，2026-11-13 23:45Z）：「我的荣耀」开屏广告进入合并结果。其余改动被更高层同名组挡住
- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v127 → v128（chore: 🐔v128，2026-11-13 14:47Z）：改写百度贴吧「功能类-自动[保存][原图]」

其余十三个来源的版本与 v19 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、言木七 v54、AIsouler 自用续订 v122、Ling v15、GK-Lemon-D v47、火山虾 v78、YaChengMu v154。

Lin-arm v632 实际并入：

- 学习通（`com.chaoxing.mobile`）新增「功能类-签到失败后弹窗」（1 条）：出现「签到失败」时点「知道了」。快照 [34723729](https://i.gkd.li/i/34723729)。功能类默认关闭，不会自动点击
- 学习通「功能类-签到成功后自动[返回]」补了 `.webapp.ui.WebAppCommonViewer` 界面，快照 [34723724](https://i.gkd.li/i/34723724)。功能类默认关闭，不会自动返回
- 学习通「通知提示-剪贴板内容已更新」补了话题页 `.group.ui.TopicBodyActivity`，快照 [34748077](https://i.gkd.li/i/34748077)。通知提示默认关闭，不会自动点击
- 移动爱家（`com.cmri.universalapp`）新增「局部广告」（3 条）：横幅式点 `vid=close_banner`（快照 [17872961](https://i.gkd.li/i/17872961)）；卡片信息流式点 `vid=iv_close`（快照 [30197268](https://i.gkd.li/i/30197268)、[32419081](https://i.gkd.li/i/32419081)）；摄像机控制页横幅式2 点关闭（快照 [25209084](https://i.gkd.li/i/25209084)、[34723502](https://i.gkd.li/i/34723502)）。局部广告默认关闭，不会自动点击
- OPPO/一加应用安装器（`com.oplus.appdetail`）：此前从 Lin-arm 并入的「功能类-自动[勾选]已知悉风险」被上游删掉，合并结果同步去掉。后面的组序号前移，选择器未改

Lin-arm v633 实际并入：

- 我的荣耀（`com.hihonor.phoneservice`）「开屏广告」改为点 `[text*="跳过"][clickable=true][text.length<10]`，并加上 `resetMatch: "app"`、`priorityTime: 10000`。快照 [34807611](https://i.gkd.li/i/34807611)。上游说明是有人反馈全局开屏触发慢，故单独适配。组没有 `enable: false`，开屏分类默认开启，这条会生效。原先来自更低层的选择器（`TextView[id="com.hihonor.phoneservice:id/start_skip_count_down"]`，快照 [14896804](https://i.gkd.li/import/14896804)，活动页 `OpenScreenAdActivity`）被 Lin-arm 同名组替换

少年阿鲲 v128 实际并入：

- 百度贴吧（`com.baidu.tieba`）「功能类-自动[保存][原图]」由 5 条收成 3 条，并加了 `matchRoot: true`、`actionDelay: 100`。流程改为：①查看原图（快照 [34725600](https://i.gkd.li/i/34725600)）→ ②长按屏幕中心（⚠️有概率不生效）→ ③保存到相册（快照 [34725662](https://i.gkd.li/i/34725662)、[34725702](https://i.gkd.li/i/34725702)）。组仍写了 `enable: false`，功能类默认关闭，不会自动点击

被更高层同名组挡住、未进入合并结果：

- 哔哩哔哩「分段广告-视频详情页下方推广」：Lin-arm v632 改了选择器。同名组仍以 AIsouler 底座为准，选择器与 v19 相同。分段广告默认关闭
- OPPO/一加应用安装器「功能类-自动安装应用」：Lin-arm v632 把勾选「已知悉风险」、点「仍然安装」和坐标点「继续安装」收进这组（5 条）。同名组仍以底座为准，还是「继续安装」和「完成」两条，与 v19 相同。本订阅里另有 Adpro 的「功能类-自动安装」（写了 `enable: false`），名字不同，内容未改，只因删组而序号前移
- 买单吧「通知提示-网络代理提示弹窗」：Lin-arm v633 改了，更高层已有同名组，合并结果与 v19 相同
- 番茄免费小说「分段广告-阅读页面广告」：Lin-arm v633 改了，更高层已有同名组，合并结果与 v19 相同
- 支付宝「开屏广告-小程序开屏广告」：Lin-arm v633 改了，更高层已有同名组，合并结果与 v19 相同
- X(推特)「分段广告-主页信息流广告」：Lin-arm v633 改了，更高层已有同名组，合并结果与 v19 相同
- 哔哩哔哩「全屏广告-会员弹窗」：Lin-arm v633 改了，更高层已有同名组，合并结果与 v19 相同
- 哔哩哔哩「分段广告-首页推荐视频卡片广告」：Lin-arm v633 改了（上游 Relates/Close #473），更高层已有同名组，合并结果与 v19 相同

净变化：应用数不变，规则组 +1，规则 +1。全局组仍为 16。学习通新组序号为 18，原先的「权限提示-开启消息通知」「未分类-开启消息通知」「通知提示」由 18–20 改为 19–21。「通知提示-剪贴板内容已更新」（key 15）和「功能类-签到成功后自动[返回]」（key 17）的序号未改。移动爱家新组序号为 8，原先三个组的序号未改。OPPO/一加应用安装器去掉 key 3 后，「功能类-忽略增强防护提示」由 4 改为 3，「功能类-自动安装」由 5 改为 4。「功能类-自动安装应用」（key 1）和「功能类-安装中高风险应用」（key 2）的序号与选择器都未改。我的荣耀「开屏广告」（key 11）和百度贴吧「功能类-自动[保存][原图]」（key 32）的序号未改。

## [19] - 2026-11-11

### 内容

对照 v18（1107 应用 / 5088 规则组 / 7914 规则 / 16 全局组），本版为 1110 应用 / 5094 规则组 / 7921 规则 / 16 全局组，订阅文件约 2.8 MB（2,863,543 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。开屏广告默认仍是开启的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v629 → v631（chore: v631，2026-11-10 23:35Z）：顽鹿运动开屏、天猫精灵会员弹窗、软件包安装程序安全模式提示、游戏中心通知权限、系统管家禁止跳转进入合并结果。花小猪打车弹窗与 QQ 局部广告仍被底座同名组挡住。「订阅源域名变更提示」和「从订阅作者处显示提醒」没有进入 `apps` / `groups`
- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v124 → v127：v125（2026-11-09）的支付宝新村、小游戏弹窗、多选勾选垃圾消息进入合并结果，「功能类-无法访问时点击[返回]」仍被底座挡住。v126 把起点读书「每日福利-自动去看广告」的选择器改了，组仍然关闭。v127 改了快手极速版任务页弹窗，这组会继续生效
- [YaChengMu 精简续更](https://github.com/YaChengMu/gkd_subscription_min) v153 → v154（2026-11-10）：新增和改动的组要么与 Lin-arm 已并入的同名组相同，要么被底座同名组挡住。功能类里不含「关闭」或「弹窗」的组，误触守卫也会丢掉。合并结果没有来自该源的差异

其余十二个来源的版本与 v18 相同：AIsouler v406、奥怪 v89、甘霖 v72、梦念逍遥 v79、Mrlc v75、Adpro v90、九千院 v9、言木七 v54、AIsouler 自用续订 v122、Ling v15、GK-Lemon-D v47、火山虾 v78。

Lin-arm 实际并入：

- 新应用：顽鹿运动（`com.onelap.bls.dear`）「开屏广告」（1 条）。点可点击的 `vid=ll_skip_advertisement_splash`，先等 1 秒，避免点太早被当成异常互动、跳过按钮锁满 5 秒。快照 [34618778](https://i.gkd.li/i/34618778)。组没有 `enable: false`，开屏分类默认开启，这条会生效
- 新应用：(荣耀)游戏中心（`com.hihonor.gamecenter`）「权限提示-通知权限」（1 条）：首页同时出现「开启」和「通知」时点「禁止」。快照 [34632910](https://i.gkd.li/i/34632910)。权限提示默认关闭，不会自动点击
- 新应用：(荣耀)系统管家服务（`com.hihonor.systemmanager`）「功能类-自动禁止应用跳转」（1 条）：出现「想要打开」时点「拒绝」。快照 [34633109](https://i.gkd.li/i/34633109)。功能类默认关闭，不会自动点击
- 软件包安装程序新增「功能类-[开启安全模式]提示弹窗」（1 条）：安装成功页出现「开启安全模式」时点「取消」。快照 [34540653](https://i.gkd.li/i/34540653)。功能类默认关闭，不会自动点击
- 天猫精灵新增「全屏广告-会员弹窗」（2 条）。Lin-arm 把自家的「全屏广告-超级会员弹窗」改成这个名字，并加了一条规则。第 1 条在营销弹窗页点「会员」旁边的关闭图，快照 [34570686](https://i.gkd.li/i/34570686)。第 2 条仍是付款页按坐标点关闭，快照 [14443874](https://i.gkd.li/i/14443874)，与底座「全屏广告-超级会员弹窗」的那条相同。底座那组的名字没变，改名后的组就按新名字补了进来。全屏广告默认关闭，不会自动点击

少年阿鲲实际并入：

- 支付宝新增「功能类-多选时自动[勾选]垃圾消息」（1 条，写了 `enable: false`，功能类默认关闭，不会自动勾选）：在个人聊天多选页，勾选未选中、文案含「送你」「请你」「有AI传话」或「你的小鸡」、且长度小于 20 的消息。点的是消息布局 `chat_msg_layout`，不是复选框本身。快照 [34544908](https://i.gkd.li/i/34544908)、[34544910](https://i.gkd.li/i/34544910)、[34562288](https://i.gkd.li/i/34562288)

下面两组没有 `enable: false`，名称也不落到默认关闭的分类，会继续生效：

- 支付宝「⛪新村-已玩15s小游戏」：不再要求「已发放」旁边是「产速奖励」或「抽奖机会」，外层由 `< View <2 View` 改为 `<2 View <2 View`。补快照 [34539052](https://i.gkd.li/i/34539052)
- 支付宝「🎮小游戏-弹窗」：去掉组上的 `resetMatch: "match"`。三条规则（小浮窗、活动弹窗、游戏更新）的选择器未改。`actionMaximum` 仍是 1，弹窗消失后再出现不再重新计数

另外两组：

- 起点读书「📆每日福利-自动去看广告」：点击目标由 `[clickable=true][text="去完成"]` 改为 `[desc=null][text="去完成"]`，用来匹配点不了的「去完成」。去掉快照 [23561912](https://i.gkd.li/i/23561912)，补快照 [34614870](https://i.gkd.li/i/34614870)。组仍然写了 `enable: false`，不会自动点击
- 快手极速版「⛳任务页-弹窗-X掉」：第 1 到第 5 条去掉了各自的活动页 `com.kwai.kds.krn.api.page.KwaiRnActivity`，改为沿用组上已有的活动页（首页、网页容器、拦截页、Yoda 页、KwaiRn）。选择器未改。第 1 条快照 [31456749](https://i.gkd.li/i/31456749) 在上游 dist 里写成了两条相同链接（源码注释分别是 E 和 A，编译后注释被去掉）。这组没有 `enable: false`，名称也不落到默认关闭的分类，会继续生效

被同名组挡住、未进入合并结果：

- 花小猪打车「全屏广告-弹窗广告」：Lin-arm 新增一条坐标点击，快照 [34613080](https://i.gkd.li/i/34613080)，并把 `resetMatch` 从 `app` 改成 `match`、去掉 `matchTime`、活动页提到组上。同名组仍以 AIsouler 底座为准，还是只点 `vid=popClose` 的那一条，与 v18 相同
- QQ「局部广告」：Lin-arm 给活动页 `.activity.QPublicFragmentActivity`、选择器为 `desc="关闭广告"` 的那条加了 500ms `actionDelay`（点太早、动画没完容易误触）。快照仍是 [33948809](https://i.gkd.li/i/33948809)。底座同名组没有这条规则，整组仍以 AIsouler 为准，这条延迟没有进入合并结果
- 支付宝「功能类-无法访问时点击[返回]」：少年阿鲲去掉了排除小程序活动页 `XRiverActivity$` 的 `excludeActivityIds`，并补快照 [34539245](https://i.gkd.li/i/34539245)（`.XRiverActivity$App01`）。同名组仍以 AIsouler 底座为准。底座用的是另一套选择器（点 `back_button`），与 v18 相同，也不含这条排除

YaChengMu v154 对照其变更记录和当前快照，没有一条进入合并结果：

- QQ 把「功能类-登录授权」改名为「功能类-设备登录授权」，并新增「功能类-App申请信息/登录授权」。忽略序号后，与 Lin-arm 在 v15 并入的同名组相同
- 哔哩哔哩新增「功能类-直播间抽奖弹窗」。选择器与 Lin-arm 在 v15 并入的同名组相同，误触守卫会当成重复选择器丢掉
- 抖音新增「功能类-自动开启[自动连播]」，并把「功能类-刷到推广视频时[上滑]」的冷却从 300ms 改为 1200ms，「功能类-刷到游戏视频时[上滑]」和「功能类-刷到直播时[上滑]」去掉 300ms 冷却。与 Lin-arm 已在 v16、v18 并入的同名组相同
- 抖音极速版新增「功能类-自动开启[自动连播]」，番茄免费小说新增「功能类-刷短剧时半自动[不喜听书]」。与 Lin-arm 在 v16 并入的同名组相同
- 上面这些功能类组，除直播间抽奖弹窗外，名称里没有「关闭」或「弹窗」，误触守卫会丢掉
- 支付宝「局部广告-卡片广告」的「余额宝广告」加上外层 `[childCount=4]`，并排除快照 [34356908](https://i.gkd.li/i/34356908)。同名组仍以底座为准，选择器与 v18 相同

没有进入 `apps` / `groups`、因此未并入：

- Lin-arm「docs: 订阅源域名变更提示」只改了该仓的 `README.md` 和 `Template.md`
- Lin-arm「perf: 从订阅作者处显示提醒」只把该仓订阅的 `author` 改成 `gkd667.vv.ax源即将停用,建议更换`。本订阅的 `author` 仍是 Dear-Ded

净变化：应用 +3，规则组 +6，规则 +7。全局组仍为 16。软件包安装程序新组序号为 9，原先的「功能类-勾选[已了解该应用存在的风险]」由 9 改为 10，选择器未改，其余组序号未改。天猫精灵新组序号为 3，原来的「全屏广告-超级会员弹窗」（key 2）未改。支付宝新组序号为 85，排在它后面的 12 个规则组只是序号顺延（85–96 改为 86–97），选择器未改。「⛪新村-已玩15s小游戏」（key 71）、「🎮小游戏-弹窗」（key 76）、起点读书「📆每日福利-自动去看广告」（key 38）、快手极速版「⛳任务页-弹窗-X掉」（key 22）的序号未改。

## [18] - 2026-11-09

### 内容

对照 v17（1107 应用 / 5088 规则组 / 7912 规则 / 16 全局组），本版为 1107 应用 / 5088 规则组 / 7914 规则 / 16 全局组，订阅文件约 2.8 MB（2,860,673 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v627 → v629（2026-11-08）：安小家局部广告、FlClash 节点测延迟、抖音三条上滑进入合并结果。豆瓣开屏与百度贴吧悬浮小广告仍被底座同名组挡住，合并结果与 v17 相同
- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v123 → v124（2026-11-07）：支付宝小游戏浏览与弹窗、微信小程序看完广告进入合并结果

其余十三个来源的版本与 v17 相同。

Lin-arm 实际并入（都在局部广告或功能类，默认关闭，不会自动点击）：

- 安小家（`cn.luowice.anxiaojia`）「局部广告」第 3 条：关闭按钮前面的节点不再限定 ImageView，旁边文案长度从大于 9 放宽到大于 6。快照 [34518515](https://i.gkd.li/i/34518515)
- FlClash（`com.follow.clash`）「功能类-节点自动测延迟」新增第 2 条：在代理页点「延迟测试」。原有点「代理」的规则改挂到组的活动页 `.MainActivity` 上。进应用后最多测 1 次。快照 [34530552](https://i.gkd.li/i/34530552)
- 抖音（`com.ss.android.ugc.aweme`）「功能类-刷到推广视频时[上滑]」：动作冷却从 300ms 改为 1200ms，避免自动化模式下多滑一次。同一提交里，「功能类-刷到游戏视频时[上滑]」和「功能类-刷到直播时[上滑]」去掉了 300ms 冷却。三条都是上滑，功能类默认关闭，不会自动滑动

少年阿鲲实际并入（这三组没有 `enable: false`，名称也不落到默认关闭的分类，会继续生效）：

- 支付宝「🎮小游戏-半自动浏览15s广告」改名为「🎮小游戏-半自动浏览15s/30s广告」（4 条改为 5 条）。15 秒退出排除带「返回首页」的页面，并新增一条 30 秒后退出。快照 [34519309](https://i.gkd.li/i/34519309)、[34519314](https://i.gkd.li/i/34519314)
- 支付宝「🎮小游戏-弹窗」的「⑨游戏更新-确定」：由「游戏有新版本」加按钮「确定」放宽为文案含「新版本」或「更新」的可点击「确定」。快照 [34523741](https://i.gkd.li/i/34523741)
- 微信「🧩小程序-看完30s广告-x掉」第 4 条（直播已获得奖励）：关闭按钮所在 FrameLayout 改为取父节点最后一个，外层子节点数从等于 4 放宽到大于 2。快照 [34519105](https://i.gkd.li/i/34519105)

被底座挡住、未进入合并结果：

- 豆瓣「开屏广告」：Lin-arm 新增一条点 `vid=sdk_view` 内较小关闭区域的规则。快照 [34494192](https://i.gkd.li/i/34494192)、[34514159](https://i.gkd.li/i/34514159)。同名组仍以 AIsouler 底座为准，选择器与 v17 相同
- 百度贴吧「局部广告-悬浮小广告」：Lin-arm 把活动页补上吧内页 `.forum.ForumActivity`，并把「悬浮广告1」从固定宽度的 ImageView 放宽。快照 [34523272](https://i.gkd.li/i/34523272)。同名组仍以底座为准，合并结果与 v17 相同

净变化：应用数不变，规则组数不变（支付宝浏览组只是改名），规则 +2。全局组仍为 16。安小家、FlClash、抖音、支付宝、微信里其余规则组的序号未改。

## [17] - 2026-11-07

### 内容

对照 v16（1107 应用 / 5087 规则组 / 7911 规则 / 16 全局组），本版为 1107 应用 / 5088 规则组 / 7912 规则 / 16 全局组，订阅文件约 2.8 MB（2,859,425 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v626 → v627（2026-11-06）：Quetta「功能类-下载完自动[打开]文件」进入合并结果
- [AIsouler 自用续订](https://github.com/AIsouler/gkd-subscription) v121 → v122（2026-11-06）：红果短剧（海外包）「权限提示-通知权限」补了短剧播放页，「全屏广告」新增上滑。两条都与 Lin-arm 已有同名组相同，合并结果与 v16 相同；全屏广告还是滑动，误触守卫也会丢掉

其余十三个来源的版本与 v16 相同。

Lin-arm 实际并入（功能类，默认关闭，不会自动点击）：

- Quetta（`net.quetta.browser`）新增「功能类-下载完自动[打开]文件」（1 条）：下载完成出现「文件已下载完毕」时点「打开」。快照 [34482455](https://i.gkd.li/i/34482455)

被更高层同名组挡住、未进入合并结果：

- 红果短剧（海外包 `com.phoenix.read.oversea.gp`）「权限提示-通知权限」：AIsouler 自用续订把活动页从首页扩到短剧播放页 `com.dragon.read.component.shortvideo.impl.ShortSeriesActivity`，并补快照 [34348017](https://i.gkd.li/i/34348017)。同名组已由 Lin-arm 在 v15 并入，选择器与 v16 相同
- 红果短剧（海外包）「全屏广告」：AIsouler 自用续订新增在首页上滑关掉 `vid=ad_source`，快照 [34213154](https://i.gkd.li/i/34213154)。同名组已由 Lin-arm 并入，内容相同。这条是滑动，误触守卫也会丢掉

净变化：应用数不变，规则组 +1，规则 +1。全局组仍为 16。Quetta 原有五个功能类组的序号未改。

## [16] - 2026-11-06

### 内容

对照 v15（1107 应用 / 5083 规则组 / 7902 规则 / 16 全局组），本版为 1107 应用 / 5087 规则组 / 7911 规则 / 16 全局组，订阅文件约 2.8 MB（2,859,029 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v625 → v626（2026-11-05）：番茄免费小说、软件包安装程序、抖音、抖音极速版四条新组进入合并结果。X「分段广告-主页信息流广告」与学习通「功能类-电脑端登录自动确认」的修复仍被底座同名组挡住，合并结果与 v15 相同

其余十四个来源的版本与 v15 相同。

Lin-arm 实际并入（四条都在功能类，默认关闭，不会自动点击）：

- 软件包安装程序（`com.android.packageinstaller`）新增「功能类-确认[未查询到此应用的 ICP 核准信息]」（1 条）：安装页出现「未查询到此应用的 ICP 核准信息」时点「知道了」。快照 [34431696](https://i.gkd.li/i/34431696)
- 番茄免费小说新增「功能类-刷短剧时半自动[不喜听书]」（2 条）：需先手动长按小说标签里的视频，再点「不感兴趣」，然后选「不喜欢听书」。快照 [34419649](https://i.gkd.li/i/34419649)、[34419676](https://i.gkd.li/i/34419676)
- 抖音新增「功能类-自动开启[自动连播]」（3 条）：刚进入时对第一个视频长按；「自动连播」未开则打开，已开则按返回。快照 [34400931](https://i.gkd.li/i/34400931)、[34400219](https://i.gkd.li/i/34400219)、[34400216](https://i.gkd.li/i/34400216)
- 抖音极速版新增同名组（3 条）。快照 [34420783](https://i.gkd.li/i/34420783)、[34423078](https://i.gkd.li/i/34423078)、[34419001](https://i.gkd.li/i/34419001)、[34421280](https://i.gkd.li/i/34421280)

被底座挡住、未进入合并结果：

- X(推特)「分段广告-主页信息流广告」：Lin-arm 把 key 2 的「发帖选项」从只匹配 ImageView 放宽到 ImageView 或 Button，并补快照 [34428571](https://i.gkd.li/i/34428571)。同名组仍以 AIsouler 底座为准
- 学习通「功能类-电脑端登录自动确认」：Lin-arm 把层级改成区间深度，以免节点深度变化失效，并补快照 [34427110](https://i.gkd.li/i/34427110)。同名组仍以底座为准，选择器与 v15 相同

净变化：应用数不变，规则组 +4，规则 +9。全局组仍为 16。番茄免费小说、软件包安装程序、抖音、抖音极速版里，排在新组后面的既有规则组只是序号顺延，选择器未改。

## [15] - 2026-11-05

### 内容

对照 v14（1107 应用 / 5080 规则组 / 7895 规则 / 16 全局组），本版为 1107 应用 / 5083 规则组 / 7902 规则 / 16 全局组，订阅文件约 2.8 MB（2,855,932 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v624 → v625（2026-11-04）：蘑菇云开屏、学习通剪贴板提示、红果短剧通知权限、哔哩哔哩直播间抽奖弹窗、QQ 登录授权进入合并结果。支付宝「局部广告-卡片广告」与百度贴吧「全屏广告-弹窗广告」的修复仍被底座同名组挡住，合并结果与 v14 相同
- [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) v45 → v47（2026-11-04）：适配哔哩哔哩暂停广告的新按钮。v14 合并时该源已发布 dist 仍是 v45，本次补入

其余十三个来源的版本与 v14 相同。

Lin-arm 实际并入：

- QQ 新增「功能类-设备登录授权」（3 条）：在扫码登录页点「登录 / 确认」，并处理异常二次确认「允许登录QQ」。快照 [20737721](https://i.gkd.li/i/20737721)、[12789287](https://i.gkd.li/i/12789287)、[13063027](https://i.gkd.li/i/13063027)
- QQ 新增「功能类-App申请信息/登录授权」（3 条）：第三方申请使用 QQ 信息时点「同意 / 确认」，以及扫码登录页点「登录 / 确认」。快照 [20737673](https://i.gkd.li/i/20737673)、[22631619](https://i.gkd.li/i/22631619)、[20737651](https://i.gkd.li/i/20737651)、[20737675](https://i.gkd.li/i/20737675)
- 哔哩哔哩新增「功能类-直播间抽奖弹窗」（1 条）：在直播间关闭抽奖（福袋）结果。快照 [34363614](https://i.gkd.li/i/34363614)
- 蘑菇云手机「开屏广告」：关闭按钮的层级由固定 `>7` 改为 `>(n+5)`，补快照 [34367435](https://i.gkd.li/i/34367435)。开屏分类默认开启，这条会生效
- 学习通「通知提示-剪贴板内容已更新」：活动页补 `.webapp.ui.WebAppCommonViewer`，补快照 [34332781](https://i.gkd.li/i/34332781)
- 红果短剧（海外包 `com.phoenix.read.oversea.gp`）「权限提示-通知权限」：活动页补短剧播放页 `com.dragon.read.component.shortvideo.impl.ShortSeriesActivity`，补快照 [34348017](https://i.gkd.li/i/34348017)

上面三条新的功能类组，以及学习通、红果短剧的改动，所在分类默认关闭，不会自动点击。

GK-Lemon-D 实际并入（哔哩哔哩 `tv.danmaku.bili`，两组在 v14 已存在，规则本身未关闭，只在原规则里多一种按钮写法；全屏广告分类默认关闭）：

- 「全屏广告-视频暂停广告倒计时」：增加 `TextView[text="后将展示广告"] + @Button[text="取消"]`，与原有 TextView 版「取消」并列
- 「全屏广告-视频暂停广告」：增加 `@View[clickable=true] > [desc="关闭暂停页"] + Button`，与原有 `desc="close"` 版并列

净变化：应用数不变，规则组 +3，规则 +7。全局组仍为 16。规则条数按规则对象计，暂停广告两组是在原规则内追加选择器，不另计一条。

## [14] - 2026-11-04

### 内容

对照 v13（1105 应用 / 4995 规则组 / 7768 规则 / 16 全局组），本版为 1107 应用 / 5080 规则组 / 7895 规则 / 16 全局组，订阅文件约 2.8 MB（2,852,515 字节）。例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

版本有变化的来源：

- [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v623 → v624（2026-11-03）：橘汁、起点读书、荣耀应用市场三条进入合并结果。百度贴吧「权限提示-通知权限」的修复仍被更高优先级的同名组挡住，合并结果与 v13 相同
- [言木七](https://github.com/yanmuq/muqi_gkd) v53 → v54（2026-11-04）：按「限时 / 持续」重排规则名，并新增新浪财经。同名组仍以更高优先级来源为准；改名后与已有选择器完全相同的组会以新名字补入，但 `enable: false`，不会自动点击

其余十三个来源的版本与 v13 相同。

Lin-arm 实际并入、且默认开启：

- 新应用：橘汁（`com.asjdhjhd.mgd.p3`），规则组「全屏广告」（1 条）。点全屏广告上「立即下载」旁边的关闭图。快照 [34303867](https://i.gkd.li/i/34303867)
- 起点读书新增「全屏广告-追更至最新章节弹窗」（2 条）：先取消勾选更新提醒，再点关闭。快照 [34316607](https://i.gkd.li/i/34316607)、[34316605](https://i.gkd.li/i/34316605)
- 荣耀应用市场新增「功能类-自动[查看更多]应用更新」（1 条）：在更新管理页点「查看更多」，每个应用最多 3 次。快照 [34304183](https://i.gkd.li/i/34304183)

言木七实际并入：

- 新应用：新浪财经，规则组「限时-应用提示-取消安装确认」（1 条，默认关闭）。快照 [34300807](https://i.gkd.li/i/34300807)
- 35 个仅来自言木七的组被原样改名。其中 16 个仍默认开启（权限控制器的四条系统权限、以及支付宝、华为浏览器、淘宝、盒马、哔哩哔哩等的通知或更新提示）。另外 19 个由默认开启改为 `enable: false`，不再自动执行：铁路 12306 同意认证，华为主题开启通知，华为音乐会员弹窗，智慧生活首页横幅，京东还款免密，哈啰购卡，Edge 开启通知与评价，微软 Office 设为默认，美团付款后点完成与骑行支付，淘宝悬浮窗权限，云闪付信用卡广告、支付完成与开启通知，饿了么定位提示、调研卡片与订单通知，哔哩哔哩青少年弹窗
- 其余新增组默认关闭。其中 62 个的选择器已被更高优先级规则完整覆盖；14 个是原先没有的补充（华为系与网易云、淘宝、QQ、微博轻享版的开屏或更新提示，淘宝悬浮广告，QQ 腾讯文档「使用 App」弹窗，网易云「获得新徽章」等），需要在 GKD 里手动打开才会生效

净变化：应用 +2，规则组 +85，规则 +127。全局组仍为 16。

## [13] - 2026-11-03

### 内容

对照 v12（1105 应用 / 4994 规则组 / 7766 规则 / 16 全局组），本版为 1105 应用 / 4995 规则组 / 7768 规则 / 16 全局组，订阅文件约 2.8 MB（2,805,868 字节）。补做 11-03 例行合并，上游按各源已发布的 dist 拉取。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

版本有变化的来源：

- [少年阿鲲](https://github.com/Lin-arm/gkd-Rules) v122 → v123（2026-11-02）：起点读书两条「每日福利」组，默认仍关闭
- [火山虾](https://github.com/VolcanoSAhrimp/gkd-rule) v75 → v78（2026-11-03）：只新增哔哩哔哩播放页中间广告，其余改动被同名组或误触守卫挡住
- [YaChengMu 精简续更](https://github.com/YaChengMu/gkd_subscription_min) v152 → v153（2026-11-03）：改的是已有组（番茄免费小说、红果免费短剧、抖音、哔哩哔哩、淘宝、支付宝、HMS Core）。同名组仍以更高优先级来源为准，合并结果没有差异

其余十二个来源的版本与 v12 相同。[Lin-arm](https://github.com/Lin-arm/GKD_subscription) 主仓在 11-03 另有起点读书、百度贴吧、荣耀应用市场、橘汁的提交，但已发布的 `dist/gkd.json5` 仍是 v623（2026-10-31），这些提交还没进入订阅文件，本次未并入。

- 哔哩哔哩新增规则组「局部广告-视频播放页中间的广告」（2 条，默认关闭）：在视频详情页先点中间广告的关闭，再点「不想看该内容」。快照 [34298713](https://i.gkd.li/i/34298713)、[34299106](https://i.gkd.li/i/34299106)
- 起点读书「📆每日福利-天降福利弹窗」：按钮由只匹配「去浏览」改为「去浏览」或「去完成」，补了快照 [34250748](https://i.gkd.li/i/34250748)。组仍然关闭
- 起点读书「📆每日福利-自动去看广告」：点击间隔由 1.7 秒改为 2.5 秒。组仍然关闭

净变化：应用数不变，规则组 +1，规则 +2。全局组仍为 16。

## [12] - 2026-11-02

### 内容

对照 v11（1105 应用 / 4993 规则组 / 7761 规则 / 16 全局组），本版为 1105 应用 / 4994 规则组 / 7766 规则 / 16 全局组，订阅文件约 2.8 MB（2,805,180 字节）。十五个上游版本与 v11 相同，变更只在自有层。

喜马拉雅（`com.ximalaya.ting.android`）开屏不跳过：梦念逍遥 / 九千院留下的应用组「开屏广告」只有一条 `[text*="跳过"][text.length<10][visibleToUser=true]`。AIsouler / Lin-arm 已在 2025-04-15 删掉这组、改走全局开屏，但合并时低层同名组被补了回来。三条全局开屏都写了 `disableIfAppGroupMatch: '开屏广告'`，于是主版的全局开屏全部停用。剩下的那条规则点的是不可点击的倒计时文案 `xm_ad_host_count_down_text`（文案「跳过广告」），真正的热区是同位置可点击的 `xm_ad_host_count_down_click_lay`。依据 [AIsouler/GKD_subscription#1252](https://github.com/AIsouler/GKD_subscription/issues/1252) 的 MainActivity 快照（9.4.7.3，开屏盖在首页上，同时有摇一摇）。没有更新的设备快照，穿山甲 `tt_splash_skip_btn` 与极速版是否同资源名按现有全局规则和主版结构补上。

- 自有层覆写主版规则组「开屏广告」（key 25，`enable: true`）：点可点击热区，开屏容器内的兜底排除 `…_no_click_view` 和摇一摇热区，另补穿山甲跳过按钮。`ignoreGlobalGroupMatch: true`，全局开屏恢复生效。只在 `MainActivity` / `WelComeActivity` 上匹配自有热区，不改播放页、签到、通知等其它组
- 极速版（`com.ximalaya.ting.lite`）原先没有「开屏广告」组，全局开屏本来就会跑。新增同名组，同样 `ignoreGlobalGroupMatch: true`，避免把全局开屏关掉

净变化：应用数不变，规则组 +1，规则 +5。全局组仍为 16。局部广告、全屏广告、功能类默认仍关闭。

## [11] - 2026-11-01

### 内容

对照 v10（1104 应用 / 4990 规则组 / 7759 规则 / 16 全局组），本版为 1105 应用 / 4993 规则组 / 7761 规则 / 16 全局组，订阅文件约 2.8 MB。其余十四个来源的版本与 v10 相同，增量只来自 [Lin-arm](https://github.com/Lin-arm/GKD_subscription) v622 → v623。未改自有层。局部广告、全屏广告、功能类默认仍是关闭的。

- 新应用：(涂鸦)智能生活，2 个规则组、2 条规则（局部广告-轮播图、功能类-自动允许通断电）
- 红果短剧（海外包）新增规则组「全屏广告」，1 条规则
- 红果免费短剧：规则组由「功能类-自动[上滑]继续看短剧」（3 条）改为「功能类-[上滑]继续看短剧」（2 条），去掉一条 5 秒上滑

净变化：应用 +1，规则组 +3（新增 4 个、去掉 1 个），规则 +2。全局组仍为 16。

## [10] - 2026-10-31

### 内容

对照 v9（1094 应用 / 4909 规则组 / 7658 规则 / 15 全局组），本版为 1104 应用 / 4990 规则组 / 7759 规则 / 16 全局组，订阅文件约 2.8 MB。原有十个来源的合并结果与 v9 一致，增量全部来自下面五个新上游和一条自有全局规则。新上游优先级最低：同名组仍以底座和原有增量源为准，不会改写已有规则。

误触守卫会丢掉：选择器已被更高层完整覆盖的组、支付 / 登录 / 删除 / 签到领取 / 打开通知、信息流滑动与 `action=back`、过宽的开屏「跳过」、以及没有选择器的空组。非开屏分类默认仍是关闭的。

| 新增上游 | 版本 | 实际并入 |
| --- | --- | --- |
| [AIsouler 自用续订](https://github.com/AIsouler/gkd-subscription) | v121（2026-10-31） | 4 个应用、36 个规则组、45 条规则。新应用：唱吧、湖南农信、红果短剧（海外包）、公交 e 出行 |
| [火山虾](https://github.com/VolcanoSAhrimp/gkd-rule) | v75（2026-10-15） | 4 个应用、30 个规则组、39 条规则。新应用：猫耳 FM、MOMO 陌陌、电影猎手、莉景天气。补了一批青少年模式、更新提示和弹窗 |
| [GK-Lemon-D](https://github.com/LenorEric/GK-Lemon-D) | v45（2026-10-30） | 0 个应用、9 个规则组、9 条规则。补哔哩哔哩暂停广告、淘宝/闲鱼弹窗和若干通知权限关闭 |
| [YaChengMu 精简续更](https://github.com/YaChengMu/gkd_subscription_min) | v152（2026-10-27） | 2 个应用、3 个规则组、5 条规则。新应用：华为教育中心、WiFi 万能钥匙极速版 |
| [Ling](https://github.com/cjy0812/Ling033_GKD_Rules) | v15（2026-10-06） | 0 个应用、3 个规则组、3 条规则。美团外卖开屏与拼好饭弹窗、设置里的电子保修卡。抖音信息流滑动规则未并入 |
| 自有层 | — | 1 个全局组「弹窗广告-广告关闭按钮」：只点可见的 `vid=ad_close`，每个应用最多 1 次 |

### 未接入的候选

- 官方名单 [GKD_THS_List](https://github.com/Adpro-Team/GKD_THS_List) 里标为仍在维护的奥怪、甘霖、梦念逍遥、Mrlc 已在原有十源中。名单本身未再收录新的活跃订阅。
- 停更或归档：`gkd-kit/subscription`（2024-04 归档）、`CKylinMC/gkd-rule-extras`（2026-06，且含无长度限制的「跳过」）、`Tsuk1ko/gkd-subscription`（最后提交 2026-09-19，超过一个月）、`lisrain/GKD_subscription`（已归档）。
- 许可证或作者明确限制再分发：`BennettChina/gkd-subscription` 写明仅供本人使用。`yzl3014/gkd` 虽为 GPL-3.0，但是 AIsouler / 奥怪 / Lin-arm 的个人裁剪子集，作者写明不适合其他用户，独有组只有 3 个，没有接入。
- 质量不够或与现有源重复：`he0524/gkd-subscription`、`anransu983-sketch/gkd-rules`（无 star，约一半是选择器重复，后者还有空应用）、`gmyboy/GKDmy`（Lin-arm 镜像，只多 2 条且含自动上滑）、`myloveisxiao/gkd-subscription`（全局「跳过」过宽）、`K-S-D-M`、`H-xiaoH`、`mfd2033`、`rensss`（规模过小且缺少快照）。`jsllb1986`、`oklazeno`、`Reev3sX`、`dlzbm`、`jack98hao` 是已有上游的二次聚合，接入只会重复。

### 机制

- `scripts/merge.py` 改为从仓库根目录读写 `dist/` 与 `custom.json5`，缺快照时按 `SOURCES.url` 拉取；`--fetch` 强制刷新。无 `state.json` 时从已发布的 `dist` 回读版本和内容哈希，避免误把版本打回 1。
- 自有层新增 `globalGroups`，同名替换、新名追加。

## [9] - 2026-10-31

### 内容

- 每日增量合并：覆盖仍为 1094 个应用，规则组 4909（+1），规则 7658 条

## [3] - 2026-10-26

### 内容

- 规则来源由 2 个扩充到 10 个：新增奥怪、甘霖、梦念逍遥、Mrlc、Adpro、九千院、少年阿鲲、言木七
- 覆盖 1085 个应用、4879 个规则组、7619 条规则，全局规则组增至 15 个，订阅文件约 2.8 MB

### 机制

- 合并管线升级为多源版：优先级为自有层 > AIsouler 底座 > Lin-arm > 其余增量源（维护中优先、存量精选殿后）

## [2] - 2026-10-26

### 变更

- 订阅正式定名为「清净 · GKD 精选订阅」，主页与订阅文件同步更名；规则内容与 v1 一致

## [1] - 2026-10-26

首版发布。

### 内容

- 三层合并上线：AIsouler 最终版（v406）精选底座 + Lin-arm 每日增量 + 本仓自有层，冲突时高层优先
- 覆盖 988 个应用、2532 个规则组、3936 条规则，订阅文件约 1.4 MB
- 合并后自动校验：格式回读解析、应用去重、规则组序号唯一

### 机制

- 每日自动拉取增量、合并、校验、升版、推送
- GKD 通过版本小文件（`dist/gkd.version.json5`）检查更新，省流量
- 用户反馈的漏跳与误触经自有层逐条精修，随每日更新推送
