import os
import requests

def get(endpoint, params):
    base_url = os.getenv('KISEKI_URL')
    api_key = os.getenv('API_KEY')
    url = f"{base_url}/api/periwinkle/{endpoint}"
    headers = { "Authorization": api_key }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}