import httpx
from config import settings
import time
from models import (
    createPaymentReq,
    createPaymentResponse,
    deletePaymentRequest,
    startPaymentReq,
    verifyPaymentReq,
    VerifyPaymentResponse,
    reversePaymentReq,
    reversePaymentResponse,
)

BASE_URL = settings.payping_base_url
HEADER = {"Authorization": f"Token {settings.payping_api_token}"}


async def create_payment_request(req: createPaymentReq):
    payload = req.model_dump(by_alias=True)
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.post("/v3/pay", json=payload)
        response.raise_for_status()
        data = response.json()
        return createPaymentResponse(
            payment_code=data.get("paymentCode", ""),
            return_url=data.get("returnUrl", ""),
            amount=data.get("amount"),
        )


async def delete_payment(req: deletePaymentRequest):
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.delete("/v3/delete", params=req.code)
        response.raise_for_status()
        data = response.json()
        return data


async def start_payment(req: startPaymentReq):
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        response = await client.get(f"/v3/pay/start/{req.code}")
        response.raise_for_status()
        data = response.json()
        return data


async def verify_payment(req: verifyPaymentReq):
    payload = req.model_dump(by_alias=True)
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.post("/v3/pay/verify", json=payload)
        response.raise_for_status()
        data = response.json()
        return VerifyPaymentResponse(**data)


async def reverse_payment(req: reversePaymentReq):
    payload = req.model_dump(by_alias=True)
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.post("/v3/pay/reverse", json=payload)
        response.raise_for_status()
        data = response.json()
        return reversePaymentResponse(**data)


async def withdraw(amount: int):
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.post(f"/v1/withdraw/{amount}")
        response.raise_for_status()
        data = response.json()
        return data


async def get_withdraw_details(code: str):
    async with httpx.AsyncClient(base_url=BASE_URL, headers=HEADER) as client:
        response = await client.get(f"/v1/withdraw/{code}")
        response.raise_for_status()
        data = response.json()
        return data
