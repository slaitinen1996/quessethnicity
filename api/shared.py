import os
import json
import random

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
LOCAL_IMAGES_DIR = os.path.join(os.path.dirname(__file__), "../static/images")

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"ethnicities": [], "images": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_image_url(path):
    return f"/images/{path}"
