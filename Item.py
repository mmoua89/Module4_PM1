"""
An item class that represent an item name, price, and quantity
"""
class Item:
    def __init__(self, item_name, item_price, item_quantity):
        """
        Default constructor
        :param item_name: item name -> str
        :param item_price: item price -> float
        :param item_quantity: item quantity -> int
        """
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def total_cost(self) -> float:
        """
        Calculate the total cost of quantity x price
        :return: total cost
        """
        return self.item_quantity * self.item_price

    def display_item_name_and_cost(self):
        """
        Display the item name and the total cost
        :return: void
        """
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.total_cost():.2f}')
