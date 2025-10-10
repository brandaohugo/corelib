import httpx
import asyncio

async def login_and_get_user_async(email: str, password: str) -> dict:
    url = "http://localhost:8002/api/v1/users/login"  # Adjust as needed
    payload = {
        "email": email,
        "password": password
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()

def login_and_get_user(email: str, password: str) -> dict:
    """
    Synchronous wrapper for async function.
    Can be called from sync or async code.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # If we're in an event loop, the caller should use await directly!
        # Raise error or return coroutine:
        raise RuntimeError("login_and_get_user must be awaited in async contexts.")
        # Or: return login_and_get_user_async(email, password)
    else:
        # Safe to use asyncio.run in sync context
        return asyncio.run(login_and_get_user_async(email, password))

