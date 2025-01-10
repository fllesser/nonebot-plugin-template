from nonebot import (
    require,
    get_driver, # @get_driver().on_startup 装饰启动时运行函数
    get_bots    # dict[str, BaseBot] 常用于定时器获取 BOT 对象
)
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
from .matcher import *

from .config import Config


__plugin_meta__ = PluginMetadata(
    name="名称",
    description="描述",
    usage="用法",
    type="application", # library
    homepage="https://github.com/用户名/nonebot-plugin-",
    supported_adapters={ "~onebot.v11" } # None 表示全适配器
)

