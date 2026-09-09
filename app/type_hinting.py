text:str = "value"
text = "Piyusha"
part: int = 90
temp: float = 43.5
number: int|float = 12

digits: list[int] = [1,2,3,4,5]

table_5: tuple[int, ...] = (1,2,3,5,5)
class City: 
    def __init__(self, name, location):
        self.name = name
        self.location = location


Kolhapur = City("Kolhapur", 65495295)
city_temp: tuple[City, float] = (Kolhapur, 30)
print(city_temp)

shipment: dict[str, int | float | str] = {
    "id": 12343,
    "weight": 1.24,
    "content": "wooden table",
    "status": "in transit"
}

# print(table_5)
# print("-------")
# print(shipment)
def root(nums: int ) ->float:
    return pow(nums, 0.5)

root_25 = root(24)
print(root_25)