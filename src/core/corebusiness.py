
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from src.service.horoscope import get_daily_horoscope
from src.service.waifu import get_waifu


def send_horoscope(message, sign, bot):
    try:
        day = message.text.strip().lower()
        horoscope = get_daily_horoscope(sign, day)
        bot.reply_to(message, f"Horoscope for {sign.capitalize()}: {horoscope['data']['horoscope_data']}",
                     reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}", reply_markup=ReplyKeyboardRemove())
        bot.reply_to(message, f"Il comando è /horoscope <segno> (In inglese) <giorno> (YYYY-MM-DD)")


def send_waifu(message, categoryType, bot):
    try:
        category = message.text.strip().lower()
        print("ID: " + str(message.from_user.id))
        print("Name: " + message.from_user.first_name + (
            " Surname: " + str(message.from_user.last_name) if message.from_user.last_name != None else ""))
        print("Username: " + message.from_user.username)
        print("The category is: ", category)
        print("The category Type is: ", categoryType)
        waifu = get_waifu(categoryType, category)
        print("The generated image is: " + waifu['url'])
        bot.reply_to(message, f"Here is your waifu: {waifu['url']}",
                     reply_markup=ReplyKeyboardRemove())
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}", reply_markup=ReplyKeyboardRemove())
        bot.reply_to(message, f"Il comando è /waifu <sfw/nsfw> <categoria>")
