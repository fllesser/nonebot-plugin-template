from nonebot.log import logger
from nonebot.rule import Rule

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import on_alconna
from arclet.alconna import (
    Alconna,
    Args,
    Subcommand, 
    Option
)

alc = Alconna(
    "pip",
    Subcommand(
        "install",
        Args["package", str],
        Option("-r|--requirement", Args["file", str]),
        Option("-i|--index-url", Args["url", str]),
    )
)


from nonebot.plugin.on import (
    on_command,
    on_message,
)
from nonebot.adapters.onebot.v11 import (
    Bot, 
    MessageEvent, 
    GroupMessageEvent
)
