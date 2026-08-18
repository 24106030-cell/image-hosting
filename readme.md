# IBM Cloud Image Hosting

A simple image upload application built with **Flask** and **Supabase Storage**.

## Technologies

* Python
* Flask
* Supabase
* python-dotenv

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/udhayasankar-UD/IBM-Cloud-Image-Hosting.git
cd IBM-Cloud-Image-Hosting
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install Flask supabase python-dotenv
```

### 4. Create `.env` File

Create a `.env` file in the project root:

```env
SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_KEY
```

You can find these values in:

**Supabase Dashboard → Project Settings → API**

> Never upload the `.env` file to GitHub.

---

## Supabase Storage Setup

### 1. Create a Supabase Project

Create a project from the Supabase Dashboard.

### 2. Create a Storage Bucket

Go to:

**Supabase Dashboard → Storage → New Bucket**

Create a bucket named:

```text
IBM
```

The bucket name must match the value in `app.py`:

```python
BUCKET_NAME = "IBM"
```

### 3. Make the Bucket Public

If you want uploaded images to be accessible using a public URL:

**Storage → IBM → Configuration → Public bucket**

Enable public access.

---

## Storage Policy

The Flask application needs permission to upload images to the `IBM` bucket.

Go to:

**Supabase Dashboard → SQL Editor**

Run:

```sql
create policy "Allow IBM uploads"
on storage.objects
for insert
to public
with check (
    bucket_id = 'IBM'
);

create policy "Allow IBM select"
on storage.objects
for select
to public
using (
    bucket_id = 'IBM'
);

create policy "Allow IBM updates"
on storage.objects
for update
to public
using (
    bucket_id = 'IBM'
)
with check (
    bucket_id = 'IBM'
);
```

---

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and go to:

```text
http://127.0.0.1:5000
```

---

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

---

## Features

* Upload images
* Store images in Supabase Storage
* Generate unique filenames
* Display uploaded images
* Flask backend

---

## `.gitignore`

Make sure your `.gitignore` contains:

```text
.env
.venv/
__pycache__/
*.pyc
```

This prevents your Supabase credentials and virtual environment from being uploaded to GitHub.

## Important

**Never commit your `.env` file or Supabase secret/service-role key to GitHub.**
