from nonebug import App
import pytest


@pytest.mark.asyncio
async def test_pip(app: App):
    import nonebot
    from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

    driver = nonebot.get_driver()
    driver.register_adapter(OnebotV11Adapter)

    # event = GroupMessageEvent(
    #     time=int(time()),
    #     sub_type="normal",
    #     self_id=123456,
    #     post_type="message",
    #     message_type="group",
    #     message_id=12345623,
    #     user_id=1234567890,
    #     group_id=1234567890,
    #     raw_message="pip install nonebot2",
    #     message=Message("pip install nonebot2"),
    #     original_message=Message("pip install nonebot2"),
    #     sender=Sender(),
    #     font=123456,
    # )

    # async with app.test_matcher(pip) as ctx:
    #     bot = ctx.create_bot()
    #     ctx.receive_event(bot, event)
    #     ctx.should_call_send(event, "nonebot2")
    #     ctx.should_finished(pip)
