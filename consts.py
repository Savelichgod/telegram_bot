from aiogram.dispatcher.filters.state import StatesGroup, State
product_index = 0
product_descriptions = ['Это очень крутой айфон', 'Это очень крутой самсунг', 'Это очень крутой ксяоми']

with open('product_names.txt') as file:
    products_names = file.readlines()