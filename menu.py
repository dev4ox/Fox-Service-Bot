from telebot import types
def start():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('📝  Сделать заказ', callback_data='order')
    button_2 = types.InlineKeyboardButton('📞  Консультация', url='https://t.me/dev4ox')
    button_3 = types.InlineKeyboardButton('🔑  Личный кабинет', callback_data='lk')
    markup.add(button_1, button_2, button_3)
    return markup