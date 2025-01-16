from nonebot import (
    require,  # noqa: F401
    get_driver,  # @get_driver().on_startup 装饰启动时运行函数  # noqa: F401
    get_bots,  # dict[str, BaseBot] 常用于定时器获取 BOT 对象  # noqa: F401
)
from nonebot.plugin import (
    PluginMetadata,
    inherit_supported_adapters
)

require("nonebot_plugin_uninfo")
require("nonebot_plugin_alconna")
require("nonebot_plugin_localstore")
require("nonebot_plugin_apscheduler")

from .config import Config  # noqa: E402


__plugin_meta__ = PluginMetadata(
    name="名称",
    description="描述",
    usage="用法",
    type="application",  # library
    homepage="https://github.com/用户名/nonebot-plugin-",
    config=Config,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_uninfo"
    ),
    # supported_adapters={"~onebot.v11"},
    extra={"author": "fllesser <fllessive@gmail.com>"},
)
