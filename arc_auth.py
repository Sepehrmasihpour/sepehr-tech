import httpx, time
from config import settings

_cache = {"token": None, "exp": 0}


async def get_access_token():
    now = time.time()
    if _cache["token"] and now < _cache["exp"] - 30:
        return _cache["token"]

    payload = {
        "client_id": settings.arc_client_id,
        "client_secret": settings.arc_client_secret,
        "grant_type": "client_credentials",
        "scope": "",
    }

    async with httpx.AsyncClient(base_url=settings.arc_base_url) as client:
        response = await client.post("/api/v1/auth/token", json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()["result"]
        _cache["token"] = data["accessToken"]
        _cache["exp"] = now + int(data.get("expiresIn", 3600))
        return _cache["token"]
