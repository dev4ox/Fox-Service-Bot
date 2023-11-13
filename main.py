import telebot
import func
import key
import menu
import text

bot = telebot.TeleBot(key.bot_token)
if __name__ == '__main__':
    def bot_main():
        @bot.message_handler(commands=['start', 'admin', 'sql'])
        def command_start(message):
            u_data = [message.from_user.id, message.message_id - 1, message.from_user.username]
            if message.text == '/start':
                func.first_join(u_data[0], u_data[2], message.text[6:])
                bot.send_message(u_data[0], text.main,
                                 parse_mode='html', reply_markup=menu.main())
            elif message.text == '/admin' and u_data[0] == key.admin_id:
                bot.send_message(u_data[0], text.a_main.format(u_data[0]),
                                 parse_mode='html', reply_markup=menu.a_main())
            elif message.text == '/sql' and u_data[0] == key.admin_id:
                data = func.check_database()
                bot.send_message(u_data[0], text.check_database(data),
                                 parse_mode='html', reply_markup=menu.back_admin(u_data[1], True))
            else:
                bot.send_message(u_data[0], text.main,
                                 parse_mode='html', reply_markup=menu.main())

        @bot.message_handler(content_types=['text'])
        def text_process(message):
            u_data = [message.chat.id, message.message_id - 1]
            if u_data[0] == key.admin_id:
                com_text, *data_text = message.text.split('; ')
                if com_text == 'neworder':
                    answer = func.db_w_new_order(data_text)
                    bot.send_message(u_data[0], answer,
                                     parse_mode='html', reply_markup=menu.back_admin(u_data[1], True))
                elif com_text == 'listorder':
                    h_page_max, *data = func.user_history(data_text[0], data_text[1])
                    bot.send_message(u_data[0], text.user_history(data_text[1], h_page_max, data),
                                     parse_mode='html', reply_markup=menu.back_admin(u_data[1], True))
                elif com_text == 'updateuser':
                    data = func.db_w_update_user(data_text)
                    if data[0]:
                        bot.send_message(u_data[0], text.db_w_update_user_t(data[1]),
                                         parse_mode='html', reply_markup=menu.back_admin(u_data[1], True))
                    else:
                        bot.send_message(u_data[0], text.db_w_update_user_f,
                                         parse_mode='html', reply_markup=menu.back_admin(u_data[1], True))

                else:
                    bot.send_message(u_data[0], 'Неизвестная команда',
                                     parse_mode='html', reply_markup=menu.back_admin(u_data[1], True))

        @bot.callback_query_handler(func=lambda call: True)
        def callback_process(call):
            u_data = [call.message.chat.id, call.message.message_id]
            if call.data == 'main':
                bot.edit_message_text(text.main, u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.main())
            elif 'u_order' in call.data:
                page = call.data.split('_')
                bot.edit_message_text(text.order(page[2], func.page_max, func.db_catalog_r(page[2])), u_data[0],
                                      u_data[1],
                                      parse_mode='html', reply_markup=menu.order(int(page[2]), func.page_max))
            elif call.data == 'lk':
                user = func.db_r_one(u_data[0], [13, 12])
                data = func.db_r_last(u_data[0], 'orders')
                if data is None:
                    data = ['-', '-', '-', '-', '-', '-', '-']
                    count = '-'
                else:
                    count = int(data[2] * (100 - data[3]) / 100)
                bot.edit_message_text(text.lk.format(user[0], user[1], data[0], data[6], count, data[4], data[5]),
                                      u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.lk())
            elif call.data == 'user_data':
                data = func.db_r_one(u_data[0], [10, 12, 13, 14, 15, 19])
                bot.edit_message_text(text.user_data.format(data[0], data[1], data[2], data[3], data[4], data[5]),
                                      u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.user_data())
            elif call.data == 'setting':
                user = func.db_r_one(u_data[0], [10, 11])
                bot.send_message(key.ch_id, text.setting_ch.format(user[0], func.t_now(), user[1]))
                bot.edit_message_text(text.setting.format(key.supp_url), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.setting())
            elif 'user_history' in call.data:
                page = call.data.split('_')
                h_page_max, *data = func.user_history(u_data[0], page[2])
                bot.edit_message_text(text.user_history(page[2], h_page_max, data), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.user_history(int(page[2]), h_page_max))
            elif 'a_main' in call.data and u_data[0] == key.admin_id:
                data = call.data.split('_')
                if data[2] == '0':
                    bot.edit_message_text(text.a_main.format(u_data[0]), u_data[0], u_data[1],
                                          parse_mode='html', reply_markup=menu.a_main())
                else:
                    bot.delete_message(u_data[0], call.data.split('_')[2])
                    bot.edit_message_text(text.a_main.format(u_data[0]), u_data[0], u_data[1],
                                          parse_mode='html', reply_markup=menu.a_main())
            elif call.data == 'a_updatecatalog_1' and u_data[0] == key.admin_id:
                bot.edit_message_text(text.a_updatecatalog_1.format(key.catalog), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.a_updatecatalog())
            elif call.data == 'a_updatecatalog_2' and u_data[0] == key.admin_id:
                data = func.db_catalog_u()
                bot.edit_message_text(text.a_updatecatalog_2.format(data[0], data[1]), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.back_admin(u_data[1]))
            elif 'a_userlist' in call.data and u_data[0] == key.admin_id:
                page = call.data.split('_')
                h_page_max, *data = func.a_userlist(page[2])
                bot.edit_message_text(text.a_userlist(page[2], h_page_max, data), u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.a_userlist(int(page[2]), h_page_max))
            elif call.data == 'a_neworder_1' and u_data[0] == key.admin_id:
                bot.edit_message_text(text.a_neworder, u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.back_admin(u_data[1]))
            elif call.data == 'a_userhistory_1' and u_data[0] == key.admin_id:
                bot.edit_message_text(text.a_userhistory, u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.back_admin(u_data[1]))
            elif call.data == 'a_updateuser_1' and u_data[0] == key.admin_id:
                bot.edit_message_text(text.a_updateuser, u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.back_admin(u_data[1]))
            else:
                bot.edit_message_text(text.main, u_data[0], u_data[1],
                                      parse_mode='html', reply_markup=menu.main())

        bot.polling(none_stop=True)


    def infinity_start(start_bot: str):
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
