import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TOKEN_URL = os.getenv("TOKEN_URL")
SCOPE = os.getenv("SCOPE")

def get_auth_token():
    """
    Fetch the authentication token from the API.

    Returns:
        str: The access token.
    """
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': SCOPE
    }
    response = requests.post(TOKEN_URL, data=payload)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json().get("access_token")
