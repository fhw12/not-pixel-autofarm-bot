import asyncio

from not_pixel import NotPixel
from autofarm import autofarm
import config

async def main():
    not_pixel = NotPixel(
        telegram_mini_app_init_data=config.TELEGRAM_MINI_APP_INIT_DATA,
        user_agent=config.USER_AGENT,
    )

    await autofarm(not_pixel=not_pixel)

if __name__ == "__main__":
    asyncio.run(main())