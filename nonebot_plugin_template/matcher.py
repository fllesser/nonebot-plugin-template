from nonebot_plugin_alconna import on_alconna  # noqa: F401
from arclet.alconna import (
    Args,
    Alconna,
    Option,
    Subcommand
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
