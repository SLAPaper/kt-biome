# web_fetch / web_search 网络可用性调查

**调查日期**: 2025-06-23  
**调查人**: general creature  
**状态**: 已验证

---

## 环境

- Windows 物理机，WiFi (Intel AC-9260)，IP 192.168.0.11
- curl 8.19.0 (mingw32)
- DNS 正常；出站 HTTP 受 GFW 影响

## web_fetch

| 条件 | 国内站 (baidu/bilibili/zhihu) | 海外非墙站 (api.github.com/jsonplaceholder) | 被墙站 (google.com/duckduckgo.com) |
|------|------|------|------|
| 无代理 | 可用 | 可用 | **失败** |
| 有代理 | 可用 | 可用 | 可用 |

## web_search

参数: `query`(必填), `max_results`(默认10), `region`(如 `us-en`, `zh-cn`)

### 后端引擎

1. **DuckDuckGo HTML** (默认) — 无代理时超时失败，有代理时可用
2. **Yahoo Search** — 无代理时可通过 `region="us-en"` 路由到此后端并成功返回

### 可用性矩阵

| 条件 | 默认后端 (DuckDuckGo) | region="us-en" (Yahoo) | region="zh-cn" |
|------|------|------|------|
| 无代理 | **超时失败** | 可用 | 超时失败 |
| 有代理 | 可用 | 可用 | 可用 |

### 无代理临时方案

指定 `region="us-en"` 走 Yahoo 后端绕过 DuckDuckGo 封锁。

## 根因

GFW 封锁 DuckDuckGo、Google 等站点。工具的 HTTP 请求走系统代理设置，无代理时被墙站点不可达。开启系统代理后两个工具完全正常。

## 使用建议

- 无代理时: web_fetch 正常用于国内和非墙海外站；web_search 需加 `region="us-en"`
- 有代理时: 两个工具全部功能正常
- 确认系统代理状态后再选择策略
