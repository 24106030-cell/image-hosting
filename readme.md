# IBM Cloud Image Hosting

A simple image upload application built with **Flask** and **Supabase Storage**.

## Technologies

* Python
* Flask
* Supabase
* python-dotenv

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/udhayasankar-UD/IBM-Cloud-Image-Hosting.git
cd IBM-Cloud-Image-Hosting
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install Flask supabase python-dotenv
```

### 4. Create `.env`

Create a `.env` file in the project folder:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

1. Create a Supabase project

Create a project in Supabase.

2. Create a Storage bucket

Go to:

Supabase Dashboard
→ Storage
→ New Bucket

Create a bucket named:

IBM

The bucket name must match the value in app.py:

BUCKET_NAME = "IBM"
3. Configure the bucket

If you want to display uploaded images using a public URL, make the IBM bucket public.

Go to:

Storage → IBM → Configuration

and enable public access.

Storage Policy

The Flask application needs permission to upload files to the bucket.

Open:

Supabase Dashboard
→ SQL Editor

Run:

create policy "Allow IBM uploads"
on storage.objects
for insert
to public
with check (
    bucket_id = 'IBM'
);

This allows files to be uploaded to the IBM bucket.

Environment Variables

Create a .env file in the root of the project:

SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_KEY

You can find the required Supabase information in:

Supabase Dashboard
→ Project Settings
→ API

Do not upload your .env file to GitHub.

## Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
cloud-image-Hosting/
│
├── templates/
│   ├── index.html
│   └── image.html
│
├── .env
├── .gitignore
├── app.py
└── README.md
```

## Features

* Upload images
* Store images in Supabase Storage
* Generate unique filenames
* Display uploaded images
* Flask backend

## Important

Do not upload `.env` to GitHub because it contains your Supabase credentials.

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
```
