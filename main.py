"""
Author: Meng Moua
Course: CSC500
Assignment: Module 4, Portfolio Milestone 1
"""
from Item import Item

def main():
    # a cart ready to add item(s)
    cart = set()
    for i in range(2):
        print(f'Item {i + 1}')
        item_name = input('Enter the item name:\n')
        item_price = input('Enter the item price:\n')
        item_quantity = input('Enter the item quantity\n')

        if not valid_number(item_price) or not valid_number(item_quantity):
            print('The (item price) or (item quantity) is not a valid number.')
            return

        if int(item_price) < 0 or int(item_quantity) < 0:
            print('Please try again. The (item price) and (item quantity) cannot be a negative number.')

        # append item in (Item) class
        item = Item(item_name, item_price, item_quantity)
        # add an item into the cart
        cart.add(item)

    # print all items names and total cost
    for item in cart:
        item.display_item_name_and_cost()

    # calculate the total cost out of the cart
    total = 0
    for item in cart:
        total += item.total_cost()

    # print the total cost
    print(f'Total: ${total:.2f}')

def valid_number(num) -> bool:
    """
    Validate a number either a float or an int
    :param num: a number
    :return: true or false
    """
    valid = True
    try:
        float(num)
        valid = True
    except ValueError:
        valid = False

    try:
        int(num)
        valid = True
    except ValueError:
        valid = False

    return valid

if __name__ == '__main__':
    main()
