<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ nonebot-plugin-template ✨
[![python](https://img.shields.io/badge/python-3.10|3.11|3.12|3.13|3.14-blue.svg)](https://www.python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv)](https://github.com/astral-sh/uv)
<br/>
[![ruff](https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![pre-commit](https://results.pre-commit.ci/badge/github/fllesser/nonebot-plugin-template/master.svg)](https://results.pre-commit.ci/latest/github/fllesser/nonebot-plugin-template/master)
[![codecov](https://codecov.io/gh/fllesser/nonebot-plugin-template/graph/badge.svg?token=TMR6QZ6C6I)](https://codecov.io/gh/fllesser/nonebot-plugin-template)

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

`bump-my-version` 和 `poethepoet` 在 dev 依赖组中，使用 `uv sync` 安装，或者使用 `uv tool install` 全局安装

    uv run poe bump patch

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
> pre-commit / prek 使用方法

<details>
<summary>提交前检查</summary>

安装 `pre-commit`

    uv tool install pre-commit

或安装 `prek` (推荐)

On `Linux` / `macOS`:

    curl --proto '=https' --tlsv1.2 -LsSf https://github.com/j178/prek/releases/download/v0.2.13/prek-installer.sh | sh
On `Windows`:

    powershell -ExecutionPolicy ByPass -c "irm https://github.com/j178/prek/releases/download/v0.2.13/prek-installer.ps1 | iex"
安装钩子

    pre-commit install

    prek install
添加到暂存区

    git add <待提交文件>

仓库地址: 
- [`prek`](https://github.com/j178/prek)
</details>
