from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

bot = Bot(TOKEN)
dp = Dispatcher(bot)
mesagee = ''
chaat = '1983759935'

@dp.message_handler(commands=['openvtbabot'])
async def process_command_1(message: types.Message):
    if message.from_user.id == '1983759935':
        await bot.send_message(message.from_user.id, 'Режим админа включен =)')
        if mesagee != '':
            print(mesagee)
            await bot.send_message(chaat, '@' + msg.from_user.username + ': ' + message.text[6:])
        else: 
            print('Новых сообщений нет')



    else: 
        await bot.send_message(message.from_user.id, 'Вы не админ)')


@dp.message_handler(commands=['start'])
async def process_command_111(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, это эхо бот")
    print(message.from_user.id)


@dp.message_handler()
async def process_command_11(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    mesagee = message.text
    

if __name__ == '__main__':
    executor.start_polling(dp)