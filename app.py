from flask import Flask, render_template, request, redirect, url_for
from supabase import create_client
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

app = Flask(__name__)

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

BUCKET_NAME = "student-images"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "image" not in request.files:
        return "No image selected"

    image = request.files["image"]

    if image.filename == "":
        return "Please select an image"

    try:

        # Get file extension
        file_extension = os.path.splitext(image.filename)[1]

        # Create unique file name
        file_name = f"{uuid.uuid4()}{file_extension}"

        # Read image
        image_data = image.read()

        print("Uploading:", file_name)
        print("Content Type:", image.content_type)

        # Upload to Supabase Storage
        response = supabase.storage.from_(BUCKET_NAME).upload(
            file_name,
            image_data,
            file_options={
                "content-type": image.content_type,
                "upsert": "true"
            }
        )

        print("Supabase upload response:", response)

        # Get public URL
        public_url = supabase.storage.from_(
            BUCKET_NAME
        ).get_public_url(file_name)

        print("Public URL:", public_url)

        return render_template(
            "image.html",
            image_url=public_url,
            file_name=file_name
        )

    except Exception as e:

        print("UPLOAD ERROR:", repr(e))

        return f"Upload failed: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)