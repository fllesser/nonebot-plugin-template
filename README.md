<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="./.docs/NoneBotPlugin.svg" width="300" alt="logo"></a>
</div>

> [!IMPORTANT]
> 使用模版创建仓库

1. 点击 [创建仓库](https://github.com/new?template_owner=fllesser&template_name=nonebot-plugin-template&owner=%40me&name=nonebot-plugin-&visibility=public)
2. 前往仓库 Settings -> Actions -> General -> Workflow permissions, 勾选 Read and write permissions，然后点击 "Save" 按钮
3. 在创建好的新仓库中, 在 "Add file" 菜单中选择 "Create new file", 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 "Choose a license template" 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支, 这会触发一个工作流，根据你的仓库名称生成 Readme，更改插件名

> [!NOTE]
> 模板库中自带了一个发布工作流, 你可以使用此工作流自动发布你的插件到 pypi

<details>
<summary>配置发布工作流</summary>

1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，打开 [Actions secrets and variables](./settings/secrets/actions) 页面。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

</details>

> [!IMPORTANT]
> 这个发布工作流需要 pyproject.toml 文件, 并且只支持 [PEP 621](https://peps.python.org/pep-0621/) 标准的 pyproject.toml 文件

<details>
<summary>触发发布工作流</summary>
从本地推送任意 tag 即可触发。

创建 tag:

    git tag v*

推送本地所有 tag:

    git push origin --tags

</details>

> [!NOTE]
> pre-commit 食用方法

<details>
<summary>使用 nonemoji 规范 commit msg </summary>

安装所有依赖:

    uv sync --all-groups

安装 pre-commit

    pre-commit install

测试提交

    nonemoji

</details>



