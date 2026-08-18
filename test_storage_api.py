import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

bucket = "student-images"

api_url = f"{url}/storage/v1/object/list/{bucket}"

headers = {
    "Authorization": f"Bearer {key}",
    "apikey": key,
    "Content-Type": "application/json"
}

payload = {
    "prefix": "",
    "limit": 100,
    "offset": 0
}

response = requests.post(
    api_url,
    headers=headers,
    json=payload
)

print("Status:", response.status_code)
print("Response:", response.text)