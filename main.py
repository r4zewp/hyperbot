import requests
import hidden
import asyncio
import ssl
import sys
import aiohttp
from aiohttp import web
import logging
import aiogram
from aiogram import Dispatcher, executor, Bot, types

API_TOKEN = hidden
logging = logging.basicConfig(level=logging.INFO)
bot = Bot(token="1814093366:AAH5nFkH_g3PaYoXEShaxlZP9SYtyVLlHxQ")
dis = Dispatcher(bot)

@dis.message_handler(commands=["get"])
async def get_account_info(message: types.Message):
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dis, skip_updates=True)