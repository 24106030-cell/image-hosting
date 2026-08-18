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

### 5. Supabase Storage

Create a Storage bucket named:

```text
IBM
```

Configure the Storage policies to allow image uploads.

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
