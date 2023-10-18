import telebot
import datetime
import key
import menu
import text

bot = telebot.TeleBot(key.bot_token)
def bot_start():
    @bot.message_handler(commands=['start'])
    def command_start(message):
        user = [message.chat.id, message.from_user.first_name, message.message_id]
        bot.send_message(user[0], text.main.format(user[1]), parse_mode='html', reply_markup=menu.main())

    @bot.callback_query_handler(func=lambda call: True)
    def callback_process(call):
        user = [call.message.chat.id, call.message.from_user.first_name, call.message.message_id]
        if call.data == 'main':
            bot.edit_message_text(text.main.format(user[1]), user[0], user[2], parse_mode='html',
                                  reply_markup=menu.main())
        elif call.data == 'order':
            bot.edit_message_text(text.order, user[0], user[2], parse_mode='html', reply_markup=menu.order())
        elif call.data == 'lk':
            bot.edit_message_text(text.lk.format(user[1], user[0]), user[0], user[2], parse_mode='html',
                                  reply_markup=menu.lk())
        elif call.data == 'catalog':
            pass
        elif call.data == 'user_data':
            pass
        elif call.data == 'user_history':
            pass
        else:
            bot.edit_message_text(text.main.format(user[1]), user[0], user[2], parse_mode='html',
                                  reply_markup=menu.main())

    bot.polling(none_stop=True)


def infinity_start():
    try:
        bot_start()
    except Exception as error:
        print(error)
        infinity_start()
infinity_start()