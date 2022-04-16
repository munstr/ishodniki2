from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
import os 
import asyncio
import time

#переменные
bot = Bot('5254391359:AAHHzp56Sx79SP0q9MrsRc3klaXwUAk21Do')
dp = Dispatcher(bot)
punctuation = '.,?¿!¡(){}<>[]:;=≈≠+±-¯—–_*×÷/|\\~%^#&№%‰"„“«»”\'ʼ‹‡`†›$€₽¥¢£'
admsend = []
idd = '1983759935'
pluszn = False
minuszn = False
umnozzn = False
delenzn = False
x = 0
y = 0

#кнопки
inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Сложение', callback_data='plus')).add(InlineKeyboardButton(text='Вычитание', callback_data='minus')).add(InlineKeyboardButton(text='Умножение', callback_data='umnoz')).add(InlineKeyboardButton(text='Деление', callback_data='delen'))


#обработка запрещенных слов
def get_words(text, punctuation=punctuation):
    text = text.lower()
    for c in punctuation:
        text = text.replace(c, ' ')
    words = set(text.split(' '))
    if '' in words:
        words.remove('')
    return words
#калькулятор
def calc(x, y, zn):
	if zn == '+':
		otv = int(x) + int(y)
	elif zn == '-':
		otv = int(x) - int(y)
	elif zn == '*':
		otv = int(x) * int(y)
	elif zn == '/':
		otv = int(x) / int(y)
		
#хэндлерЫ
@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer('Привет. Я на связи)')
    
@dp.message_handler(commands=['calc'])
async def hello(message: types.Message):
    await message.answer('Режим калькулятора активирован. Выберите действие:', reply_markup=inkb)
    
@dp.callback_query_handler(text='plus')
async def pluscalc(callback : types.CallbackQuery):
    global pluszn
    pluszn = True
    
    
@dp.callback_query_handler(text='minus')
async def pluscalc(callback : types.CallbackQuery):
    global minuszn
    minuszn = True
  
@dp.callback_query_handler(text='umnoz')
async def pluscalc(callback : types.CallbackQuery):
    global umnozzn
    umnozzn = True
    
@dp.callback_query_handler(text='delen')
async def pluscalc(callback : types.CallbackQuery):
    global delenzn
    delenzn = True
      
    

#админская часть
@dp.message_handler(commands=['send_all_message'])
async def admin_mode(message: types.Message):
    if str(message.from_user.id) == idd: 
    	await message.answer('Привет, админ')
    	number = len(admsend)
    	try:
            for name in admsend:
                await message.answer(name)
        except RetryAfter as e:
			await asyncio.sleep(e.timeout)
    	admsend.clear()
    else:
    	await message.answer("Вы не админ")


@dp.message_handler()
async def echo_send (message : types.Message):
    admsend.append(str(message.from_user.id) + ': ' + message.text)
    if len(get_words(message.text) & set(json.load(open('cenz.json')))) != 0:
        msg = await message.reply('Обсуждение на эту тему ЗАПРЕЩЕНО!!!')
        await msg.delete()
        await message.delete()
	
    if len(get_words(message.text) & set(json.load(open('cenzz.json')))) != 0:
        msg = await message.reply('Материться ЗАПРЕЩЕНО!!!')
        await msg.delete()
        time.sleep(2)
        await message.delete()
    
    if pluszn == True:
        try:
            x = int(message.text)
        except ValueError:
            await message.reply('Это не число!!!')
        await message.answer('Введите второе число')
        time.sleep(1)
        
        
        
    


if __name__ == '__main__':
    executor.start_polling(dp)
