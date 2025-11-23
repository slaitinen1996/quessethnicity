import os
import json
import random

LOCAL_IMAGES_DIR = 'images-folder'
DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"ethnicities": [], "images": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_image_url(path):
    # Adjust if you later move images to Blob Storage
    return f"/images/{path}"
