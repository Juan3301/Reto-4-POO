"""For this new update to the restaurant scenario, setters and getters were 
added to all MenuItem subclasses, the total price method was redefined and 
changed in several subclasses using polymorphism, and finally, the payment 
method for canceling the order was added, also using polymorphism."""


class MenuItem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float):
        self._price = new_price

    def total_price(self, quantity: int) -> float:
        return self._price * quantity


class Drink(MenuItem):
    def __init__(self, name, price, size, drink_type):
        super().__init__(name, price)
        self.__size = size
        self.__drink_type = drink_type

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_drink_type(self):
        return self.__drink_type

    def set_drink_type(self, drink_type):
        self.__drink_type = drink_type

    def total_price(self, quantity: int) -> float:
        return super().total_price(quantity) * 1.05


class Starter(MenuItem):
    def __init__(self, name, price, temperature, size, presentation):
        super().__init__(name, price)
        self.__temperature = temperature
        self.__size = size
        self.__presentation = presentation

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_presentation(self):
        return self.__presentation

    def set_presentation(self, presentation):
        self.__presentation = presentation


class MainCourse(MenuItem):
    def __init__(self, name, price, protein_type, side_dish, size, style):
        super().__init__(name, price)
        self.__protein_type = protein_type
        self.__side_dish = side_dish
        self.__size = size
        self.__style = style

    def get_protein_type(self):
        return self.__protein_type

    def set_protein_type(self, protein_type):
        self.__protein_type = protein_type
        
    def get_style(self):
        return self.__style

    def set_style(self, style):
        self.__style = style
        
    def get_side_dish(self):
        return self.__side_dish

    def set_side_dish(self, dish):
        self.__side_dish = dish
        
    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def total_price(self, quantity: int) -> float:
        return super().total_price(quantity) * 1.10


class Dessert(MenuItem):
    def __init__(self, name, price, dessert_type, flavor, temperature):
        super().__init__(name, price)
        self.__dessert_type = dessert_type
        self.__flavor = flavor
        self.__temperature = temperature

    def get_flavor(self):
        return self.__flavor

    def set_flavor(self, flavor):
        self.__flavor = flavor
        
    def get_dessert_type(self):
        return self.__dessert_type
    
    def set_dessert_type(self, dessert):
        self.__dessert_type = dessert
        
    def get_temperature(self):
        return self.__temperature
    
    def set_temperature(self, temperature):
        self.__temperature = temperature


class Additional(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)


class OrderItem:
    def __init__(self, item: MenuItem, quantity: int):
        self.item = item
        self.quantity = quantity

    def subtotal(self) -> float:
        return self.item.total_price(self.quantity)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: MenuItem, quantity: int):
        self.items.append(OrderItem(item, quantity))

    def subtotal_order(self) -> float:
        return sum(i.subtotal() for i in self.items)

    def discounts(self) -> float:
        total = self.subtotal_order()
        discount = 0

        has_starter = any(isinstance(i.item, Starter) for i in self.items)
        has_main = any(isinstance(i.item, MainCourse) for i in self.items)
        has_drink = any(isinstance(i.item, Drink) for i in self.items)
        has_dessert = any(isinstance(i.item, Dessert) for i in self.items)

        if has_starter and has_main and has_drink and has_dessert:
            discount += total * 0.10

        total_items = sum(i.quantity for i in self.items)

        if total_items >= 5:
            discount += total * 0.05
        
        #disscount if order have a meat

        has_meat = any(
            isinstance(i.item, MainCourse)
            and i.item.get_protein_type() == "meat" #Getter 
            for i in self.items
        )

        if has_meat:
            discount += total * 0.05
            
        #discount if order has dessert
        
        if has_dessert:
            discount += total * 0.05
            
        return discount

    def total_order(self) -> float:
        return self.subtotal_order() - self.discounts()

    def pay(self, payment_method):
        total = self.total_order()
        payment_method.pay(total)


class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")


class Card(PaymentMethod):
    def __init__(self, number: str, cvv: str):
        self.__number = number
        self.__cvv = cvv

    def get_masked_number(self) -> str:
        return f"****{self.__number[-4:]}"

    def pay(self, amount):
        print(f"Paying {amount:.2f} with card {self.get_masked_number()}")


class Cash(PaymentMethod):
    def __init__(self, amount_given):
        self.amount_given = amount_given

    def pay(self, amount):
        if self.amount_given >= amount:
            print(f"Cash payment successful. Change: {self.amount_given - amount:.2f}")
        else:
            print(f"Insufficient funds. Missing: {amount - self.amount_given:.2f}")


if __name__ == "__main__":
    #Example with a family three persons
    # Mom
    mom_drink = Drink("Lemonade", 10000, "medium", "non-alcoholic")
    mom_starter = Starter("Ceviche", 20000, "cold", "small", "bowl")
    mom_main = MainCourse("Salmon", 50000, "fish", "asparagus", "large", "oven")
    mom_dessert = Dessert("Banana Split", 15000, "ice cream", "sweet", "cold")

    # Dad
    dad_drink = Drink("Beer", 5000, "medium", "alcoholic")
    dad_starter = Starter("Empanadas", 10000, "hot", "small", "plate")
    dad_main = MainCourse("Steak", 50000, "meat", "salad", "large", "grill")
    dad_dessert = Dessert("Crepe Suzette", 20000, "crepe", "sweet", "hot")

    # Kid
    kid_drink = Drink("Juice", 3500, "medium", "non-alcoholic")
    kid_food = Starter("Nuggets", 15000, "hot", "small", "tray")
    kid_extra = Additional("Fries", 6000)

    # Using a setter
    mom_drink.set_size("large")

    order = Order()
    order.add_item(mom_drink, 2)
    order.add_item(mom_starter, 1)
    order.add_item(mom_main, 1)
    order.add_item(mom_dessert, 2)

    order.add_item(dad_drink, 3)
    order.add_item(dad_starter, 1)
    order.add_item(dad_main, 1)
    order.add_item(dad_dessert, 1)

    order.add_item(kid_drink, 1)
    order.add_item(kid_food, 2)
    order.add_item(kid_extra, 1)

    print("Total order:", order.total_order())

    # Payment example with cash
    payment = Cash(200000)
    order.pay(payment)
    
    # Payment example with card
    payment2 = Card("109057801254812","033")
    order.pay(payment2)
    