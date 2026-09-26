from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from .database import save, shipments
from .schemas import ShipmentCreate, ShipmentRead, ShipmentUpdate

app = FastAPI()


# Shipment datastore as dict
# shipments = {
#     12403: {
#         "content": "Glassware",
#         "weight": 0.6,
#         "destination": 11000,
#         "status": "placed"
#     },
#     12404: {
#         "content": "Electronics",
#         "weight": 4.2,
#         "destination": 11001,
#         "status": "in_transit"
#     },
#     12405: {
#         "content": "Books",
#         "weight": 1.8,
#         "destination": 11002,
#         "status": "delivered"
#     },
#     12406: {
#         "content": "Furniture",
#         "weight": 22.5,
#         "destination": 11003,
#         "status": "placed"
#     },
#     12407: {
#         "content": "Appliances",
#         "weight": 18.0,
#         "destination": 11004,
#         "status": "out_for_delivery"
#     }
# }

# Shipment by id
@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id : int):
    # Check if that shipment id present
    if id not in shipments:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Given Id doesn't exist"
        )
    return shipments[id]

# Create new shipment with content and weight
@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, int]:
    # Create shipment to new_id
    new_id = max(shipments.keys()) + 1
    # Add that shipment to new id
    shipments[new_id] = {
        **shipment.model_dump(),
        "id": new_id,
        "status": "placed",
    }

    return {"id": new_id} # --> Will be useful later

# Update fields of a shipment -> as content, weight, destination all will be same. In update we can only update status
@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(id: int, body: ShipmentUpdate):

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given Id doesn't exist"
        )

    shipments[id].update(body.model_dump())
    save() 
    return shipments[id]

# Delete a shipment
@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    if id in shipments:
        shipments.pop(id)
    save()
    return{"detail": f"Shipment with id #{id} is deleted!"}


## Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )