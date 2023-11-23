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
    button_2 = types.InlineKeyboardButton('Заказать  🛒', url=key.buy_url)
    button_3 = types.InlineKeyboardButton('◀️  Пред. страница', callback_data='u_order_' + str(page - 1))
    button_4 = types.InlineKeyboardButton('След. страница  ▶️', callback_data='u_order_' + str(page + 1))
    if page <= 1 < max_page != 1:
        markup.add(button_1, button_2, button_4)
    elif max_page <= page != 1:
        markup.add(button_1, button_2, button_3)
    elif 1 < page < max_page:
        markup.add(button_1, button_2, button_3, button_4)
    else:
        markup.add(button_1, button_2)
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
    button_1 = types.InlineKeyboardButton('⬅️  Назад', callback_data='lk')
    button_2 = types.InlineKeyboardButton('Поддержка  🆘', url=key.supp_url)
    button_3 = types.InlineKeyboardButton('◀️  Пред. страница', callback_data='user_history_' + str(page - 1))
    button_4 = types.InlineKeyboardButton('След. страница  ▶️', callback_data='user_history_' + str(page + 1))
    if page <= 1 < max_page != 1:
        markup.add(button_1, button_2, button_4)
    elif max_page <= page != 1:
        markup.add(button_1, button_2, button_3)
    elif 1 < page < max_page:
        markup.add(button_1, button_2, button_3, button_4)
    else:
        markup.add(button_1, button_2)
    return markup


# Если админ пишет текстовую команду, то бот удаляет своё предыдущее сообщение (сохраняется история сообщений)
def back_admin(message_id: int, delmessage: bool = False):
    markup = types.InlineKeyboardMarkup(row_width=1)
    if delmessage:
        button_1 = types.InlineKeyboardButton('⬅️  В админку', callback_data='a_main_' + str(message_id))
    else:
        button_1 = types.InlineKeyboardButton('⬅️  В админку', callback_data='a_main_0')
    markup.add(button_1)
    return markup


def a_main():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button_1 = types.InlineKeyboardButton('🔃  Обновить каталог', callback_data='a_updatecatalog_1')
    button_2 = types.InlineKeyboardButton('👥  Список пользователей', callback_data='a_userlist_1')
    button_3 = types.InlineKeyboardButton('➕  Записать заказ', callback_data='a_neworder_1')
    button_4 = types.InlineKeyboardButton('📃  Заказы пользователя', callback_data='a_userhistory_1')
    markup.add(button_1, button_2, button_3, button_4)
    return markup


def a_updatecatalog():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  В админку', callback_data='a_main_0')
    button_2 = types.InlineKeyboardButton('🔃  Обновить', callback_data='a_updatecatalog_2')
    markup.add(button_1, button_2)
    return markup


def a_userlist(page: int, max_page: int):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button_1 = types.InlineKeyboardButton('⬅️  В админку', callback_data='a_main_0')
    button_2 = types.InlineKeyboardButton('Смена данных  📝', callback_data='a_updateuser_1')
    button_3 = types.InlineKeyboardButton('◀️  Пред. страница', callback_data='a_userlist_' + str(page - 1))
    button_4 = types.InlineKeyboardButton('След. страница  ▶️', callback_data='a_userlist_' + str(page + 1))
    if page <= 1 < max_page != 1:
        markup.add(button_1, button_2, button_4)
    elif max_page <= page != 1:
        markup.add(button_1, button_2, button_3)
    elif 1 < page < max_page:
        markup.add(button_1, button_2, button_3, button_4)
    else:
        markup.add(button_1, button_2)
    return markup

