# List of valid zodiac signs
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

zodiac_signs = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]
sfw_category = [
    'waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry',
    'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet',
    'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite',
    'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance',
    'cringe'
]
nsfw_category = [
    'waifu','neko','trap','blowjob']
category_type = ['sfw','nsfw']

# Create a custom keyboard with zodiac sign buttons
def create_zodiac_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [KeyboardButton(sign.capitalize()) for sign in zodiac_signs]
    keyboard.add(*buttons)
    return keyboard

# Create a custom keyboard with date options
def create_date_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [KeyboardButton("Today"), KeyboardButton("Tomorrow"), KeyboardButton("Yesterday")]
    keyboard.add(*buttons)
    return keyboard

def create_waify_category_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [KeyboardButton(sign.capitalize()) for sign in category_type]
    keyboard.add(*buttons)
    return keyboard

def create_sfw_category_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [KeyboardButton(sign.capitalize()) for sign in sfw_category]
    keyboard.add(*buttons)
    return keyboard

def create_nsfw_category_keyboard():
    keyboard = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = [KeyboardButton(sign.capitalize()) for sign in nsfw_category]
    keyboard.add(*buttons)
    return keyboard