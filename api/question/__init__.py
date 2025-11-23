import json
import random
import azure.functions as func
from ..shared import load_data, get_image_url

def main(req: func.HttpRequest) -> func.HttpResponse:
    data = load_data()

    if not data['images'] or not data['ethnicities']:
        return func.HttpResponse(
            json.dumps({"error": "No data available. Please add images and ethnicities first."}),
            status_code=404,
            mimetype="application/json"
        )

    image = random.choice(data['images'])
    correct_ethnicity = image['ethnicity']
    correct_index = image['order']

    if correct_index < 0 or correct_index >= len(data['ethnicities']):
        return func.HttpResponse(
            json.dumps({"error": "Invalid order value in data.json."}),
            status_code=400,
            mimetype="application/json"
        )

    options = [
        {"label": correct_ethnicity, "is_correct": True}
    ]

    if len(data['ethnicities']) > 1:
        if correct_index == 0:
            neighbor_index = 1
        elif correct_index == len(data['ethnicities']) - 1:
            neighbor_index = len(data['ethnicities']) - 2
        else:
            neighbor_index = correct_index + random.choice([-1, 1])

        neighbor = data['ethnicities'][neighbor_index]
        options.append({"label": neighbor, "is_correct": False})

    random.shuffle(options)

    return func.HttpResponse(
        json.dumps({
            "image_url": get_image_url(image['path']),
            "options": options,
            "correct_answer": correct_ethnicity
        }),
        mimetype="application/json"
    )
