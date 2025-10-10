import requests


def read_me(email: str, password: str) -> dict | None:
    """
    Log in to get an access token, then fetch user data from /users/me endpoint.
    Returns user data dict, or None if any step fails.
    """
    # 1. Login to get token
    url_token = "http://auth-users:8000/api/v1/login/access-token"
    payload = {
        "username": email,      # must be "username", not "email"
        "password": password
    }
    try:
        resp = requests.post(
            url_token,
            data=payload,
            timeout=5
        )
        resp.raise_for_status()
        # Note: spelling fix for "access_token"
        token = resp.json()["access_token"]
    except Exception as err:
        print(f"Login failed: {err}")
        return None

    # 2. Use token to call /users/me (or /me)
    url_me = "http://auth-users:8000/api/v1/users/me"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        resp = requests.get(url_me, headers=headers, timeout=5)
        resp.raise_for_status()
        return resp.json()
    except Exception as err:
        print(f"Fetching user data failed: {err}")
        return None


