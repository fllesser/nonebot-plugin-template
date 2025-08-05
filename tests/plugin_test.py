from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, Message
from nonebug import App
import pytest


def make_onebot_event(message: Message) -> GroupMessageEvent:
    from random import randint
    from time import time

    from nonebot.adapters.onebot.v11.event import Sender

    message_id = randint(1000000000, 9999999999)
    user_id = randint(1000000000, 9999999999)
    group_id = randint(1000000000, 9999999999)

    event = GroupMessageEvent(
        time=int(time()),
        sub_type="normal",
        self_id=123456,
        post_type="message",
        message_type="group",
        message_id=message_id,
        user_id=user_id,
        group_id=group_id,
        raw_message=message.extract_plain_text(),
        message=message,
        original_message=message,
        sender=Sender(user_id=user_id, nickname="TestUser"),
        font=123456,
    )
    return event


@pytest.mark.asyncio
async def test_pip(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

    event = make_onebot_event(Message("pip install nonebot2"))
    try:
        from nonebot_plugin_template import pip
    except ImportError:
        pytest.skip("nonebot_plugin_template.pip not found")

    async with app.test_matcher(pip) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, Message("nonebot2"), result=None, bot=bot)
        ctx.should_finished()
