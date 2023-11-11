from telebot import types
import key


def main():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('📝  Сделать заказ', callback_data='u_order_1')
    button_2 = types.InlineKeyboardButton('Канал в telegram  📢', url=key.pub_url)
    button_3 = types.InlineKeyboardButton('🔑  Личный кабинет', callback_data='lk')
    markup.add(button_1, button_2, button_3)
    return markup


def lk():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('👤  Мои данные', callback_data='user_data')
    button_3 = types.InlineKeyboardButton('📖  История заказов', callback_data='user_history_1')
    markup.add(button_1, button_2, button_3)
    return markup


def order(page: int, max_page: int):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('Заказать  🛒', url=key.con_url)
    button_3 = types.InlineKeyboardButton('◀️  Пред. страница', callback_data='u_order_' + str(page - 1))
    button_4 = types.InlineKeyboardButton('След. страница  ▶️', callback_data='u_order_' + str(page + 1))
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


def setting():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_1 = types.InlineKeyboardButton('⬅️  В главное меню', callback_data='main')
    markup.add(button_1)
    return markup


def user_history(page: int, max_page: int):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='main')
    button_2 = types.InlineKeyboardButton('Заказать  🛒', url=key.con_url)
    button_3 = types.InlineKeyboardButton('◀️  Пред. страница', callback_data='user_history_' + str(page - 1))
    button_4 = types.InlineKeyboardButton('След. страница  ▶️', callback_data='user_history_' + str(page + 1))
    if page <= 1:
        markup.add(button_1, button_2, button_4)
    elif page >= max_page:
        markup.add(button_1, button_2, button_3)
    else:
        markup.add(button_1, button_2, button_3, button_4)
    return markup


def back_admin():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_1 = types.InlineKeyboardButton('⬅️  В админку', callback_data='a_main')
    markup.add(button_1)
    return markup


def a_main():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_1 = types.InlineKeyboardButton('🔃  Обновить каталог', callback_data='a_updatecatalog_1')
    button_2 = types.InlineKeyboardButton('👥  Список пользователей', callback_data='a_userlist_1')
    button_3 = types.InlineKeyboardButton('➕  Записать заказ', callback_data='a_neworder_1')
    markup.add(button_1, button_2, button_3)
    return markup


def a_updatecatalog_1():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  В админку', callback_data='a_main')
    button_2 = types.InlineKeyboardButton('🔃  Обновить', callback_data='a_updatecatalog_2')
    markup.add(button_1, button_2)
    return markup


