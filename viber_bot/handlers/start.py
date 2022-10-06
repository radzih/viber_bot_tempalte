from loader import dp, viber
from viberio.types import messages, requests
from viber_bot.filters.text_filter import TextFilter


@dp.text_messages_handler(TextFilter('start'))
async def start(request: requests.ViberMessageRequest, data: dict):
    text = messages.TextMessage(text=f"Hello, {request.sender.name}")
    return await viber.send_message(request.sender.id, text)