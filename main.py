import logging
import aiogram
from aiogram import Dispatcher, executor, Bot, types

API_TOKEN = "1814093366:AAH5nFkH_g3PaYoXEShaxlZP9SYtyVLlHxQ"
logging = logging.basicConfig(level=logging.INFO)
bot = Bot(token="1814093366:AAH5nFkH_g3PaYoXEShaxlZP9SYtyVLlHxQ")
dis = Dispatcher(bot)

@dis.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await  message.reply("Hello! \n I can speak now") 

@dis.message_handler()
async def reply_messages(message: types.Message):
    await message.reply(message.text)

if __name__ == '__main__':
    executor.start_polling(dis, skip_updates=True)
