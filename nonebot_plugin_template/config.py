from nonebot import (
    get_driver, 
    require, 
    get_plugin_config
)
from pydantic import BaseModel
from pathlib import Path
from typing import List, Literal, Optional

require("nonebot_plugin_localstore")
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
import nonebot_plugin_localstore as store

class Config(BaseModel):
    pass

cache_dir: Path = store.get_plugin_cache_dir()
config_dir: Path = store.get_plugin_config_dir()
data_dir: Path = store.get_plugin_data_dir()

# 配置加载
config: Config = get_plugin_config(Config)
gconfig = get_driver().config

# 全局名称
NICKNAME: str = next(iter(gconfig.nickname), "")
