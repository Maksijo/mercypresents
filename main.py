import asyncio  # для асинхронного запуска бота 
import logging # для настройки логгирования, которое поможет в отладке

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode #содержит настройки разметки сообщений (HTML, Markdown)
from aiogram.fsm.storage.memory import MemoryStorage # хранилища данных для состояний пользователей
from aiogram.utils.chat_action import ChatActionMiddleware

import config
from handlers import router # функционал нашего бота


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_router(router) #подключает к нашему диспетчеру все обработчики
    await bot.delete_webhook(drop_pending_updates=True) # удаляет все обновления, которые произошли после последнего завершения работы бота
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
