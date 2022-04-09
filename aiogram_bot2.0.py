from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
import os 
import asyncio
import time

#переменные
bot = Bot(TOKEN)
dp = Dispatcher(bot)
punctuation = '.,?!():;-'
admsend = []


#обработка запрещенных слов
def get_words(text, punctuation=punctuation):
    text = text.lower()
    for c in punctuation:
        text = text.replace(c, ' ')
    words = set(text.split(' '))
    if '' in words:
        words.remove('')
    return words

#хэндлерЫ
@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer('Привет. Я на связи)')

#админская часть
@dp.message_handler(commands=['3303_adm_send'])
async def admin_mode(message: types.Message):
    await message.answer('Привет, админ')
    number = len(admsend)
    try:
        for name in admsend:
        await message.answer(name)
    except RetryAfter as e:
        await asyncio.sleep(e.timeout)
    admsend.clear()


@dp.message_handler()
async def echo_send (message : types.Message):
    admsend.append(str(message.from_user.id) + ': ' + message.text)
    if len(get_words(message.text) & set(json.load(open('cenz.json')))) != 0:
        msg = await message.reply('Обсуждение на эту тему ЗАПРЕЩЕНО!!!')
        time.sleep(3)
        await msg.delete()
        await message.delete()
    


if __name__ == '__main__':
    executor.start_polling(dp)