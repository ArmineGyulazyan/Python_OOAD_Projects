from typing import List
import Products

class Customer:
    def __init__(self,name:str,contact:str):
        self.name = name
        self.contact = contact
        self.cart: List[Products.Product] = []


    def add_to_cart(self,product:Products.Product):
        self.cart.append(product)


