import telebot
import func
import key
import menu
import text

bot = telebot.TeleBot(key.bot_token)
if __name__ == '__main__':
    def bot_main():
        @bot.message_handler(commands=['start'])
        def command_start(message):
            user = [message.from_user.id, message.from_user.first_name, message.from_user.username]
            func.first_join(user[0], user[1], user[2], message.text[6:])
            bot.send_message(user[0], text.main.format(user[1]), parse_mode='html', reply_markup=menu.main())

        @bot.callback_query_handler(func=lambda call: True)
        def callback_process(call):
            user = [call.message.chat.id, func.db_req_users(call.message.chat.id, [18])[0],
                    call.message.message_id]
            if call.data == 'main':
                bot.edit_message_text(text.main.format(user[1]), user[0], user[2], parse_mode='html',
                                      reply_markup=menu.main())
            elif 'order' in call.data:
                page = call.data.split('_')
                print(page)
                bot.edit_message_text(text.order.format(page[1]), user[0], user[2], parse_mode='html',
                                      reply_markup=menu.order(int(page[1])))
            elif call.data == 'lk':
                bot.edit_message_text(text.lk.format(user[1], user[0]),
                                      user[0], user[2], parse_mode='html', reply_markup=menu.lk())
            elif call.data == 'user_data':
                pass
            elif call.data == 'user_history':
                pass
            else:
                bot.edit_message_text(text.main.format(user[1]), user[0], user[2], parse_mode='html',
                                      reply_markup=menu.main())

        bot.polling(none_stop=True)


    def infinity_start(start_bot):
        try:
            if start_bot.lower() != 'y':
                quit()
            bot_main()
        except Exception as error:
            print(error)
            infinity_start(start_bot)


    start_bot = 'y'
    # start_bot = input(text.start_bot)
    infinity_start(start_bot)
else:
    print('Файл main.py создан для запуска')
