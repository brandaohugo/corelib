import httpx


async def fetch_user_by_username(username: str) -> dict:
    url = f"http://auth-users:8000/api/v1/users/by-username/{username}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()
