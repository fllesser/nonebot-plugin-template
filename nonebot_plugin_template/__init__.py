from nonebot import logger, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_uninfo")
require("nonebot_plugin_alconna")
require("nonebot_plugin_localstore")
require("nonebot_plugin_apscheduler")
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="名称",
    description="描述",
    usage="用法",
    type="application",  # library
    homepage="https://github.com/owner/nonebot-plugin-template",
    config=Config,
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna", "nonebot_plugin_uninfo"),
    # supported_adapters={"~onebot.v11"},
    extra={"author": "owner <your@mail.com>"},
)

from arclet.alconna import Alconna, Args, Arparma, Option, Subcommand
from nonebot_plugin_alconna import on_alconna
from nonebot_plugin_alconna.uniseg import UniMessage

alc = Alconna(
    "pip",
    Subcommand(
        "install",
        Args["package", str],
        Option("-r|--requirement", Args["file", str]),
        Option("-i|--index-url", Args["url", str]),
    ),
)


pip = on_alconna(alc)


@pip.handle()
async def _(result: Arparma):
    package: str = result.other_args["package"]
    logger.info(f"installing {package}")
    await UniMessage.text(package).send()
