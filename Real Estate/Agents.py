import Properties
from typing import List

class Agent:
    def __init__(self,name:str,contact:str):
        self.name = name
        self.contact = contact
        self.sold_properties: List[Properties.Property] = []
        self.on_sale_properties: List[Properties.Property] = []

    def sell_property(self,propertyy:Properties.Property):
        if propertyy in self.on_sale_properties:
            self.sold_properties.append(propertyy)
            self.on_sale_properties.remove(propertyy)

    def put_on_sale(self,propertyy:Properties.Property):
        if propertyy not in self.on_sale_properties:
            self.on_sale_properties.append(propertyy)

