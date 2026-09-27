from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from .database import Databse
from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate

app = FastAPI()

db = Databse()

# Shipment by id
@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id : int):
    # Check if that shipment id present
    shipment = db.get(id)
    if shipment is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Given Id doesn't exist"
        )
    return shipment

# Create new shipment with content and weight
@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, int]:
    new_id = db.create(shipment)

    return {"id": new_id} # --> Will be useful later

# Update fields of a shipment -> as content, weight, destination all will be same. In update we can only update status
@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, shipment: ShipmentUpdate):
    updated_shipment = db.update(id, shipment)
    if updated_shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given Id doesn't exist"
        )
    return updated_shipment

# Delete a shipment
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    db.delete(id)
    return{"detail": f"Shipment with id #{id} is deleted!"}


## Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

