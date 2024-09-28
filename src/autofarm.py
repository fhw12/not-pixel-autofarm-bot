from models.user_status import UserStatus
from models.repaint import Repaint
from models.claim import Claim
from not_pixel import NotPixel
from random import randint
import asyncio
import time

def time_now():
    now = time.time()
    time_localtime = time.localtime(now)
    return time.strftime("%H:%M:%S", time_localtime)

async def autofarm(not_pixel: NotPixel):
    while True:
        user_status: UserStatus = await not_pixel.get_status()

        if user_status is None:
            print(f'[{time_now()}] Failed to get user status')
            print(f'[{time_now()}] Waiting for 10 seconds to try again')
            await asyncio.sleep(10)
            continue

        print(f'[{time_now()}] Energy: {user_status.charges}/{user_status.max_charges} | Your pixels: {user_status.repaints_total} | Your balance: {user_status.user_balance}')

        if randint(0, 10) == 0:
            print(f'[{time_now()}] Trying to claim')
            claim: Claim = await not_pixel.claim()
            if claim is not None:
                print(f'[{time_now()}] Claimed: {claim.claimed}')
            else:
                print(f'[{time_now()}] Failed to claim')

        if user_status.charges <= 0:
            print(f'[{time_now()}] Waiting for 3 minutes')
            await asyncio.sleep(randint(3 * 60, 3 * 60 + 30))
            continue

        repaint: Repaint = await not_pixel.set_random_pixel()

        if repaint is None:
            print(f'[{time_now()}] Failed to set pixel')
        else:
            print(f'[{time_now()}] Pixel is set')
            await asyncio.sleep(randint(3, 5))