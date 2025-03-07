<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="./.docs/NoneBotPlugin.svg" width="300" alt="logo"></a>
</div>

### ✨ 使用方法
1. 点击 [创建仓库](https://github.com/new?template_owner=fllesser&template_name=nonebot-plugin-template&owner=%40me&name=nonebot-plugin-&visibility=public), 输入仓库名即可
2. ⚠️ **重要：**前往仓库 `Settings` -> `Actions` -> `General` -> 最下方 `Workflow permissions`, 勾选 `Read and write permissions`，然后点击 `Save` 按钮
3. 在 `Add file` 菜单中选择 `Create new file`, 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 `Choose a license template` 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支(这会触发一个工作流，根据仓库名称生成新的 `README`，更新 `pyproject.toml` 等文件中的插件名称)

> [!NOTE]
> 模板库中自带了一个发布工作流, 你可以使用此工作流自动发布你的插件到 pypi

<details>
<summary>配置发布工作流</summary>

1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，打开 [Actions secrets and variables](./settings/secrets/actions) 页面。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

</details>

<details>
<summary>触发发布工作流</summary>
从本地推送任意 tag 即可触发。

创建 tag:

    git tag v*

推送本地所有 tag:

    git push origin --tags

</details>

> [!IMPORTANT]
> 不会使用 uv ？

<detail>
<summary>不会看文档去</summary>
首先安装 [uv](https://astral.sh/blog/uv)

windows:

    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
curl:

    curl -LsSf https://astral.sh/uv/install.sh | sh
pip:

    pip install uv
安装所有依赖(自动创建 venv 虚拟环境, -p 指定 python 版本):

    uv sync --all-groups -p 3.12

[uv 文档](https://astral.sh/blog/uv)
</detail>

> [!NOTE]
> pre-commit 使用方法

<details>
<summary>使用 nonemoji 为 commit message 添加 emoji 前缀 </summary>

安装所有依赖(自动创建虚拟环境, -p 指定 python 版本)

    uv sync --all-groups -p 3.12
安装 `pre-commit`

    pre-commit install
添加到暂存区

    git add <待提交文件>
使用 `nonemoji` 编辑 `commit message` 并**提交**

    nonemoji

仓库地址: [nonemoji](https://github.com/nonebot/nonemoji)
</details>
