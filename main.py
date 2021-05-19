import hidden
from aiohttp import web
import sqlite3
import logging
import psycopg2 
import aiogram
import os
from aiogram import Dispatcher, executor, Bot, types

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

API_TOKEN = hidden
logging = logging.basicConfig(level=logging.INFO)
bot = Bot(token="1814093366:AAH5nFkH_g3PaYoXEShaxlZP9SYtyVLlHxQ")
dis = Dispatcher(bot)

@dis.message_handler(commands=["get"])
async def get_account_info(message: types.Message):
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dis, skip_updates=True)