
import logging
from aiogram import Bot, Dispatcher, executor, types

from oxfordlookup import getDefinitions
from googletrans import Translator

print('Main.py ishladi')
translator  = Translator()
API_TOKEN = '5265821070:AAECJWJZD-VhWqth8KN7oyytp5lr_f7PU4E'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Translate botimga xush !!! Siz o'zbekcha yozing va men inglizchaga tarjima qilaman va so'zlarni definition larini topib beraman, mazza qilib foydalaning😉😉😉")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang  = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en ' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang=="en":
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest="en").text
        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z topilmadi❓❓❓❓❓")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)