import httpx


async def fetch_user_by_username(username: str) -> dict:
    url = f"http://auth-users:8002/api/v1/users/read-user/{username}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        result = resp.json()
        # Assuming the user data is directly in the response or under "data"
        if isinstance(result, dict):
            # Adjust key as needed if your user data is wrapped, e.g. result["data"]
            return result.get("data", result)
        return result
