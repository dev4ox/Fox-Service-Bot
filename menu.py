from telebot import types
import key


def main():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('📝  Сделать заказ', callback_data='order_1')
    button_2 = types.InlineKeyboardButton('Канал в telegram  📢', url=key.public_url)
    button_3 = types.InlineKeyboardButton('🔑  Личный кабинет', callback_data='lk')
    markup.add(button_1, button_2, button_3)
    return markup

def lk():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('👤  Мои данные', callback_data='user_data')
    button_3 = types.InlineKeyboardButton('📖  История заказов', callback_data='user_history')
    markup.add(button_1, button_2, button_3)
    return markup

def order(page:int, max_page:int):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('Заказать  🛒', url=key.connect_url)
    button_3 = types.InlineKeyboardButton('◀️  Пред. страница', callback_data='order_'+str(page-1))
    button_4 = types.InlineKeyboardButton('След. страница  ▶️', callback_data='order_'+str(page+1))
    if page <= 1:
        markup.add(button_1, button_2, button_4)
    elif page >= max_page:
        markup.add(button_1, button_2, button_3)
    else:
        markup.add(button_1, button_2, button_3, button_4)
    return markup

def user_data():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='lk')
    button_2 = types.InlineKeyboardButton('🔏  Редактировать', callback_data='setting')
    markup.add(button_1, button_2)
    return markup

