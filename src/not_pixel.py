from models.user_status import UserStatus
from models.repaint import Repaint
from models.claim import Claim
from models.pixel import Pixel

from random import randint
import aiohttp

class NotPixel():
    def __init__(self, telegram_mini_app_init_data, user_agent):
        self.headers = {
            'Authorization': f'initData {telegram_mini_app_init_data}',
            'User-Agent': user_agent,
        }

        self.session = aiohttp.ClientSession(
            base_url='https://notpx.app',
            headers=self.headers,
        )

        self.map_width = 1000

    async def get_status(self) -> UserStatus | None:
        user_status_raw = await self.session.request(
            url='/api/v1/mining/status',
            method='GET',
        )

        if user_status_raw.status != 200:
            return None

        user_status = await user_status_raw.json()

        status_model = UserStatus(
            coins = user_status['coins'],
            claimed = user_status['claimed'],
            repaints_total = user_status['repaintsTotal'],
            user_balance = user_status['userBalance'],
            charges = user_status['charges'],
            max_charges = user_status['maxCharges'],
        )

        return status_model

    async def get_pixel(self, pixel_id: int) -> Pixel | None:
        pixel_raw = await self.session.request(
            url=f'/api/v1/image/get/{pixel_id}',
            method='GET',
        )

        if pixel_raw.status != 200:
            return None

        pixel = await pixel_raw.json()

        pixel_model = Pixel(
            x=pixel['pixel']['x'],
            y=pixel['pixel']['y'],
            owner_id=pixel['pixel']['ownerId'],
            repaints=pixel['pixel']['repaints'],
            color=pixel['pixel']['color'],
            date_obtained=pixel['pixel']['dateObtained'],
        )

        return pixel_model

    async def get_pixel_by_coords(self, x: int, y: int) -> Pixel | None:
        return await self.get_pixel(self.map_width * y + (x + 1))

    async def set_pixel(self, pixel_id: int, new_color: str) -> Repaint | None:
        repaint_raw = await self.session.request(
            url='/api/v1/repaint/start',
            method='POST',
            json={'pixelId': pixel_id, 'newColor': new_color},
        )

        if repaint_raw.status != 200:
            return None

        repaint = await repaint_raw.json()

        repaint_model = Repaint(
            balance=repaint['balance']
        )

        return repaint_model

    async def set_random_pixel(self) -> Repaint | None:
        return await self.set_pixel(
            pixel_id=randint(1, 1000 * 1000),
            new_color='#e46e6e',
        )

    async def claim(self) -> Claim | None:
        claim_raw = await self.session.request(
            url='/api/v1/mining/claim',
            method='GET',
        )

        if claim_raw.status != 200:
            return None

        claim = await claim_raw.json()

        claim_model = Claim(
            claimed=claim['claimed']
        )

        return claim_model