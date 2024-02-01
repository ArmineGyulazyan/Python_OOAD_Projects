import abc


class Property(abc.ABC):
    def __init__(self,address:str,price:int,feature:str):
        self.address = address
        self.price = price
        self.feature = feature

    @abc.abstractmethod
    def view_info(self):
        ...


class Residential(Property):

    def view_info(self):
        print(f'The residential property is located at {self.address}, the price is {self.price},features are {self.feature}')
