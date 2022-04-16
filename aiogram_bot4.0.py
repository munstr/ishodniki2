from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
import os 
import asyncio
import time

#переменные
bot = Bot('5148976681:AAH_2G4SmbegCm3VMjh54bxDJ3SILT6FhXc')
dp = Dispatcher(bot)
punctuation = '.,?¿!¡(){}<>[]:;=≈≠+±-¯—–_*×÷/|\\~%^#&№%‰"„“«»”\'ʼ‹‡`†›$€₽¥¢£'
admsend = []
idd = '1983759935'
pluszn = False
minuszn = False
umnozzn = False
delenzn = False

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

#хэндлерЫ
@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer('Привет. Я на связи)')
    
@dp.message_handler(commands=['calc'])
async def hello(message: types.Message):
    await message.answer('Режим калькулятора активирован. Выберите действие:', reply_markup=inkb)
    
@dp.callback_query_handler(text='plus')
async def pluscalc(callback : types.CallbackQuery):
    await message.answer('Напишите 2 числа, которые вы хотите сложить, через пробел')
    global pluszn
    pluszn = True
    
    
@dp.callback_query_handler(text='minus')
async def pluscalc(callback : types.CallbackQuery):
    await message.answer('Напишите 2 числа, которые вы хотите вычесть, через пробел')
    global minuszn
    minuszn = True
  
@dp.callback_query_handler(text='umnoz')
async def pluscalc(callback : types.CallbackQuery):
    await message.answer('Напишите 2 числа, которые вы хотите умножить, через пробел')
    global umnozzn
    umnozzn = True
    
@dp.callback_query_handler(text='delen')
async def pluscalc(callback : types.CallbackQuery):
    await message.answer('Напишите 2 числа, которые вы хотите разделить, через пробел')
    global delenzn
    delenzn = True
      
    

#админская часть
@dp.message_handler(commands=['send_all_message'])
async def admin_mode(message: types.Message):
    if str(message.from_user.id) == idd: 
        await message.answer('Привет, админ')
        number = len(admsend)        
        for name in admsend:
            await message.answer(name)
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

    global pluszn
    global minuszn
    global umnozzn
    global delenzn
    
    if pluszn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x + y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        pluszn = False



    elif minuszn == True: 
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x - y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        minuszn = False


    elif delenzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x / y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        delenzn = False
            


    elif umnozzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x * y
            await message.answer('Ответ: ' + str(otv))
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')  
        umnozzn = False  


        

if __name__ == '__main__':
    executor.start_polling(dp)
