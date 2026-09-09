from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return {
        "content" : "Wooden Block",
        "status": "In transit"
    }

@app.get("/shipment/{id}")
def get_shipment_by_ID(id: int) -> dict[str , Any]:
    return {
        "id": id,
        "content": "Wooden Block",
        "weight": 32.4,
        "status": "In transit"
    }

@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )