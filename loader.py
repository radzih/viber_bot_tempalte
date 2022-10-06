import asyncio
from aiohttp import web

from viberio.api.client import ViberBot
from viberio.dispatcher.dispatcher import Dispatcher
from viberio.types.configuration import BotConfiguration

from viber_bot.config import load_config


config = load_config()

loop = asyncio.new_event_loop()
app = web.Application()
bot_config = BotConfiguration(auth_token=config.bot.token, name='Test bot')
viber = ViberBot(bot_config, loop=loop)
dp = Dispatcher(viber)
