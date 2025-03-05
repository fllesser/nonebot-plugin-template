from arclet.alconna import Alconna, Args, Option, Subcommand
from nonebot_plugin_alconna import on_alconna

alc = Alconna(
    "pip",
    Subcommand(
        "install",
        Args["package", str],
        Option("-r|--requirement", Args["file", str]),
        Option("-i|--index-url", Args["url", str]),
    ),
)

on_alconna(alc)
