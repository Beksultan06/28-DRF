from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging, os
from dotenv import load_dotenv

load_dotenv()


ADMIN_ID = os.environ.get("ADMIN_ID")

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Бот готов принимать уведомление!")


async def send_car_notification(car_data: dict):
    text = (
        f"Added new car!\n\n"
        f"Owner : {car_data.get('user')}\n"
        f"Brand : {car_data.get('brand')}\n"
        f"Model : {car_data.get('model')}\n"
        f"Number : {car_data.get('number')}\n"
        f"Date : {car_data.get('date')}\n"
        f"KPP : {car_data.get('carabka_transfer')}\n"
        f"Type : {car_data.get('type_car')}\n"
        f"Probeg : {car_data.get('Probeg')}\n"
    )
    await bot.send_message(ADMIN_ID, text)

async def main():
    print("Starting Bot")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())