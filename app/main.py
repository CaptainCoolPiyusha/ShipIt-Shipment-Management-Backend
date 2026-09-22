from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

class Shipment(BaseModel):
    content: str
    weight: float
    destination: int

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

# Request body
@app.post("/shipment")
def submit_shipment(shipment: Shipment) -> dict[str, Any]:
    if shipment.weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Maximum weight limit is 25",
        )
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        "content": shipment.content,
        "weight": shipment.weight,
        "status": "placed"
    }
    return {"id": new_id}

# Using Path and Query parameter together
@app.get("/shipment/{field}")
def get_shipment_field(field: str, id:int) -> Any:
    return shipments[id][field]

# Replacing the current element with new values/Update
@app.put("/shipment")
def update_shipment(id: int, content: str, weight:float, status:str) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": status
    }
    return shipments[id]

@app.patch("/shipment")
def patch_shipment(id: int, body: dict[str, Any]) -> dict[str, Any]:
    # First extract that shipment from list
    shipment = shipments[id]
    shipment.update(body)
    shipments[id] = shipment
    return shipment

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    if id in shipments:
        shipments.pop(id)
    return{"detail": f"Shipment with id #{id} is deleted!"}

@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )