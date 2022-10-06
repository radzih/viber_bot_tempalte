import asyncio
from aiohttp import web

from viber_bot.misc.setup_django import setup_django; setup_django()
from loader import *
from viber_bot.config import load_config
from viberio.dispatcher.webhook import ViberWebhookView


config = load_config()


ViberWebhookView.bind(dp, app, '/')

async def set_webhook():
    await asyncio.sleep(1)
    result = await viber.set_webhook(config.bot.webhook_url)


async def on_shutdown(application: web.Application):
    await viber.close()

def main():
    app.on_shutdown.append(on_shutdown)
    loop.create_task(set_webhook())
    web.run_app(app, host='localhost', port=8000, loop=loop)

if __name__ == '__main__':
    main()