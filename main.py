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
bot = Bot(token=hidden)
dis = Dispatcher(bot)

@dis.message_handler(commands=["get"])
async def get_account_info(qiwi, message: types.Message):
    res = aiohttp.ClientSession()
    res.headers['Accept'] = "application/json"
    res.headers['authorization'] = 'Bearer ' + qiwi
    obj = res.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
    await message.reply(res.json())

if __name__ == "__main__":
    executor.start_polling(skip_updates=True)