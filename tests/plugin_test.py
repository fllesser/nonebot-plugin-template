import pytest
from fake import fake_group_message_event_v11
from nonebug import App


@pytest.mark.asyncio
async def test_pip(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Bot, Message
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

    event = fake_group_message_event_v11(message="pip install nonebot2")
    try:
        from nonebot_plugin_template import pip  # type:ignore
    except ImportError:
        pytest.skip("nonebot_plugin_template.pip not found")

    async with app.test_matcher(pip) as ctx:
        adapter = nonebot.get_adapter(OnebotV11Adapter)
        bot = ctx.create_bot(base=Bot, adapter=adapter)
        ctx.receive_event(bot, event)
        ctx.should_call_send(event, Message("nonebot2"), result=None, bot=bot)
        ctx.should_finished()
