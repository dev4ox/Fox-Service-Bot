import telebot
import func
import key
import menu
import text

bot = telebot.TeleBot(key.bot_token)
if __name__ == '__main__':
    def bot_main():
        @bot.message_handler(commands=['start', 'admin', 'sql', 'pay'])
        def command_start(message):
            u_data = [message.from_user.id, message.from_user.username]
            if message.text == '/start':
                func.first_join(u_data[0], u_data[1], message.text[6:])
                bot.send_message(u_data[0], text.main, parse_mode='html', reply_markup=menu.main())
            elif message.text == '/admin' and u_data[0] == key.admin_id:
                bot.send_message(u_data[0], text.com_admin.format(u_data[0]), reply_markup=menu.com_admin())

        @bot.callback_query_handler(func=lambda call: True)
        def callback_process(call):
            u_data = [call.message.chat.id, call.message.message_id]
            if call.data == 'main':
                bot.edit_message_text(text.main, u_data[0], u_data[1], parse_mode='html', reply_markup=menu.main())
            elif 'order' in call.data:
                page = call.data.split('_')
                bot.edit_message_text(text.order(page[1], func.page_max, func.catalog_r(page[1])), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.order(int(page[1]), 1))
            elif call.data == 'lk':
                user = func.db_r_one(u_data[0], [13, 12])
                data = func.db_r_last(u_data[0], 'orders')
                if data is None:
                    data = ['-', '-', '-', '-', '-', '-', '-']
                    count = '-'
                else:
                    count = int(data[2] * (100 - data[3]) / 100)
                bot.edit_message_text(text.lk.format(user[0], user[1], data[1], data[6], count, data[4], data[5]),
                                      u_data[0], u_data[1], parse_mode='html', reply_markup=menu.lk())
            elif call.data == 'user_data':
                data = func.db_r_one(u_data[0], [10, 12, 13, 14, 15, 18])
                bot.edit_message_text(text.user_data.format(data[0], data[1], data[2], data[3], data[4], data[5]),
                                      u_data[0], u_data[1], parse_mode='html', reply_markup=menu.user_data())
            elif call.data == 'setting':
                user = func.db_r_one(u_data[0], [10, 11])
                bot.send_message(key.ch_id, text.setting_ch.format(user[0], func.t_now(), user[1]))
                bot.edit_message_text(text.setting.format(key.con_url), u_data[0], u_data[1], parse_mode='html',
                                      reply_markup=menu.setting())
            elif 'user_history' in call.data:
                page = call.data.split('_')
                user = func.db_r_one(u_data[0], [13, 12])
                page_max, *data = func.user_history
                bot.edit_message_text(text.user_history(user[0], user[1], page[2], page_max, data),
                                      u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.user_history(int(page[1]), func.page_max))
            elif call.data == 'main_admin' and u_data[0] == key.admin_id:
                bot.edit_message_text(text.com_admin.format(u_data[0]), u_data[0], u_data[1], parse_mode='html',
                                      reply_markup=menu.com_admin())
            elif call.data == 'a_update_catalog1' and u_data[0] == key.admin_id:
                bot.edit_message_text(text.a_update_catalog1.format(key.catalog), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.update_catalog1())
            elif call.data == 'a_update_catalog2' and u_data[0] == key.admin_id:
                data = func.catalog_u()
                bot.edit_message_text(text.a_update_catalog2.format(data[0], data[1]), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.update_catalog2())
            else:
                bot.edit_message_text(text.main, u_data[0], u_data[1], parse_mode='html', reply_markup=menu.main())

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
