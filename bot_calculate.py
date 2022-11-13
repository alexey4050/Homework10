import telebot
from telebot import types

TOKEN = "YOUR_TOKEN_COD"
bot = telebot.TeleBot(TOKEN)

value = ''
old_value = ''

keyboard = telebot.types.InLineKeyboardMarkup()
keyboard.row(telebot.InLineKeyboardButton(' ', callback_data='no'),
             telebot.InLineKeyboardButton('C', callback_data='C'),
             telebot.InLineKeyboardButton('<=', callback_data='<='),
             telebot.InLineKeyboardButton('/', callback_data='/'))
keyboard.row(telebot.InLineKeyboardButton('7', callback_data='7'),
             telebot.InLineKeyboardButton('8', callback_data='8'),
             telebot.InLineKeyboardButton('9', callback_data='9'),
             telebot.InLineKeyboardButton('*', callback_data='*'))
keyboard.row(telebot.InLineKeyboardButton('4', callback_data='4'),
             telebot.InLineKeyboardButton('5', callback_data='5'),
             telebot.InLineKeyboardButton('6', callback_data='6'),
             telebot.InLineKeyboardButton('-', callback_data='-'))
keyboard.row(telebot.InLineKeyboardButton('1', callback_data='1'),
             telebot.InLineKeyboardButton('2', callback_data='2'),
             telebot.InLineKeyboardButton('3', callback_data='3'),
             telebot.InLineKeyboardButton('+', callback_data='+'))
keyboard.row(telebot.InLineKeyboardButton(' ', callback_data=' '),
             telebot.InLineKeyboardButton('0', callback_data='0'),
             telebot.InLineKeyboardButton(',', callback_data=','),
             telebot.InLineKeyboardButton('=', callback_data='='))

@bot.massage_handler(commands=['start', 'go'])
def getMassege(massege):
    global value
    if value == '':
        bot.send_massege(massege.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_massage(massege.from_user.id, value, reply_markup=keyboard)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_fubc(query):
    global value, old_value
    data = query.data
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        value = str(eval(value))
    else:
        value += data
    if value != old_value:
        if value == '':
            bot.edit_massege_text(
                chat_id=query.massege.chat.id, massage_id=query.massege.chat.id, text='0', reply_markup=keyboard)
        else:
            bot.edit_massege_text(chat_id=query.massege.chat.id,
                                  massege_id=query.massege.id, text=value, realy_markup=keyboard)
            old_value = value
            
bot.polling()
    

             
