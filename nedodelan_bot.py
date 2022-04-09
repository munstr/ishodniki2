from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

import os

bot = Bot(TOKEN)
dp = Dispatcher(bot)

answ = dict()
#инлайн кнопки
urlkb = InlineKeyboardMarkup(row_width=1)
urlButton1 = InlineKeyboardButton(text='YouTube', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='Google', url='https://google.com')
urlkb.add(urlButton1, urlButton2)

#обработка кнопок
@dp.message_handler(commands=['start'])
async def process_command_1(message: types.Message):
    await message.answer("Ютуб или гугл?", reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='лайк', callback_data='like1'),\
                                             InlineKeyboardButton(text='дизлайк', callback_data='like2'))

@dp.message_handler(commands=['test'])
async def process_command_10(message: types.Message):
    await message.answer("Ютуб", reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like'))
async def calllll(callback : types.CallbackQuery):
	res = int(callback.data.split('_')[0])
	if callback.from_user.id not in answ:
		answ[f'{callback.from_user.id}'] = res
		await callback.answer('Вы проголосовали!')
	else:
		await callback.answer('Не дудось, бота сломаешь!', show_alert=True)


if __name__ == '__main__':
    executor.start_polling(dp)
