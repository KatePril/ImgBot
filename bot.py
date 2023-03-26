"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from decouple import config

from random import randint

API_TOKEN = config('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

list_of_images = ['photo', 'image', 'picture', 'drawing', 'painting']
categories = {'people' : ['people', 'person', 'family', 'coworker', 'co-worker', 'children', 'child', 'kid', 'student', 'human'], 'nature' : ['nature', 'environment', 'landscape', 'forest', 'exterior', 'lake', 'mountains'], 'space' : ['space', 'universe', 'star', 'sky', 'planet', 'galaxy', 'interstellar']}

def find_key_word(string, list):
    for word in list:
        if string.lower().find(word) != -1:
            return True
    return False

def open_photo(category):
    return open(f'images/{category}/{randint(1, 15)}.jpg', 'rb')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm ImgBot!\nPowered by aiogram.\nThere three categories of photos\n(space, people, nature)\nSend explenation of what you want to receive\n(you must include synonym of photo and synonym of the name of one of the categories)\ne.g. I want images of people")

@dp.message_handler()
async def echo(message: types.Message):
    if find_key_word(message.text, list_of_images):
        for key, value in categories.items():
            if find_key_word(message.text, value):
                await message.answer_photo(open_photo(key))
                break
        else:
            await message.answer('Sorry, no images for your request')
    else:
        await message.answer('Sorry, no images for your request')
 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)