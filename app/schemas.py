from pydantic import BaseModel, Field


class Shipment(BaseModel):
    content: str = Field(
        description="Contents of the shipment",
        max_length=30,
        min_length=8,
    )
    weight: float = Field(
        description="Weight of the shipment in kilograms (kg)",
        le=25,
        ge=1,
    )
    destination: int | None = Field(
        description="Destination Zipcode. If not provided will be sent off to a random location",
        default=11000,
    )
