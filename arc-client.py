import httpx
from models import getAccountBalanceResponse
from config import settings
from arc_auth import get_access_token

BASE_URL = settings.arc_base_url
ACOUNT_NUMBER = settings.bank_acount_number


async def _auth_headers():
    return {"Authorization": f"Bearer {await get_access_token()}"}


async def get_acount_balance():
    headers = await _auth_headers()
    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers) as client:
        response = await client.get(f"/api/v1/accounts/{ACOUNT_NUMBER}/balance")
        response.raise_for_status()
        data = response.json()
        return getAccountBalanceResponse(
            availableBalance=data["availableBalance"],
            actualBalance=data["actualBalance"],
        )
