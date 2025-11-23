import json
import azure.functions as func
from ..shared import load_data

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps(load_data()),
        mimetype="application/json"
    )
