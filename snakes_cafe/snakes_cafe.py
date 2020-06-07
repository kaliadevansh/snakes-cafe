"""
This command line utility mimics the functionality of a Point Of Sales machine for a restaurant system.
User ought to give inputs on the command line as instructed by the utility.
"""

# Variables
appetizers = ["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
quit_input = "quit"

menu = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
{}
{}
{}

Entrees
-------
{}
{}
{}
{}

Desserts
--------
{}
{}
{}

Drinks
------
{}
{}
{}

""".format(*appetizers, *entrees, *desserts, *drinks)
take_order_text = """***********************************
** What would you like to order? **
***********************************"""


# Functions


def is_quit(user_input):
    """
    Checks and exits if the user has given quit command.
    :param user_input: user input from console.
    :return: None
    """
    if user_input.lower() == quit_input:
        exit()


def print_menu():
    """
    Function to print menu.
    :return: None
    """
    print(menu)


def take_order():
    """
    Function to take user's order.
    :return: String representing user's order in Title case.
    """
    order = None
    while order is None or len(order) == 0:
        order = input().title()
    return order


def store_order(order_dictionary, order):
    """
    Stores user's order in-memory dictionary. Accepts items not on the menu as well.
    :param order_dictionary: existing orders dictionary.
    :param order: current user order.
    :return: None
    """
    if order in order_dictionary:
        order_dictionary[order] += 1
    else:
        if order not in appetizers and order not in entrees and order not in desserts and order not in drinks:
            print("We don't usually accept orders that are not on the menu, but you're special. "
                  "We'll make that for you.")
        order_dictionary[order] = 1


def repeat_order(order_dictionary, order_item):
    """
    Function to repeat the item that the user just ordered. Does not repeat the entire order.
    :param order_dictionary: existing orders dictionary.
    :param order_item: current user order.
    :return: None
    """
    item_count = order_dictionary[order_item]
    print(f"""** {item_count} order of {order_item} {'have' if item_count > 1 else 'has'} been added to your meal **""")


def initiate_pos():
    """
    Main method to start the POS machine.
    :return: None
    """
    print_menu()
    print(take_order_text)
    order = take_order()
    order_dictionary = {}
    while not is_quit(order):
        store_order(order_dictionary, order)
        repeat_order(order_dictionary, order)
        order = take_order()


if __name__ == "__main__":
    """
    Runs main method only if the module is being called directly.
    """
    initiate_pos()
