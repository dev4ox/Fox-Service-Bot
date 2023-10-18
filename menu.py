from telebot import types
def main():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('📝  Сделать заказ', callback_data='order')
    button_2 = types.InlineKeyboardButton('Канал в telegram  📢', url='https://t.me/rndfoxservice')
    button_3 = types.InlineKeyboardButton('🔑  Личный кабинет', callback_data='lk')
    markup.add(button_1, button_2, button_3)
    return markup

def lk():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('👤  Мои данные', callback_data='user_data')
    button_3 = types.InlineKeyboardButton('  История заказов', callback_data='user_history')
    markup.add(button_1, button_2, button_3)
    return markup

def order():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('📋  Каталог', callback_data='catalog')
    button_3 = types.InlineKeyboardButton('📩  Написать нам', url='https://t.me/dev4ox')
    markup.add(button_1, button_2, button_3)
    return markup


