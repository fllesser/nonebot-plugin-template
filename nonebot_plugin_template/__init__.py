from nonebot import (
    require,
    get_driver, # @get_driver().on_startup 装饰启动时运行函数
    get_bots    # dict[str, BaseBot]
)
from nonebot.log import logger
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

__plugin_meta__ = PluginMetadata(
    name="名称",
    description="描述",
    usage="用法",
    type="application", # library
    homepage="https://github.com/fllesser/nonebot-plugin-",
    supported_adapters={ "~onebot.v11" }
)

