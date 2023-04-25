from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from vkbottle.tools.dev.keyboard import button

buttons_menu = [
    InlineKeyboardButton('Kаталог', callback_data='catalog'),
    InlineKeyboardButton('Мои заказы', callback_data='orders'),
    InlineKeyboardButton('Корзина', callback_data='cart'),
    InlineKeyboardButton('Информация', callback_data='info'),
    InlineKeyboardButton('Регистрация', callback_data='register'),
    InlineKeyboardButton('Вход', callback_data='login'),
]

buttons_catalogue = [
    InlineKeyboardButton('Назад', callback_data='back'),
    InlineKeyboardButton('Далее', callback_data='next'),
    InlineKeyboardButton('Добавить в корзину', callback_data='add_to_cart'),
]

buttons_added_to_cart = [
    InlineKeyboardButton('Корзина', callback_data='cart'),
    InlineKeyboardButton('Продолжить просмотр', callback_data='catalog'),
]

buttons_cart = [
    InlineKeyboardButton('Удалить', callback_data='delete'),
    InlineKeyboardButton('Заказать', callback_data='order'),
    InlineKeyboardButton('Очистить корзину', callback_data='clear_cart')
]

buttons_ordered = [
    InlineKeyboardButton('Мои заказы', callback_data='orders'),
    InlineKeyboardButton('Корзина', callback_data='cart'),
]

buttons_orders = [
    InlineKeyboardButton('Отменить заказ', callback_data='cancel'),
]

buttons_register = [
    InlineKeyboardButton('Регистрация', callback_data='register'),
    InlineKeyboardButton('Войти', callback_data='login'),
    InlineKeyboardButton('Корзина', callback_data='cart'),
]

button_back = InlineKeyboardButton('Назад в меню', callback_data='menu')

keyboard_menu = InlineKeyboardMarkup(row_width=2).add(*buttons_menu)
keyboard_catalogue = (InlineKeyboardMarkup(row_width=2)
                      .add(*buttons_catalogue)
                      .add(button_back))
keyboard_added_to_cart = (InlineKeyboardMarkup()
                          .add(*buttons_added_to_cart)
                          .add(button_back))
keyboard_cart = (InlineKeyboardMarkup(row_width=3)
                 .add(*buttons_cart)
                 .add(button_back))
keyboard_ordered = (InlineKeyboardMarkup()
                    .add(*buttons_ordered)
                    .add(button_back))
keyboard_orders = (InlineKeyboardMarkup()
                   .add(*buttons_orders)
                   .add(button_back))
keyboard_register = (InlineKeyboardMarkup(row_width=2)
                     .add(*buttons_register)
                     .add(button_back))