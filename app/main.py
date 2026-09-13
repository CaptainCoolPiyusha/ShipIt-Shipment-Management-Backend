from typing import Any

from fastapi import FastAPI, HTTPException, status
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

# Path parameter
# @app.get("/shipment/{id}") # dynamic
# def get_shipment_by_id(id: int) -> dict[str, Any]:
#     if id not in shipments:
#         return {"detail": "Given id doesn't exist"}
#     return shipments[id]

# Query parameter
@app.get("/shipment")
def get_shipment_by_id(id : int) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Given Id doesn't exist"
        )
    return shipments[id]

@app.post("/shipment")
def submit_shipment(data: dict[str, str], weight: float) -> dict[str, Any]:
    content = data["content"]


    if weight>25:
        raise HTTPException(
            status_code = status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25"
        )
    new_id = max(shipments.keys())+1
    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed"
    }
    return data

@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )