from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json
import os 
import asyncio
import time
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import config as cfg
from pyowm.utils.config import get_default_config
import wikipedia
import re
import random


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
weather = False
wikip = False

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

def weatherr(place):
    global weather
    global clouds
    global temperat
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('e3a6bb0af106f781e5bac08fd23945cc')
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather
        clouds = w.detailed_status      # 'clouds'
        temperat = w.temperature('celsius')['temp']
        weather = False
    except:
        clouds = ''
        temperat = 0
        weather = True


#хэндлерЫ
@dp.message_handler(commands=['start'])
async def hellgho(message: types.Message):
    await message.answer('Привет. Я на связи)')

@dp.message_handler(commands=['random'])
async def hellgewho(message: types.Message):
    await message.answer('Случайное число от 1 до 10: ' + str(random.randrange(1, 11, 1)))

@dp.message_handler(commands=['coin'])
async def hellwwho(message: types.Message):
    result = random.randint (1, 2)
    if result == 1:
        await message.answer('РЕШКА')
    elif result == 2:
        await message.answer('ОРЕЛ')
    
@dp.message_handler(commands=['calc'])
async def hellgo(message: types.Message):
    await message.answer('Режим калькулятора активирован.')
    await message.answer('Выберите действие:', reply_markup=inkb)
    
    
@dp.callback_query_handler(text='plus')
async def pluscatttlc(callback : types.CallbackQuery):
    global pluszn
    pluszn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
    
    
@dp.callback_query_handler(text='minus')
async def pluscakjklc(callback : types.CallbackQuery):
    global minuszn
    minuszn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
  
@dp.callback_query_handler(text='umnoz')
async def pluscjjjalc(callback : types.CallbackQuery):
    global umnozzn
    umnozzn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()
    
@dp.callback_query_handler(text='delen')
async def pluscalnnnc(callback : types.CallbackQuery):
    global delenzn
    delenzn = True
    await callback.message.answer('Введите первое и второе число через пробелы')
    await callback.answer()


@dp.message_handler(commands=['about'])
async def admin_mdddodwwe(message: types.Message):  
    await message.answer('ChatBot - последняя версия от 29.04.2022\nНаписано на Python\nРазработчик: @munstr001') 

@dp.message_handler(commands=['info'])
async def adodwwe(message: types.Message):  
    await message.answer('Вероятность события: ' + str(random.randrange(0, 101, 1)) + '%')
    

#админская часть
@dp.message_handler(commands=['send_all_message'])
async def admin_modwwe(message: types.Message):
    if str(message.from_user.id) == idd: 
        await message.answer('Привет, админ')
        number = len(admsend)        
        for name in admsend:
            await message.answer(name)
        admsend.clear()
    else:
        await message.answer("Вы не админ")

@dp.message_handler(commands=['weather'])
async def admin_mwwwqode(message: types.Message):
    global weather
    weather = True
    await message.answer('Режим погоды активирован')
    await message.answer('Напишите название вашего города')

@dp.message_handler(commands=['wikipedia'])
async def admin_mwwqode(message: types.Message):
    global wikip
    wikip = True
    await message.answer('Режим поиска по википедии активирован')
    await message.answer('Напишите слово, которое вы хотите найти')


wikipedia.set_lang("ru")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'




@dp.message_handler()
async def echo_send(message : types.Message):
    admsend.append(str(message.from_user.id) + ': ' + message.text)
    if len(get_words(message.text) & set(json.load(open('ukr.json')))) != 0:
        msg = await message.reply('Обсуждение на эту тему ЗАПРЕЩЕНО!!!')
        time.sleep(4)
        await msg.delete()
        await message.delete()
	
    if len(get_words(message.text) & set(json.load(open('mat.json')))) != 0:
        msg = await message.reply('Материться ЗАПРЕЩЕНО!!!')
        time.sleep(4)
        await msg.delete()
        await message.delete()

    global pluszn
    global minuszn
    global umnozzn
    global delenzn
    global wikip
    
    if pluszn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x + y
            await message.answer('Ответ: ' + str(otv))
            pluszn = False
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        



    elif minuszn == True: 
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x - y
            await message.answer('Ответ: ' + str(otv))
            minuszn = False
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        


    elif delenzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x / y
            await message.answer('Ответ: ' + str(otv))
            delenzn = False
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')
        
            


    elif umnozzn == True:
        s = message.text
        try:
            x = int(s.split()[0])
            y = int(s.split()[1])
            otv = x * y
            await message.answer('Ответ: ' + str(otv))
            umnozzn = False 
        except ValueError:
            await message.answer('Введите цифры, а не буквы')
        except IndexError:
            await message.answer('Введите 2 числа!!!')  
         

    if weather == True:
        global place 
        place = message.text
        weatherr(place)
        if clouds != '':
            await message.answer('Сегодня в городе ' + place + ' ' + clouds + '\n' + 'Температура в районе ' + str(temperat) + '°C')
        else:
            await message.answer('Данного города нет в базе городов или вы ввели не название города. Попробуйте заново')

    if wikip == True:
        await message.answer(getwiki(message.text))
        wikip = False


        

if __name__ == '__main__':
    executor.start_polling(dp)
