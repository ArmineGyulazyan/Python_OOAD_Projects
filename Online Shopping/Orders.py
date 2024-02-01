import Customers
import Products


class Order:

    orders = {}

    def __init__(self,customer:Customers.Customer,*products:Products.Product):
        self.customer = customer
        self.products = products
        self.total_price = sum([i.price for i in products])
        self.orders[customer] = products

    def see_total_price(self):
        print(f'the total price is {self.total_price}')

    def view_customer_orders(self):
        for cust, ord in self.orders.items():
            print(cust.name,[i.name for i in ord])

