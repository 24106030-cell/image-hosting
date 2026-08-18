from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

BUCKET_NAME = "student-images"

print("Connected to Supabase")

try:
    result = supabase.storage.from_(BUCKET_NAME).list()

    print("Bucket access successful")
    print(result)

except Exception as e:
    print("Bucket test failed:")
    print(repr(e))