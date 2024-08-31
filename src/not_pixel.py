import aiohttp

class NotPixel():
    def __init__(self, telegramMiniAppInitData):
        self.headers = {
            "Authorization": telegramMiniAppInitData
        }

        self.session = aiohttp.ClientSession(
            base_url="https://notpx.app",
            headers=self.headers,
        )

    async def get_status():
        return NotImplemented

    async def get_pixel():
        return NotImplemented

    async def set_pixel():
        return NotImplemented

    async def claim():
        return NotImplemented