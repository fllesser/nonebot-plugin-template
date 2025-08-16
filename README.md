<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ nonebot-plugin-template ✨

<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff" alt="ruff">
</a>
<a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv" alt="uv">
</a>
</div>

> [!IMPORTANT]
> **收藏项目** 以便创建插件仓库～⭐️

<img width="100%" src="https://starify.komoridevs.icu/api/starify?owner=fllesser&repo=nonebot-plugin-template" alt="starify" />

### 🎉 快速开始

1. 点击 [创建仓库](https://github.com/new?template_owner=fllesser&template_name=nonebot-plugin-template&owner=%40me&name=nonebot-plugin-&visibility=public)
2. **⚠️ 重要:** 前往仓库 `Settings` -> `Actions` -> `General` -> 最下方 `Workflow permissions`, 勾选 `Read and write permissions`，然后点击 `Save` 按钮
3. 在 `Add file` 菜单中选择 `Create new file`, 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 `Choose a license template` 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支(这会触发一个工作流，生成新的 `README`，并修改 `pyproject.toml` 等文件中的插件名称)

> [!NOTE]
> 模板库中自带了一个 Release 工作流, 你可以使用此工作流发布你的插件到 PyPI

<details>
<summary>配置 PyPI Trusted Publisher</summary>
配置文档: https://docs.pypi.org/trusted-publishers/adding-a-publisher/ 

 - PyPI Project Name: nonebot-plugin-template
 - Owner: Your GitHub username
 - Repository name: nonebot-plugin-template
 - Workflow name: release.yml
 - Environment name: release

</details>

<details>
<summary>使用 bump-my-version 工具更新版本号，并触发 Release 工作流 (推荐)</summary>

`bump-my-version` 在 dev 依赖组中，使用 `uv sync --all-groups` 安装，或者使用 `uv tool install bump-my-version` 全局安装

    bump-my-version bump patch

该操作会有以下行为:
1. 更新 `pyproject.toml` 中 `project.version` 和 `tool.bumpversion.current_version`
2. 更新 `uv.lock` 中的版本号
3. 创建一个带 `tag` 的提交, 提交信息可以在 `pyproject.toml` 中的 `[tool.bumpversion]` 中配置

接下来你只需要推送提交，并推送 `tag` (git push origin --tags) 即可触发 Release 工作流

</details>

<details>
<summary>触发 Release 工作流 (手动)</summary>

更新版本号 

    uv version --bump patch
    
possible values: major, minor, patch, stable, alpha, beta, rc, post, dev

提交并推送...

从本地推送任意 `tag` 即可触发。

创建 `tag`:

    git tag v*

推送本地所有 `tag`:

    git push origin --tags

</details>

> [!IMPORTANT]
> 不会使用 uv ？

<details>
<summary>不会看文档去</summary>

<details>
<summary>安装 uv </summary>

`windows`:

    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
`curl`:

    curl -LsSf https://astral.sh/uv/install.sh | sh
`pipx`:

    pipx install uv
    
</details>

安装所有依赖(自动创建 `venv` 虚拟环境, `-p` 指定 `python` 版本):

    uv sync --all-groups -p 3.12
添加其他依赖, 例如 `koishi`(bushi

    uv add koishi
[uv 文档](https://astral.sh/blog/uv)
</details>

> [!NOTE]
> pre-commit 使用方法

<details>
<summary>使用 nonemoji 为 commit message 添加 emoji 前缀 </summary>

安装 `nonemoji`

    uv tool install nonemoji
安装 `pre-commit`

    uv tool install pre-commit

    pre-commit install
添加到暂存区

    git add <待提交文件>
使用 `nonemoji` 编辑 `commit message` 并**提交**

    nonemoji

仓库地址: [nonemoji](https://github.com/nonebot/nonemoji)
</details>
