from collections import defaultdict

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup

import keyboards as kb
from consts import products_names, product_descriptions, info, \
    RegistrationStateGroup, product_index, LoginStateGroup
from db_engine import create_table, append_to_table, get_products, delete_line, \
    get_all_id, get_ordered_names, set_ordered, get_ordered_ids, clear_database

API = '5913091059:AAGpH1ZNaJGNtRxQSEpQSzb_LYMHNacz9U0'
bot = Bot(token=API)
data = defaultdict(dict)
tmp = defaultdict(dict)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def hi(message: Message):
    await bot.send_message(message.from_user.id,
                           'Привет, это магазин электроники',
                           reply_markup=kb.keyboard_menu)


@dp.callback_query_handler(lambda c: c.data == 'menu')
async def main_menu(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await bot.send_message(callback_query.from_user.id,
                           'Главное меню.\n',
                           reply_markup=kb.keyboard_menu)


@dp.callback_query_handler(lambda c: c.data == 'catalog')
async def show_catalog(callback_query: CallbackQuery):
    await callback_query.message.delete()
    global product_index
    with open('product_names.txt') as f:
        file_size = len(f.readlines())
    if product_index > file_size - 1:
        product_index = 0
    msg = products_names[product_index] + '\n\n' + product_descriptions[
        product_index]
    await bot.send_message(callback_query.from_user.id,
                           # photo=open(f'img/tovar{product_index + 1}.jpg', 'rb'),
                           f'Каталог товаров\n\n{msg}',
                           reply_markup=kb.keyboard_catalogue)


@dp.callback_query_handler(lambda c: c.data == 'next')
async def add_to_cart(callback_query: CallbackQuery):
    global product_index
    product_index += 1
    await show_catalog(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'back')
async def add_to_cart(callback_query: CallbackQuery):
    global product_index
    if product_index <= 0:
        product_index = 3
    product_index -= 1
    await show_catalog(callback_query)


@dp.callback_query_handler(lambda c: c.data == 'add_to_cart')
async def add_to_cart(callback_query: CallbackQuery):
    await callback_query.message.delete()
    append_to_table(products_names[product_index],
                    callback_query.from_user.id, )
    await bot.send_message(callback_query.from_user.id,
                           f'Товар добавлен в корзину',
                           reply_markup=kb.keyboard_added_to_cart)


@dp.callback_query_handler(lambda c: c.data == 'cart')
async def show_cart(callback_query: CallbackQuery):
    await callback_query.message.delete()
    products = list(get_products(callback_query.from_user.id))
    if len(products) == 0:
        await bot.send_message(callback_query.from_user.id,
                               'Ваша корзина пуста.',
                               reply_markup=InlineKeyboardMarkup().add(
                                   kb.button_back))
    else:
        await bot.send_message(callback_query.from_user.id,
                               ('Ваши товары:\n' + '\n'.join(
                                   [f'{n + 1}. ' + i[0] for n, i in
                                    enumerate(products)])),
                               reply_markup=kb.keyboard_cart
                               )


@dp.callback_query_handler(lambda c: c.data == 'delete')
async def delete_product(callback_query: CallbackQuery):
    await callback_query.message.delete()