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
            func.first_join(message.from_user.id, message.from_user.username, message.text[6:])
            bot.send_message(message.from_user.id, text.main, parse_mode='html', reply_markup=menu.main())

        @bot.callback_query_handler(func=lambda call: True)
        def callback_process(call):
            u_data = [call.message.chat.id, call.message.message_id]
            user = func.db_r(u_data[0], [11, 12, 13, 14, 15, 16])
            if call.data == 'main':
                bot.edit_message_text(text.main, u_data[0], u_data[1], parse_mode='html', reply_markup=menu.main())
            elif 'order' in call.data:
                page = call.data.split('_')
                bot.edit_message_text(text.order.format(page[1]), u_data[0], u_data[1], parse_mode='html',
                                      reply_markup=menu.order(int(page[1]), 5))
            elif call.data == 'lk':
                last_data = func.db_r_last(u_data[0], 'orders')
                print(last_data)
                if not last_data:
                    last_data = ['-', '-', '-', '-', '-', '-', '-']
                    count = '-'
                else:
                    count = int(last_data[2] * (100 - last_data[3]) / 100)
                bot.edit_message_text(text.lk.format(user[2], user[1], last_data[1], last_data[6], count, last_data[4],
                                                     last_data[5]), u_data[0], u_data[1],
                                                     parse_mode='html', reply_markup=menu.lk())
            elif call.data == 'sing_up':
                pass
            elif call.data == 'user_data':
                pass
            elif call.data == 'setting':
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
