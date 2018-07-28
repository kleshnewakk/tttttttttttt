import logging
import telebot
from telebot import types

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
#
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# local imports:
from config import TOKEN
import storagework as st

#
logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# enable logging:
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
    button_1 = types.KeyboardButton(text = st.get_setting("button1","title"))
    button_2 = types.KeyboardButton(text = st.get_setting("button2","title"))
    button_3 = types.KeyboardButton(text = st.get_setting("button3","title"))
    button_4 = types.KeyboardButton(text = st.get_setting("button4","title"))
    button_5 = types.KeyboardButton(text = st.get_setting("button5","title"))
    button_6 = types.KeyboardButton(text = st.get_setting("button6","title"))
    button_7 = types.KeyboardButton(text = st.get_setting("button7","title"))
    keyboard.add(button_1)
    keyboard.add(button_2, button_3, button_4)
    keyboard.add(button_5, button_6)
    keyboard.add(button_7)
    await bot.send_message(message.chat.id, st.get_setting("general","title"), reply_markup=keyboard)

@dp.message_handler()
async def process_message(msg: types.Message):
    if msg.chat.type == 'group':
        toid = msg.chat.id
    elif msg.chat.type == 'private':
        toid = msg.from_user.id
    if msg.text == st.get_setting("button1","title"):
        await bot.send_message(toid, st.get_setting("button1","message"))
    elif msg.text == st.get_setting("button2","title"):
        await bot.send_message(toid, st.get_setting("button2","message"))
    elif msg.text == st.get_setting("button3","title"):
        await bot.send_message(toid, st.get_setting("button3","message"))
    elif msg.text == st.get_setting("button4","title"):
        await bot.send_message(toid, st.get_setting("button4","message"))
    elif msg.text == st.get_setting("button5","title"):
        await bot.send_message(toid, st.get_setting("button5","message"))
    elif msg.text == st.get_setting("button6","title"):
        await bot.send_message(toid, st.get_setting("button6","message"))
    elif msg.text == st.get_setting("button7","title"):
        await bot.send_message(toid, st.get_setting("button7","message"))
# shut down, close storage
async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

# POLLING:
if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)