"""
An item class that represent an item name, price, and quantity
"""
class Item:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        """
        Default constructor
        :param item_name: the name of an item -> str
        :param item_price: the price of an item -> float
        :param item_quantity: the quantity of an item -> int=
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

    def print_item_cost(self):
        """
        Display the item name and the total cost
        :return: void
        """
        print("{} {} @ ${} = ${:.2f}".format(self.item_name,
                                             self.item_quantity,
                                             self.item_price,
                                             self.total_cost()))
