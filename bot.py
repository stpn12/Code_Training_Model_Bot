import logging
from aiogram import Bot, Dispatcher, executor, types
import antifakesearcher

bot = Bot(token="")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование
logging.basicConfig(level=logging.INFO)

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь")
    ])

# Хэндлер на команду /start
@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    await set_default_commands(dp)
    await message.answer("Добро пожаловать! Я бот для проверки новостей на фейки. Просто отправьте мне сообщение")

#Стандартная обработка
@dp.message_handler()
async def message_handler(message: types.Message):
    text = message.text
    print(message.from_user.first_name, ':', text)

    try:
        r = antifakesearcher.predict_proba(str(text))
        await message.answer(f'Вероятность содержания фейковой информации:{round(r[1] * 100, 2)}%')
    except TypeError as e:
        print(e)
        await message.answer('Ошибка чтения :(')

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)



