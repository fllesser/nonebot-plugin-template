<div align="center">
    <a href="https://v2.nonebot.dev/store">
    <img src="https://raw.githubusercontent.com/fllesser/nonebot-plugin-template/refs/heads/resource/.docs/NoneBotPlugin.svg" width="310" alt="logo"></a>

## ✨ {plugin-name} ✨

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/{owner}/{plugin-name}.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/{plugin-name}">
    <img src="https://img.shields.io/pypi/v/{plugin-name}.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">
<a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/badge/code%20style-ruff-black?style=flat-square&logo=ruff" alt="ruff">
</a>
<a href="https://github.com/astral-sh/uv">
    <img src="https://img.shields.io/badge/package%20manager-uv-black?style=flat-square&logo=uv" alt="uv">
</a>
<a href="https://results.pre-commit.ci/latest/github/{owner}/{plugin-name}/master">
    <img src="https://results.pre-commit.ci/badge/github/{owner}/{plugin-name}/master.svg" alt="pre-commit" />
</a>
</div>

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install {plugin-name} --upgrade
使用 **pypi** 源安装

    nb plugin install {plugin-name} --upgrade -i "https://pypi.org/simple"
使用**清华源**安装

    nb plugin install {plugin-name} --upgrade -i "https://pypi.tuna.tsinghua.edu.cn/simple"


</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details open>
<summary>uv</summary>

    uv add {plugin-name}
安装仓库 master 分支

    uv add git+https://github.com/{owner}/{plugin-name}@master
</details>

<details>
<summary>pdm</summary>

    pdm add {plugin-name}
安装仓库 master 分支

    pdm add git+https://github.com/{owner}/{plugin-name}@master
</details>
<details>
<summary>poetry</summary>

    poetry add {plugin-name}
安装仓库 master 分支

    poetry add git+https://github.com/{owner}/{plugin-name}@master
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>

<details>
<summary>使用 nbr 安装(使用 uv 管理依赖可用)</summary>

[nbr](https://github.com/fllesser/nbr) 是一个基于 uv 的 nb-cli，可以方便地管理 nonebot2

    nbr plugin install {plugin-name}
使用 **pypi** 源安装

    nbr plugin install {plugin-name} -i "https://pypi.org/simple"
使用**清华源**安装

    nbr plugin install {plugin-name} -i "https://pypi.tuna.tsinghua.edu.cn/simple"

</details>


## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项  | 必填  | 默认值 |   说明   |
| :-----: | :---: | :----: | :------: |
| 配置项1 |  是   |   无   | 配置说明 |
| 配置项2 |  否   |   无   | 配置说明 |

## 🎉 使用
### 指令表
| 指令  | 权限  | 需要@ | 范围  |   说明   |
| :---: | :---: | :---: | :---: | :------: |
| 指令1 | 主人  |  否   | 私聊  | 指令说明 |
| 指令2 | 群员  |  是   | 群聊  | 指令说明 |

### 🎨 效果图
如果有效果图的话
