import json
import azure.functions as func
from ..shared import save_data

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        save_data(data)

        return func.HttpResponse(
            json.dumps({"success": True}),
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=400,
            mimetype="application/json"
        )
