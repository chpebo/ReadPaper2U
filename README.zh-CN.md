# ReadPaper2U

[English](./README.md) · **简体中文** · [한국어](./README.ko.md)

> 把学术论文变成视觉小说 (visual novel) 风格的对话伴读。

ReadPaper2U 是一个单文件的网页应用，可将一篇 PDF 学术论文转换为一段
可对话的阅读体验。一位可自定义的伴读角色会以视觉小说式的剧本，逐
轮带你读完全文；读完之后，可以在 Q&A 面板继续追问。文中的公式、图
表会被即时渲染或摘要，所有对话状态保存在本地。

整个应用就是一份 `index.html`，无需构建步骤，任何静态文件服务器都
能托管。

应用内嵌了一份首次运行体验用的 demo（Attention Is All You Need，
完全离线、无需配置 API），无论是否准备好接入模型，都可以先试一遍
完整的阅读流程。

---

## 功能

- **浏览器内解析 PDF**——通过 PDF.js 在客户端解析论文；同时支持
  arXiv 链接。
- **视觉小说模式**——将论文内容改写为伴读角色逐轮讲述的对白脚本。
- **Q&A 模式**——视觉小说读完之后，针对论文内容向模型继续追问。
- **内嵌离线 demo**——上传页提供一键加载的演示（Attention Is All
  You Need），预置中 / 英 / 韩三种语言版本，完整呈现阅读体验，
  全程不需要配置 API。
- **剧本翻译 (script translation)**——当当前剧本语言与界面语言不
  匹配时，可以一键（或通过自动询问）将整份剧本逐场景翻译为当前
  界面语言，结果会自动覆盖保存。
- **思维导图 (mind map)**——一键基于对话脚本生成论点结构图，并支持
  导出为 SVG / PNG，方便嵌入笔记或幻灯片。
- **图表处理**——四档可选：关闭、仅图注、由视觉模型生成描述、或
  将图描述内嵌进对白。
- **公式渲染**——LaTeX 公式由 KaTeX 渲染。
- **多语言**——界面与对白支持简体中文、英文、韩文。
- **明暗主题 (light & dark themes)**——可在设置中切换，也可通过顶部
  栏的图标快捷切换，二者共用同一套 CSS 变量体系。
- **键盘快捷键 (keyboard shortcuts)**——下一句 / 上一句、自动播放、
  对话历史，以及一个快捷键速查面板（按 `?` 可随时调出）。
- **自适应自动播放 (adaptive auto-play)**——每个场景的停留时间会根据
  其文本长度与脚本的主导文字（CJK 字符 / 分钟 vs. 拉丁单词 / 分钟）
  自动调整：短旁白快速推进，长解释留出足够阅读时间。
- **情绪相关的角色动画 (emotion-specific character animations)**——
  伴读角色立绘会根据对白情绪做出细微的动态反馈。
- **持久存档**——对话状态保存在 IndexedDB；可选通过
  File System Access API 导出到本地文件夹。
- **黑板栏**——侧边栏持续追踪关键术语 (terminology)、公式与论证脉络。
- **自带 LLM 端点**——任何 OpenAI 兼容的 chat completion 接口
  (DeepSeek、OpenAI、Moonshot/Kimi 等) 均可。API key 仅保存在浏览器
  `localStorage`，并直接发往你所配置的端点。

---

## 灵感来源与差异

