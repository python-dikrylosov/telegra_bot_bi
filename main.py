# -*- coding: utf-8 -*-
name = None
row_status = None
import numpy as np
import pandas as pd
print(pd.options.display.max_rows)
pd.options.display.max_rows = 999
pd.options.display.max_columns = 999
import time
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Rate = 3
speak.Volume = 100

text = "бот активирован" + str(time.time())
speak.Speak(text)


import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import password
from polosdk import RestClient
client = RestClient(password.api_key_polo, password.api_secret_polo)
# Get a list of all accounts of a user with each account’s id, type and balances (assets)
response = client.accounts().get_balances()
#print(response)
response_0 = response[0]
response_0_balances = response_0['balances']
print(response_0_balances)
dapd = pd.DataFrame(response_0_balances)
print(dapd.shape)
for i in range(dapd.shape[0]):
    print(response_0_balances[i])
    response_0_balances_i = response_0_balances[i]
    if response_0_balances_i['currency'] == "BTC":
        print("victory BTC")
        available_balance_btc = response_0_balances_i['available']
        available_balance_btc = float(available_balance_btc)
        print(type(available_balance_btc))
        hold_balance_btc = response_0_balances_i['hold']
        hold_balance_btc = float(response_0_balances_i['hold'])
        print(type(hold_balance_btc))
        total_balance_btc = available_balance_btc + hold_balance_btc
        print(response_0_balances_i['currency'],"Total balance btc polo : " + str(total_balance_btc))

from nicehash import nicehash as nh
host = password.host
organisation_id = password.organisation_id
key = password.keynh
secret = password.secretnh

private_api = nh.private_api(host, organisation_id, key, secret)
my_accounts = private_api.get_accounts()
print()
#print(my_accounts)
total = my_accounts['total']
total_currencies = my_accounts['currencies']
#print(str(total['currency']))
print(str(total['totalBalance']))
print( )


import telebot
from telebot import types
from block_io import BlockIo
api_key_block_btc = ''
SECRET_PIN = '' 
API_VERSION = 2
block_io_btc = BlockIo(api_key_block_btc, SECRET_PIN, API_VERSION)

#https://t.me/freemarket_exchange_bot


time.sleep(2)

telegram_group = "-1001910854574"
CHANNEL_ID = -1001688555585
bot = telebot.TeleBot(password.TOKEN)


def start_output():
    data_output = block_io_btc.is_valid_address(address=str(str(message.text.strip())))
    print(data_output)
    data_output = data_output["data"]
    data_output_adress = data_output["address"]
    data_output_is_valid = data_output["is_valid"]
    if data_output_is_valid == True:
        block_io_btc.send_to_address(address=str(message.text.strip()), amount=str(1))
        #bot.send_message(message.chat.id, text="Весь баланс кошелька отправлен по этому адресу")
        #bot.send_message(message.chat.id, text=data_output_adress)
    elif data_output_is_valid == False:
        print("Error")
        #bot.send_message(message.chat.id, text="Адрес невалатилен")
    #bot.send_message(message.chat.id, text="Другой текст: " + str(message.text.strip()))


def mana_status():
    asdasdasd = 1
    print(asdasdasd)



