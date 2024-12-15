#!/bin/bash

# Aktivasi environment Python (Opsional, jika Anda menggunakan virtual environment)
# source venv/bin/activate

# Menjalankan aplikasi Flask dengan Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
