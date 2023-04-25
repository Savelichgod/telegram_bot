from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

import keyboards as kb
from consts import product_index, product_descriptions

API = '5913091059:AAGpH1ZNaJGNtRxQSEpQSzb_LYMHNacz9U0'
bot = Bot(token=API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hi(message: Message):
    await bot.send_message(message.from_user.id,
                           'Привет, это магазин электроники',
                           reply_markup=kb.keyboard)


@dp.callback_query_handler(lambda c: c.data == 'catalog')
async def show_catalog(callback_query: CallbackQuery):
    await callback_query.message.delete()
    global product_index
    if product_index > 2:
        product_index = 0
    await bot.send_photo(callback_query.from_user.id,
                         photo=open(f'tovar{product_index + 1}.jpg', 'rb'),
                         caption=f'Каталог товаров\n{product_descriptions[product_index]}',
                         reply_markup=kb.keyboard_2)


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


@dp.callback_query_handler(lambda c: c.data == 'to_cart')
async def add_to_cart(callback_query: CallbackQuery):
    with open(f'cart.txt', 'a+') as cart:
        cart.write(f'{callback_query.from_user.id},{product_descriptions[product_index].split()[-1]}\n')
    await bot.send_message(callback_query.from_user.id,
                           f'Товар добавлен в корзину')


@dp.callback_query_handler(lambda c: c.data == 'cart')
async def show_cart(callback_query: CallbackQuery):
    products = []
    with open(f'cart.txt') as cart:
        for product in cart.readlines():
            products.append(product.split(",")[1])
    await bot.send_message(callback_query.from_user.id,
                           ('Ваши товары:\n' + ''.join(products)))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