ReadPaper2U 是受 [Paper2Gal](https://paper2gal.com/) 启发的一次部分复现，
后者是一款将论文转换为 Galgame 风格视觉小说的网页应用。两个项目的核心
想法一致 (用一位陪伴角色带读论文)。ReadPaper2U 的取向更偏功能性，不再
锚定在 ACG 文化之上，具体差异有三处：

- **开源、本地运行。** ReadPaper2U 以 MIT 协议发布，本体只是一份静态
  HTML 文件。没有需要注册的服务，没有调用上限，浏览器与 LLM 之间也不
  存在任何代理。文件会把请求直接发往用户所配置的 OpenAI 兼容端点。
- **"陪伴角色"的覆盖面更宽。** 角色编辑器暴露了 12 个维度 (种族、外观、
  能量水平、语气正式度、幽默风格、招牌口癖、擅长领域，以及四种分段
  讲解策略)。默认头像是作者自家猫的照片。ACG 风格的角色当然能用，导师、
  同事、虚构研究者、宠物等同样适用。项目并不锚定在某一种美学传统上。
- **能"看图"的阅读。** 当用户配置了视觉模型 (vision-capable model) 时，
  应用既可以一次性地为每张图生成简短描述并注入对白，也可以在脚本生成
  调用中直接把图像本身一并喂给模型。文本模型场景或希望控制成本时，仅
  展示图注或完全关闭抽图也是可选项。

ReadPaper2U 当前不包含的部分：背景音乐 (BGM)、语音合成、内建立绘委托。
视觉小说仅运行在文字与一张静态立绘之上。

---

## 快速开始

应用本体是一份 HTML 文件。最简单的方式是通过本地静态服务器打开
（File System Access API 与 PDF.js worker 都偏好 `http://` 而非
`file://`）：

```bash
# Python 3 (任意平台)
python -m http.server 8765
# 然后访问 http://localhost:8765
```

首次打开会停留在主页。可以先点 START 进入上传页，在上传页中部的
"看看 demo：Attention Is All You Need"卡片可一键加载一份预置的
32 个场景的演示剧本，**整个过程不需要配置 API**。

要读自己的论文时，点开**设置**（右上角齿轮图标或主页的 SETTINGS
按钮），填入以下三项：

1. **API 基础地址 (base URL)**——例如 `https://api.deepseek.com/v1`、
   `https://api.openai.com/v1`，或任一 OpenAI 兼容端点。
2. **模型名称**——例如 `deepseek-chat`、`gpt-4o-mini` 等。
3. **API key**——仅保存在当前设备的 `localStorage` 中。

填好之后将 PDF 拖入上传区，或粘贴一个 arXiv 链接。

### 离线 / 内网环境

默认情况下，PDF.js、KaTeX 以及 Mermaid（仅在生成思维导图时加载）
从公共 CDN（`cdnjs.cloudflare.com`、`cdn.jsdelivr.net`）加载。当 CDN
不可达时，应用会回退到本地 `lib/` 目录。若要完全离线使用，请将以下
文件放置在 `index.html` 同级：

```
lib/
├── pdf.min.js
├── pdf.worker.min.js
├── mermaid.min.js              # 仅思维导图功能需要
└── katex/
    ├── katex.min.js
    ├── katex.min.css
    └── fonts/...
```

内嵌 demo 完全离线运行，不依赖上述任何文件（它既不解析 PDF，也不
渲染思维导图）。

具体文件可从 PDF.js、KaTeX 与 Mermaid 的官方发布版获取，详见
[THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。

---

## 隐私

应用完全运行在浏览器内。具体而言：

- PDF 在本地解析；解析得到的文本会随聊天补全请求 (chat completion
  request) 发送到**你所配置的** LLM 端点。
- API key 不会离开浏览器，仅出现在向你所配置端点发出的请求的
  `Authorization` 头中。
- 存档保存在浏览器的 IndexedDB 中（也可选择导出到你指定的文件夹）。
- 内嵌 demo 不发起任何网络请求。

上传**未发表**的论文稿件之前，请先确认所选 LLM 服务商的数据保留与
训练用途条款。

---

## 项目结构

```
readpaper2u/
├── index.html              # 应用本体
├── banni.png               # 默认伴读角色头像
├── find-section.py         # 节标记导航脚本
├── process_avatar.py       # 一次性工具：HEIC 照片 → 抠图 PNG
├── LICENSE
├── README.md               # 英文 README
├── README.zh-CN.md         # 本文件
├── README.ko.md            # 韩文 README
├── CHANGELOG.md
├── CONTRIBUTING.md
├── THIRD_PARTY_NOTICES.md
├── requirements.txt        # 仅供 process_avatar.py 使用
└── .gitignore
```

`index.html` 刻意保持单文件结构。导航此文件所用的节标记
(section marker) 系统及其辅助脚本说明，参见
[CONTRIBUTING.md](./CONTRIBUTING.md)。

---

## 辅助脚本

### `find-section.py`

列出、筛选、并重新生成嵌入在 `index.html` 顶部的目录块。仅依赖
Python 标准库，无需额外安装。

```bash
python find-section.py                # 列出 CSS 与 JS 中的所有节
python find-section.py --name api     # 按子串筛选
python find-section.py --update-toc   # 就地重写目录块
```

### `process_avatar.py`

一次性工具，将 HEIC 照片处理成抠图、裁剪、带 alpha 通道的 PNG，
适合用作伴读角色头像。仅在你想替换头像时才需要；仓库内自带的
`banni.png` 可直接使用。

```bash
pip install -r requirements.txt
# 修改脚本顶部的 SRC 与 DST 常量后运行：
python process_avatar.py
```

---

## 许可证

本项目以 MIT License 发布。详见 [LICENSE](./LICENSE)。

默认伴读头像 `banni.png` 是作者拍摄的自家猫的原创照片，同样以
MIT 许可证发布。运行时加载的第三方库 (PDF.js、KaTeX、Mermaid) 各自
适用其原始许可，详见 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。

---

## 致谢

构建于 [PDF.js](https://mozilla.github.io/pdf.js/)（Apache 2.0）、
[KaTeX](https://katex.org/)（MIT）与
[Mermaid](https://mermaid.js.org/)（MIT）之上。LLM 推理由你所配置的
OpenAI 兼容端点完成。Banni（默认伴读角色）是一只真实存在的猫。
