import os
import telebot
from dotenv import load_dotenv
from threading import Event

from src.core.corebusiness import send_waifu, send_horoscope
from src.keyboard.keyboard_list import create_waify_category_keyboard, create_sfw_category_keyboard, \
    create_nsfw_category_keyboard, create_zodiac_keyboard, create_date_keyboard, category_type, zodiac_signs



# Load environment variables from .env file
load_dotenv('token.env')

# Access the BOT_TOKEN environment variable
bot_token = os.getenv('BOT_TOKEN')

if bot_token is None:
    raise ValueError("BOT_TOKEN environment variable not found in token.env")

# Create an instance of the TeleBot class
bot = telebot.TeleBot(bot_token)

# Create an event to signal when to stop the bot
stop_event = Event()

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['waifu'])
def select_category(message):
    keyboard = create_waify_category_keyboard()
    bot.reply_to(message, "Please select the category:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() in category_type)
def select_type_category(message):
    category = message.text.lower()
    if category == 'sfw':
        keyboard = create_sfw_category_keyboard()
    else:
        keyboard = create_nsfw_category_keyboard()
        bot.reply_to(message, " Ah zozzo, ti piace il nsfw eh?")
    bot.reply_to(message, f"You selected {category.capitalize()}. Please select the category:", reply_markup=keyboard)
    bot.register_next_step_handler(message, send_waifu, category, bot)

@bot.message_handler(commands=['horoscope'])
def select_zodiac_sign(message):
    keyboard = create_zodiac_keyboard()
    bot.reply_to(message, "Please select your zodiac sign:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() in zodiac_signs)
def ask_for_day(message):
    sign = message.text.lower()
    keyboard = create_date_keyboard()
    bot.reply_to(message, f"You selected {sign.capitalize()}. Please select the day:", reply_markup=keyboard)
    bot.register_next_step_handler(message, send_horoscope, sign, bot)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "/start or /hello - Greet the user\n"
        "/horoscope - Get the daily horoscope\n"
        "/exit - Stop the bot\n"
        "/help - Show this help message\n"
        "/waifu - Get a waifu image"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['exit'])
def closebot(message):
    bot.reply_to(message, "Congratulazioni hai spento il bot, ora vai a fare qualcosa di utile")
    stop_event.set()

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text + ", molto interessante ma non mi interessa")





# Start polling in a separate thread
import threading

polling_thread = threading.Thread(target=bot.infinity_polling, kwargs={'timeout': 10, 'long_polling_timeout': 5})
polling_thread.start()

# Wait for the stop event
stop_event.wait()

# Stop the bot
bot.stop_polling()
polling_thread.join()
