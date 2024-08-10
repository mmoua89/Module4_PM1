"""
Author: Meng Moua
Course: CSC500
Assignment: Module 4, Portfolio Milestone 1
"""
from Item import Item

def main():
    # a cart ready to add item(s)
    cart = set()
    for itemNumber in range(0, 2, 1):
        print(f'Item {itemNumber + 1}')
        itemName = input('Item name:\n')
        itemPrice = input('Item price:\n')
        itemQuantity = input('Item quantity\n')

        # valid item_price and item_quantity
        if not valid_numbers(itemPrice, itemQuantity):
            return

        # append item in (Item) class
        item = Item(itemName, float(itemPrice), int(itemQuantity))
        # add an item into the cart
        cart.add(item)

    # print all items names, costs, and total cost
    print('TOTAL COST')
    reversed_cart = list(cart)[::-1]
    for item in reversed_cart:
        item.print_item_cost()

    # calculate the total cost out of the cart
    total = 0
    for item in cart:
        total += item.calculate_total_cost()

    # print the total cost
    print(f'Total: ${total:.2f}')

def valid_numbers(item_price, item_quantity) -> bool:
    """
    Valid item price and item quantity numbers
    :param item_price: item price -> str
    :param item_quantity: item quantity -> str
    :return: true or false
    """
    if not valid_number(item_price):
        print('Please try again. The (item price) must be a valid number.')
        return False

    if float(item_price) < 0:
        print('Please try again. The (item price) cannot be a negative value.')
        return False

    if not valid_number(item_quantity):
        print('Please try again. The (item quantity) must be a valid number.')
        return False

    if int(item_quantity) < 0:
        print('Please try again. The (item quantity) cannot be a negative value.')
        return False

    return True

def valid_number(num) -> bool:
    """
    Validate a number
    :param num: a string number
    :return: true or false
    """
    try:
        float(num)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    main()
