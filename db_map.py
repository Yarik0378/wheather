import telebot
import pyowm

bot = telebot.TeleBot(token)
# observation = owm.weather_at_place(message.text)
owm = pyowm.OWM('681470a570d9bac8906681a35c08ce1d', language="ua")

@bot.message_handler(commands=['help'])
def after_send(message):
    bot.send_message(message.chat.id, "Hello, i'm bot for geting wheather in your city")

@bot.message_handler(commands=['start'])
def how_city(message):
    bot.send_message(message.chat.id, "Вкажіть ваше місто ", )

@bot.message_handler(content_types="[text]")
def abs(message):
    try:
        observation = owm.weather_at_place(message.text)
        global w
        w = observation.get_weather()
        global temp
        temp = w.get_temperature()['temp']
        global fahrenheit
        global celsius
        fahrenheit = 9 / 5 * (temp - 273) + 32
        celsius = (fahrenheit - 32) * 5 / 9
        bot.send_message(message.chat.id, "На даний момент тепература у місті " + message.text + "-"  + str(int(celsius)) + "°C")
        bot.send_message(message.chat.id, + w.get_detailed_status())
    except:
        pass
    if message.text == "dick":
        bot.send_message(message.chat.id,"Ти долбойоб")

upd = bot.get_updates()
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)
bot.polling()


























# while True:
#     bot.send_message(506729279, "fuck")
#

# bot.polling()
