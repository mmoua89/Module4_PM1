class Item:
    def __ini__(self, item_name='', item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def total_cost(self) -> float:
        return self.item_quantity * self.item_price

    def display_item_name_and_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.total_cost():.2f}')