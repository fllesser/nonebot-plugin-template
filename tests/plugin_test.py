from time import time

from nonebug import App
import pytest

from nonebot.adapters.onebot.v11 import Message, MessageEvent
from nonebot.adapters.onebot.v11.event import Sender


@pytest.mark.asyncio
async def test_pip(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

    driver = nonebot.get_driver()
    driver.register_adapter(OnebotV11Adapter)
    from nonebot_plugin_template import pip

    event = MessageEvent(
        time=int(time()),
        sub_type="friend",
        self_id=123456,
        post_type="message",
        message_type="private",
        message_id=123456,
        user_id=123456,
        message=Message("pip install nonebot2"),
        original_message=Message("pip install nonebot2"),
        raw_message="pip install nonebot2",
        sender=Sender(),
        font=123456,
    )

    async with app.test_matcher(pip) as ctx:
        bot = ctx.create_bot()
        ctx.receive_event(bot, event)

        ctx.should_call_send(event, Message("nonebot2"), result=None)
        ctx.should_finished(pip)
