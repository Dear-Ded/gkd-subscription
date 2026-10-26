<div align="center">

# ✨ Dear-Ded 精选 GKD 订阅

**集百家之所长 · 每日自动合并维护的 GKD 规则订阅**

精选底座打底 + 全网增量补齐 + 自有规则精修 —— 只为真的好用

[![订阅版本](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FDear-Ded%2Fgkd-subscription%2Fmain%2Fdist%2Fgkd.version.json5&query=%24.version&label=%E8%AE%A2%E9%98%85%E7%89%88%E6%9C%AC&color=blue)](https://github.com/Dear-Ded/gkd-subscription)
[![更新方式](https://img.shields.io/badge/%E6%9B%B4%E6%96%B0-%E6%AF%8F%E6%97%A5%E8%87%AA%E5%8A%A8-brightgreen)](https://github.com/Dear-Ded/gkd-subscription)
[![GKD 官网](https://img.shields.io/badge/GKD-gkd.li-orange)](https://gkd.li)

</div>

---

## 📥 订阅地址

```
https://raw.githubusercontent.com/Dear-Ded/gkd-subscription/main/dist/gkd.json5
```

**添加方法**：打开 GKD → 订阅 → 右上角 **+** → 粘贴上方地址 → 保存。之后 GKD 会每日自动检查更新，无需再管。

| 指标 | 首版数据（v1） |
| --- | --- |
| 覆盖应用 | 988 个 |
| 规则组 | 2532 个 |
| 规则条数 | 3936 条 |
| 文件大小 | 约 1.4 MB |

## 🧩 规则从哪来：三层合并

| 层级 | 来源 | 角色 |
| --- | --- | --- |
| 🥇 精选底座 | [AIsouler/GKD_subscription](https://github.com/AIsouler/GKD_subscription) 最终版（v406，已停更） | 人工精选、克制准确，冲突时以它为准 |
| 🥈 每日增量 | [Lin-arm/GKD_subscription](https://github.com/Lin-arm/GKD_subscription) | 仍在每日更新，补底座没有的新应用、新规则组 |
| 🥉 自有层 | 本仓库 `custom.json5` | 针对反馈逐条精修：补漏跳、修误触、禁用坏规则，优先级最高 |

合并原则：**同应用同名规则组只保留一份，高层优先**；低层独有的应用与规则组自动补入并重排序号；每日合并后自动校验（格式、重复、序号冲突），内容有变化才递增版本号推送。

## 🎯 精选标准

- **准**：底座是社区公认的精选集，误触率低，不为凑数堆规则
- **鲜**：停更底座缺的新应用、新版界面规则，由每日增量补上
- **修**：用户反馈的漏跳与误触进入自有层逐条修，不等上游
- **稳**：版本号单调递增，`checkUpdateUrl` 只拉一个小文件，检查更新不费流量

## 🐞 反馈与共建

遇到**漏跳**（广告没跳过）或**误触**（点错地方），请开 [Issue](https://github.com/Dear-Ded/gkd-subscription/issues)：

1. 注明应用名与出问题的场景（如「XX 开屏广告没跳」）
2. **附上 GKD 快照链接**（在 GKD 里对出问题界面保存快照并分享，得到 i.gkd.li 链接）——有快照，规则能照着界面节点精确写，修复最快
3. 维护者会把修复写进自有层，随下一次每日更新推送给所有人

## 🙏 致谢与说明

本仓库是对社区优秀订阅的**聚合再维护**，规则著作权归原作者及各贡献者所有：

- [AIsouler/GKD_subscription](https://github.com/AIsouler/GKD_subscription) —— 精选底座，感谢作者多年的维护（已归档停更）
- [Lin-arm/GKD_subscription](https://github.com/Lin-arm/GKD_subscription) —— 每日增量来源
- [GKD](https://github.com/gkd-kit/gkd) 本体与所有规则贡献者

如原作者对聚合方式有异议，请开 Issue 联系，将立即处理。

## ⚠️ 免责声明

本订阅仅供无障碍自动化操作辅助与学习交流使用。应用界面改版可能导致个别规则失效或误触，使用前请自行判断，风险自担。

---

<div align="center">
每日自动维护 · 有问题请提 Issue 附快照
</div>
