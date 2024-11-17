from configT import pass_gen
import telebot
import random
password = ''
data_text = []
bad = ['Привет', 'Сам такой', 'лол', 'Ответить норм не можешь', 'Э', 'Ты чо', 'Афигел',  'Чо не можешь?',  'Да', 
'Нет',  'Так я не экаю', 'Ичо', 'Хахахаха', 'Смешно да?', 'Э', 'Кончено', 'Конечно да',  'Сам', 'Лол', 'Так ты сам так говорил']

bot = telebot.TeleBot('8101211575:AAHRNzkkyxC1MKcQcaW1TdjT9OcNYNB-hKI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['getpass'])
def gen_pass_tg(message):
    bot.reply_to(message,pass_gen(10))
      
    
@bot.message_handler(commands=['numgen'])
def gen_num(message):
    numrand = random.randint(1,10000000)
    bot.reply_to(message,numrand)

    




@bot.message_handler(func=lambda message: True)
def echo_message(message):
    data_text.append(message.text)
    print(data_text)
    rand_text = random.choice(data_text)
    print(rand_text)
    chance = random.randint(1,2)
    if chance == 1:
        bot.reply_to(message,rand_text)
    elif chance == 2:
        rand_bad = random.choice(bad)
        print(bad)
        bot.reply_to(message,rand_bad)
    


    
bot.infinity_polling()