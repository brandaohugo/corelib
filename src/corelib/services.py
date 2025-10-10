import httpx


async def login_and_get_user(email: str, password: str) -> dict:
    url = "http://auth-users:8002/api/v1/login/access-token"  # Adjust port and host as needed for your docker setup
    payload = {
        "email": email,
        "password": password
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload)
        resp.raise_for_status()
        result = resp.json()
        # Assuming user data is returned directly as a dict
        return result

