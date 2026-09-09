from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

shipments = {
    12403: {
        "content": "Glasswear",
        "weight": 0.6,
        "status": "placed"
    },
    12404: {
        "content": "Electronics",
        "weight": 4.2,
        "status": "in_transit"
    },
    12405: {
        "content": "Books",
        "weight": 1.8,
        "status": "delivered"
    },
    12406: {
        "content": "Furniture",
        "weight": 22.5,
        "status": "processing"
    },
    12407: {
        "content": "Appliances",
        "weight": 18.0,
        "status": "placed"
    }
}

# Order matters
# Declare static routes before dynamic parameterized routes 
@app.get("/shipment/latest") #static
def get_latest_shipment():
    id = max(shipments.keys())
    return shipments[id]

@app.get("/shipment")
def get_shipment():
    return shipments

@app.get("/shipment/{id}") #dynamic
def get_shipment_by_ID(id: int) -> dict[str , Any]:
    if id not in shipments:
        return {"detail": "Given id doesn't exist"}
    return shipments[id]


@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )