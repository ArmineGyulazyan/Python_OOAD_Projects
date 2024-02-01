import Customers
import Products
import Orders

def main():

    customer = Customers.Customer('Ann','012568899')
    customer2 = Customers.Customer('Tina','012567799')
    product1 = Products.Clothing('dress',20000,'red dress','XS')
    product2 = Products.Clothing('blouse',15000,'cashmere blouse','S')
    product3 = Products.Clothing('hoodie',10000,'black hoodie','M')
    order = Orders.Order(customer,product1,product2)
    order.see_total_price()
    order.view_customer_orders()

    order2 = Orders.Order(customer2,product3)
    order2.see_total_price()
    order2.view_customer_orders()


if __name__ == '__main__':
    main()
