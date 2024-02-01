import abc

class Product(abc.ABC):
    def __init__(self,name:str,price:int,description:str):
        self.name = name
        self.price = price
        self.description = description

    @abc.abstractmethod
    def rate(self):
        ...


class Clothing(Product):
    def __init__(self,name:str,price:int,description:str,size:str):
        super().__init__(name,price,description)
        self.size = size

    def available_size(self,size:str):
        if size == self.size:
            print(f'{size} is available')

    def rate(self):
        rating = input('Please enter a number from 1-5 to rate the product: ')
        print(f'rating is {rating}')