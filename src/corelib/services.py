import requests


def login_and_get_user(email: str, password: str) -> dict | None:
    """
    Perform a sync login request and return only user data as dict.
    Returns None if login fails (invalid credentials or server error).
    """
    url = "http://auth-users:8000/api/v1/users/login"  # Use Docker service name and internal port
    payload = {
        "email": email,
        "password": password
    }
    try:
        resp = requests.post(url, json=payload, timeout=5)
        resp.raise_for_status()
        result = resp.json()
        # Return only the user data as dict
        return result
    except requests.HTTPError as err:
        # Optional: inspect err.response for API error details
        print(f"Login failed: {err}")
    except requests.RequestException as err:
        print(f"Error connecting to auth-users: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None

