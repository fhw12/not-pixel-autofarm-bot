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