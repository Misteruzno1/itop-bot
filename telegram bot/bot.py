import asyncio
import os
from html import escape

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Tokenni to'g'ridan-to'g'ri emas, muhit o'zgaruvchisidan (Environment Variable) o'qiymiz
TOKEN = os.getenv("BOT_TOKEN", "9249551414:AAFxrZoJvu13RC0reyteiEuBTkakPEiwEbM")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    name = escape(message.from_user.full_name)

    text = (
        f"Assalomu alaykum, <b>{name}</b>! 👋\n\n"
        "🏪 <b>iTop Bozori</b> — har kim o'z do'konini ochadigan virtual bozor.\n"
        "• Bepul do'kon och, turini va nomini o'zing tanla\n"
        "• Vazifalar bajarib coin yig', qavat qur\n\n"
        "Boshlash uchun pastdagi tugmani bosing 👇"
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🏪 Bozorni ochish",
                callback_data="open_bazaar",
            )]
        ]
    )

    await message.answer(text, reply_markup=keyboard)


@dp.callback_query(F.data == "open_bazaar")
async def open_bazaar(callback: CallbackQuery):
    await callback.message.answer("🏪 Bozor tez orada ochiladi!")
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())