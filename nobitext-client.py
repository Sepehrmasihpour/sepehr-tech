import httpx
from config import settings
from models import (
    nobitextBalanceReq,
    nobitextTransactionsReq,
    nobitextTransactionsResponse,
    nobitextDepositsReq,
    nobitextDepositsResponse,
)

HEADER = {"Authorization": f"Token {settings.nobitex_auth_token}"}
BASE_URL = settings.nobitex_base_url


async def get_currency_balance(req: nobitextBalanceReq):
    pay_load = req.model_dump()
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.post("/users/wallets/balance", json=pay_load)
        response.raise_for_status()
        data = response.json()
        return data.get("amount")


async def get_wallet_transaction_list(req: nobitextTransactionsReq):
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        params = req.model_dump(by_alias=True)
        response = await client.get("/users/wallets/transactions/list", params=params)
        response.raise_for_status()
        data = response.json()
        nobitextTransactionsResponse(**data)


async def nobitext_deposits_req(req: nobitextDepositsReq):
    params = req.model_dump(by_alias=True)
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.get("/users/wallets/deposits/list", params=params)
        response.raise_for_status()
        data = response.json()
