import telebot

bot = telebot.TeleBot('6843637773:AAFXvxu45Ax6cVgY7eNK1frE5TxO4MvPf6w')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Выберите команду с нужным писателем', parse_mode='Markdown')


@bot.message_handler(commands=['command1'])
def main(message):
    bot.send_message(message.chat.id, text='Сказка о Царе Салтане\n Царь Салтан\n 1831', parse_mode='Markdown')


@bot.message_handler(commands=['command2'])
def main(message):
    bot.send_message(message.chat.id, text='Преступление и наказание\n Раскольников\n 1866', parse_mode='Markdown')


@bot.message_handler(commands=['command3'])
def main(message):
    bot.send_message(message.chat.id, text='Муму\n Герасим\n 1852', parse_mode='Markdown')


@bot.message_handler(commands=['command4'])
def main(message):
    bot.send_message(message.chat.id, text='На дне\n Костылев\n 1902', parse_mode='Markdown')


@bot.message_handler(commands=['command5'])
def main(message):
    bot.send_message(message.chat.id, text='Вишневый сад\n Раневская\n 1903', parse_mode='Markdown')


@bot.message_handler(commands=['command6'])
def main(message):
    bot.send_message(message.chat.id, text='Шинель\n Акакий\n 1841', parse_mode='Markdown')


@bot.message_handler(commands=['command7'])
def main(message):
    bot.send_message(message.chat.id, text='Горе от ума\n Чацкий\n 1822', parse_mode='Markdown')


bot.infinity_polling()