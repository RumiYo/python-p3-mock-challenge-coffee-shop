class Coffee:
    def __init__(self, name):
        self.name = name

    @property 
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if not hasattr(self, 'name'):
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
        
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in Order.all if order.coffee == self]))
    
    def num_orders(self):
        return len(Coffee.orders(self))
    
    def average_price(self):
        coffee_prices = []
        for item in Coffee.orders(self):
            coffee_prices.append(item.price)
        
        return sum(coffee_prices) / len(coffee_prices)


class Customer:
    
    all = []

    def __init__(self, name):
        self.name = name
        if name not in Customer.all:
            Customer.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if len(name)>=1 and len(name)<=15:
                self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
        
    @classmethod
    def most_aficionado(cls, coffee):

        highest_spend = 0
        highest_spender = None

        for customer in cls.all:
            orders_for_coffee = [order for order in customer.orders() if order.coffee == coffee]
            total_spend = sum(order.price for order in orders_for_coffee)
            if total_spend > highest_spend:
                highest_spend = total_spend
                highest_spender = customer
        
        return highest_spender
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property 
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self,customer):
        if isinstance(customer, Customer):
            self._customer = customer
    
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    @property 
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not hasattr(self, 'price'):
            if isinstance(price, float) or isinstance(price, int):
                if price >= 1 and price <= 10: 
                    self._price = price 