from pydantic import BaseModel

from nonebot import get_driver, get_plugin_config


class Config(BaseModel):
    pass


# 配置加载
plugin_config: Config = get_plugin_config(Config)
global_config = get_driver().config

# 全局名称
NICKNAME: str | None = next(iter(global_config.nickname), None)