@bot.message_handler(commands=["start"])
def start(m, res=False):
    answer = 'Добавляя этого бота вы обязутесь соблюдать все законы мира'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_Accept_user_agreement = types.KeyboardButton("Аккаунт")

    markup.add(item_Accept_user_agreement)
    speak.Speak(answer)
    bot.send_message(m.chat.id,answer , reply_markup=markup)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):

    data_base = pd.read_csv("base_log.txt")
    print(data_base.shape)
    print(data_base)



    btc_address = block_io_btc.get_my_addresses(labels=str(message.from_user.id))

    # print(data_ad_btc)

    data_btc = btc_address["data"]
    network_btc = data_btc["network"]
    addresses_btc = data_btc["addresses"]
    data_ad_btc = np.array(addresses_btc)
    print(data_ad_btc)
    user_btc = addresses_btc[0]
    user_id_btc = user_btc["user_id"]
    addresses_btc_user = user_btc["address"]
    label_btc_user = user_btc["label"]
    pending_received_balance_btc_user = user_btc["pending_received_balance"]
    available_balance_btc_user = user_btc["available_balance"]
    is_segwit_btc_user = user_btc["is_segwit"]

    total = my_accounts['total']
    total_currencies = my_accounts['currencies']
    bot.send_message(810299040,text=str(message.from_user.id) + " : " + str(message.text))
    bot.send_message(810299040, text=str(message.from_user.first_name) + " : " + str(message.text))
    data_price_base = block_io_btc.get_current_price(price_base="RUB")
    data_status_price_base = data_price_base['status']
    data_price_base = data_price_base['data']
    data_network_price_base = data_price_base['network']
    data_prices_price_base = data_price_base['prices']
    data = np.array(data_prices_price_base)
    datas = data[0]
    print(data_status_price_base)
    print(data_network_price_base)
    data_pay = datas['price']
    print("Курс BTC/USD : " + str(data_pay))
    full_ballance_base = float(data_pay) * float(available_balance_btc_user)
    bot.send_message(message.chat.id,"баланс админа в системе :" + str(available_balance_btc_user) + ", BTC \nв заморозке: " + str(pending_received_balance_btc_user) + "\nв RUB :" + str(full_ballance_base))
    # user_id = message.from_user.id
    # user_first_name = message.from_user.first_name
    # user_last_name = message.from_user.last_name
    # user_username = message.from_user.username

    data_logo = open("log.csv", "a")
    data_logo.write(str(message.from_user.id))
    data_logo.write(str(","))
    data_logo.write(str(message.from_user.first_name))
    data_logo.write(str(","))
    data_logo.write(str(message.from_user.last_name))
    data_logo.write(str(","))
    data_logo.write(str(message.from_user.username))
    data_logo.write(str(","))
    data_logo.write(str(message.text.strip()))
    data_logo.write(str(","))
    data_logo.write(str("\n"))
    data_logo.close()


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item_outputs_btc = types.KeyboardButton("купить бота")
    item_volue_remote = types.KeyboardButton("Разработка, обновления и новости")
    ietm_person = types.KeyboardButton("Аккаунт")

    markup.add(item_outputs_btc)
    markup.add(item_volue_remote)
    markup.add(ietm_person)
    total_balance_btc_nh = float(total['totalBalance'])
    full_data_balance_btc_1_2 =  total_balance_btc_nh + total_balance_btc
    full_ballance_rub = float(data_pay) * full_data_balance_btc_1_2



    bot.send_message(message.chat.id, "Баланс админа вне системы Майнинг : " + str(total['totalBalance']) + " BTC\n" + \
                     "Баланс админа вне системы Биржа : " + str(total_balance_btc) + " BTC\n" + \
                     "Баланс админа вне системы (М+Б) : " + str(full_data_balance_btc_1_2) + " BTC\n" + \
                     "(Google) Общий баланс в рублях : " + str(round(full_ballance_rub,2)) , reply_markup=markup)

    if message.text.strip() == 'Аккаунт':
        import os.path
        data_price_base = block_io_btc.get_current_price(price_base="RUB")
        data_status_price_base = data_price_base['status']
        data_price_base = data_price_base['data']
        data_network_price_base = data_price_base['network']
        data_prices_price_base = data_price_base['prices']
        data = np.array(data_prices_price_base)
        datas = data[0]
        print(data_status_price_base)
        print(data_network_price_base)
        #print(datas)

        for i in range(data.shape[0]):
            datas = data[i]
            data_pandas = pd.DataFrame()

            price_base = block_io_btc.get_current_price(price_base=datas['price_base'])
            exchange_price_base = price_base["data"]
            status_exchange_price_base = price_base["data"]
            network_exchange_price_base = status_exchange_price_base["network"]
            prices_network_exchange_price_base = status_exchange_price_base["prices"]

            #print(price_base)
            #print(exchange_price_base)
            #print(status_exchange_price_base)
            print(network_exchange_price_base)
            #print(prices_network_exchange_price_base.shape)

            prices_network_exchange_price_base = prices_network_exchange_price_base[0]
            print(prices_network_exchange_price_base)
            exchange_prices_network_exchange_price_base = prices_network_exchange_price_base['exchange']
            #print(exchange_prices_network_exchange_price_base)

            price_base_exchange_prices_network_exchange_price_base = prices_network_exchange_price_base['price_base']
            #print(price_base_exchange_prices_network_exchange_price_base)

            time_base_exchange_prices_network_exchange_price_base = prices_network_exchange_price_base['time']
            #print(time_base_exchange_prices_network_exchange_price_base)

            price_exchange_prices_network_exchange_price_base = prices_network_exchange_price_base['price']
            # print(exchange_prices_network_exchange_price_base)

            #bot.send_message(810299040, str(exchange_prices_network_exchange_price_base)+" "+str(price_base_exchange_prices_network_exchange_price_base))
            time.sleep(0)

        if os.path.isfile("base_log.txt") == False:
            print("файл не существует, база уничтожена")

        elif os.path.isfile("base_log.txt") == True:
                print("файл существует")
                ac_status = 0
                data = pd.read_csv("base_log.txt")
                print(data)
                for i in range(data.shape[0]):
                    data_ids = data["id"][i]
                    print(data_ids)
                    if data_ids == message.from_user.id:
                        ac_status = 1

                print(ac_status)
                if ac_status == 1:
                    print("аккаунт уже существует")
                    text_new_file_data_user = "файл в базе"

                    print(text_new_file_data_user)

                    btc_address = block_io_btc.get_my_addresses(labels=str(message.from_user.id))

                    # print(data_ad_btc)

                    data_btc = btc_address["data"]
                    network_btc = data_btc["network"]
                    addresses_btc = data_btc["addresses"]
                    data_ad_btc = np.array(addresses_btc)
                    print(data_ad_btc)
                    for i in range(data_ad_btc.shape[0]):
                        user_btc = addresses_btc[i]
                        user_id_btc = user_btc["user_id"]
                        addresses_btc_user = user_btc["address"]
                        label_btc_user = user_btc["label"]
                        if label_btc_user == str(message.from_user.id):
                            pending_received_balance_btc_user = user_btc["pending_received_balance"]
                            available_balance_btc_user = user_btc["available_balance"]
                            is_segwit_btc_user = user_btc["is_segwit"]
                            print([network_btc, user_id_btc, addresses_btc_user, label_btc_user,
                                   pending_received_balance_btc_user, available_balance_btc_user, is_segwit_btc_user])
                            """💼 Кошелек DOGE
                                            Баланс: 0 DOGE
                                            Примерно: 0 RUB
                                            Заблокировано: 0 DOGE
                                            За 195 дней вами проведено 0 успешных сделок на общую сумму 0 DOGE.
                                            🤝 Приглашено: 0 пользователей
                                            💰 Заработано: 0 DOGE
                                            Рейтинг: 👶 11.383
                                            Отзывы: (2) 👍 (0) 👎

                                            Верификация: ❌ Нет (чтобы пройти верификацию, нажмите на кнопку меню "Дополнительно")"""


                            prime_btcusd = float(available_balance_btc_user)*float(price_exchange_prices_network_exchange_price_base)
                            answer = "💼 Кошелек BTC пользователя " + message.from_user.first_name + "\n\n" +"Адрес кошелька BTC: " + addresses_btc_user + "\n"+ "Баланс: "+str(available_balance_btc_user)+" BTC \n" + "Примерно: "+ str(prime_btcusd) +" RUB \n" \
                                     + "Заблокировано: "+str(pending_received_balance_btc_user)+" BTC \n" + "\n\n" + "Получаеый курс с биржи : " + exchange_prices_network_exchange_price_base + "\nКурс BTC: " + price_exchange_prices_network_exchange_price_base + "\n" + "Курс BTCRUB: " + str(data_pay)
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                            item_outputs_btc = types.KeyboardButton("купить бота")
                            item_volue_remote = types.KeyboardButton("Разработка, обновления и новости")
                            ietm_person = types.KeyboardButton("Аккаунт")

                            markup.add(item_outputs_btc)
                            markup.add(item_volue_remote)
                            markup.add(ietm_person)

                            bot.send_message(message.chat.id, answer, reply_markup=markup)



                        #elif label_btc_user == str("default"):
                        #    pending_received_balance_btc_user = user_btc["pending_received_balance"]
                        #    available_balance_btc_user = user_btc["available_balance"]
                        #    is_segwit_btc_user = user_btc["is_segwit"]
                        #    print([network_btc, user_id_btc, addresses_btc_user, label_btc_user,
                        #           pending_received_balance_btc_user, available_balance_btc_user, is_segwit_btc_user])

                        else:
                            #block_io_btc.unarchive_addresses(labels=str(message.from_user.id))
                            #block_io_btc.archive_addresses(label=label_btc_user)
                            print("На этом месте было удаление адресов")


                elif ac_status == 0:
                    bot.send_message(message.chat.id,"📖 Регистрация пользователя 📖 \nТекст:" + message.text.strip() \
                                     + "\nот пользователя : " + message.from_user.first_name)

                    btc_new_address = block_io_btc.get_new_address(label=str(message.from_user.id))

                    print(btc_new_address)

                    text_new_file_data_user = "Такого пользователя не существует, начинаю создание"
                    print(text_new_file_data_user)

                    btc_address = block_io_btc.get_my_addresses(labels=str(message.from_user.id))
                    data_btc = btc_address["data"]
                    network_btc = data_btc["network"]
                    addresses_btc = data_btc["addresses"]
                    data_ad_btc = np.array(addresses_btc)
                    print(data_ad_btc.shape)
                    for i in range(data_ad_btc.shape[0]):
                        user_btc = addresses_btc[i]
                        user_id_btc = user_btc["user_id"]
                        addresses_btc_user = user_btc["address"]
                        label_btc_user = user_btc["label"]
                        if label_btc_user == str(message.from_user.id):
                            pending_received_balance_btc_user = user_btc["pending_received_balance"]
                            available_balance_btc_user = user_btc["available_balance"]
                            is_segwit_btc_user = user_btc["is_segwit"]

                            file_save_new_person = open("base_log.txt", "a")
                            file_save_new_person.write(str(user_id_btc)+ ",")
                            file_save_new_person.write(str(network_btc) + ",")
                            file_save_new_person.write(str(message.from_user.id) + ",")
                            file_save_new_person.write(str(message.from_user.first_name) + ",")
                            file_save_new_person.write(str(addresses_btc_user) + ",")
                            file_save_new_person.write(str(is_segwit_btc_user) + " ")
                            file_save_new_person.write("\n")
                            file_save_new_person.close()

                ac_status = 0

                print("Пользовательский id : " + str(message.from_user.id))


                answer = "\n\n" + "Спасибо за доверие " + str(message.from_user.first_name) + "\n\n" \
                             + "Ваш пользовательский id: " + str(message.from_user.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                item_outputs_btc = types.KeyboardButton("купить бота")
                item_volue_remote = types.KeyboardButton("Разработка, обновления и новости")
                ietm_person = types.KeyboardButton("Аккаунт")

                markup.add(item_outputs_btc)
                markup.add(item_volue_remote)
                markup.add(ietm_person)


                bot.send_message(message.chat.id, answer, reply_markup=markup)
    elif message.text.strip() == 'Разработка, обновления и новости':

        answer = "Обновление от 10.06.2023 №0.003 \n" \
                 "Добавлен вывод BTC\n"


        bot.send_message(message.chat.id, answer, reply_markup=markup)

        answer = "Обновление от 24.05.2023 №0.002 \n" \
                 "Добавлено автопривязывание кошельков BTC,DOGE,LTC  \n" \
                 "Добавлены кнопки ввода и вывода \n" \
                 "Разработка, обновления и новости\n" \
                 "Аккаунт"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item_outputs_btc = types.KeyboardButton("купить бота")
        item_volue_remote = types.KeyboardButton("Разработка, обновления и новости")
        ietm_person = types.KeyboardButton("Аккаунт")

        markup.add(item_outputs_btc)
        markup.add(item_volue_remote)
        markup.add(ietm_person)
        bot.send_message(message.chat.id, answer, reply_markup=markup)

        answer = "Обновление от 23.05.2023 №0.001 \n" \
                 "Добавлена кнопка Аккаунт\n" \
                 "Разработка, обновления и новости\n" \
                 "Аккаунт"

        bot.send_message(message.chat.id, answer, reply_markup=markup)

    elif message.text.strip() == 'купить бота':
        global name
        name = message.text
        btc_address = block_io_btc.get_my_addresses(labels=str(message.from_user.id))

        # print(data_ad_btc)

        data_btc = btc_address["data"]
        network_btc = data_btc["network"]
        addresses_btc = data_btc["addresses"]
        data_ad_btc = np.array(addresses_btc)
        print(data_ad_btc)
        for i in range(data_ad_btc.shape[0]):
            user_btc = addresses_btc[i]
            user_id_btc = user_btc["user_id"]
            addresses_btc_user = user_btc["address"]
            label_btc_user = user_btc["label"]
            if label_btc_user == str(message.from_user.id):
                pending_received_balance_btc_user = user_btc["pending_received_balance"]
                available_balance_btc_user = user_btc["available_balance"]
                is_segwit_btc_user = user_btc["is_segwit"]

                bot.send_message(message.chat.id, str(network_btc))
                bot.send_message(message.chat.id, str(data_ad_btc.shape[0]))
                bot.send_message(message.chat.id, str(user_btc))
                bot.send_message(message.chat.id, str(user_id_btc))
                bot.send_message(message.chat.id, str(addresses_btc_user))
                bot.send_message(message.chat.id, str(label_btc_user))
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('купить на 60cek.org', url="https://60cek.org/ru/?rid=16763895840434")
        texts = block_io_btc.get_address_balance(label=message.from_user.id)
        btn2 = types.InlineKeyboardButton('обменники', url="https://bestchange.ru")
        markup.add(btn1)
        markup.add(btn2)
        name = message.text
        bot.send_message(message.chat.id, text="Вы нажали на кнопку вывести, дальше должен быть адрес вывода", reply_markup=markup)
        # Как же сделать нормальный вывод
        bot.send_message(810299040, message.text)
        bot.register_next_step_handler(message, next_step_give_my_money)


    else:
        bot.send_message(message.chat.id," : " + message.text)
        if message.text.lower() == "привет":
            bot.send_message(message.chat.id, f"Привет , {message.from_user.last_name}, что нужно ? \n\n" + str(time.strftime("%Y-%m-%d %H:%M:%S")))

        print("Отсылаем юзеру сообщение в его чат")


        if message.text == 'перейти на site':
            bot.send_message(message.chat.id, 'website in open')
        else:
            btc_address = block_io_btc.get_my_addresses(labels=str(message.from_user.id))

            # print(data_ad_btc)

            data_btc = btc_address["data"]
            network_btc = data_btc["network"]
            addresses_btc = data_btc["addresses"]
            data_ad_btc = np.array(addresses_btc)
            print(data_ad_btc)
            for i in range(data_ad_btc.shape[0]):
                user_btc = addresses_btc[i]
                user_id_btc = user_btc["user_id"]
                addresses_btc_user = user_btc["address"]
                label_btc_user = user_btc["label"]
                if label_btc_user == str(message.from_user.id):
                    pending_received_balance_btc_user = user_btc["pending_received_balance"]
                    available_balance_btc_user = user_btc["available_balance"]
                    is_segwit_btc_user = user_btc["is_segwit"]

            bot.send_message(message.chat.id,f"Доступный баланс : {available_balance_btc_user}\n\nвведите сумму (комиссия 0.0001):")
            bot.send_message(810299040,message.text)

def next_step_give_my_money(message):
    bot.send_message(message.chat.id, "забираю всё в админку :" + message.text)
def next_step_handler2(message):
    # prepare the transaction




    # prepared_transaction = block_io_btc.prepare_transaction(from_labels=str(message.from_user.id), to_addresses="3BYdnTuuZwXvENq3XPAeD6gjPHxx72WhGw",amounts=aba_baise)
    # bot.send_message(message.chat.id,prepared_transaction)
    # summasdf = block_io_btc.summarize_prepared_transaction(prepared_transaction)
    # bot.send_message(message.chat.id, summasdf)
    # create the transaction and its signatures
    # created_transaction_and_signatures = block_io_btc.create_and_sign_transaction(prepared_transaction)
    # bot.send_message(message.chat.id, summasdf)
    # once satisfied with the data in created_transaction_and_signatures, submit it to Block.io for its signature and to broadcast to the peer-to-peer network
    # response = block_io_btc.submit_transaction(transaction_data=created_transaction_and_signatures)
    # print(">> Transaction ID:",response['data']['txid'])
    # you can check this on SoChain or any other blockchain explorer immediately"""

    bot.send_message(message.chat.id, 'Проверка баланса')
    print(block_io_btc.get_balance())
    data = block_io_btc.get_account_info()
    balance_address = block_io_btc.get_address_balance(labels=message.from_user.id)

    bot.send_message(message.chat.id, data["status"])
    data_data = data["data"]
    bot.send_message(message.chat.id, "Текущий тариф: " + str(data_data["current_plan"]))
    bot.send_message(message.chat.id, 'balance аккаунтa : ' + str(balance_address))
    bot.send_message(message.chat.id, 'перевод на аккаунт ')
    balance_address_data = balance_address['data']
    balance_address_data_ab = balance_address_data['available_balance']

    if float(balance_address_data_ab) >= float(0.000021):
            ##soz1 = block_io_btc.get_network_fee_estimate(amounts=float(balance_address_data_ab), to_addresses='3EbezHMCRWbH69WT1m9yjEanVbe4uFkiWo')
            ##print(soz1)
            # sozen = block_io_btc.prepare_transaction(amounts=str(balance_address_data_ab), from_labels=str(message.from_user.id),to_addresses=message.text,network_fee_estimate='high')
            print("yes")
            omission = block_io_btc.get_network_fee_estimate(amounts=str(balance_address_data_ab),to_addresses="3BYdnTuuZwXvENq3XPAeD6gjPHxx72WhGw")
            print(omission)
            aba_baise = str(available_balance_btc) - str(omission)
            print(aba_baise)
    elif float(balance_address_data_ab) <= float(0.000019):
            bot.send_message(message.chat.id, "balance_not_confirmed (min-0.002):" + str(balance_address_data_ab))







# Запускаем бота
bot.polling(none_stop=True, interval=0)
"""
https://t.me/+f1iGRTikaKgxZWRi

Канал
DK support
id: -1001910854574"""

"AgYAMX9jTKnKT_sA7CY6Llv0d9o9q7AoumzTAv8YdtMrZtAG_J7OoRjKrWwXRHo7" #Бинго мапс
