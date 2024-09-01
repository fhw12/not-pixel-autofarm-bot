from models.user_status import UserStatus

import aiohttp

class NotPixel():
    def __init__(self, telegram_mini_app_init_data, user_agent):
        self.headers = {
            "Authorization": telegram_mini_app_init_data,
            "User-Agent": user_agent,
        }

        self.session = aiohttp.ClientSession(
            base_url="https://notpx.app",
            headers=self.headers,
        )

    async def get_status(self) -> UserStatus | None:
        user_status_raw = await self.session.request(
            url="/api/v1/mining/status",
            method="GET",
        )

        if user_status_raw.status != 200:
            return None

        user_status = await user_status_raw.json()

        status_model = UserStatus(
            coins = user_status['coins'],
            claimed = user_status['claimed'],
            total_user_pixels = user_status['totalUserPixels'],
            user_balance = user_status['userBalance'],
            charges = user_status['charges'],
            max_charges = user_status['maxCharges'],
        )

        return status_model

    async def get_pixel(self):
        return NotImplemented

    async def set_pixel(self, pixel_id, color):
        return NotImplemented

    async def claim(self):
        return NotImplemented