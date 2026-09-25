from enum import Enum

from pydantic import BaseModel, Field


class ShipmentStatus(Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered" 

class BaseShipment(BaseModel):
    content: int
    weight: float = Field(le=25)
    destination: int

class ShipmentRead(BaseShipment):
    status: ShipmentStatus

class ShipmentCreate(BaseShipment):
    # Status will be auto matically created
    pass

class ShipmentUpdate(BaseModel):
    # We need only status update so use of BaseModel
    status: ShipmentStatus