# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/18/2023
# Description: The following program records menu items and daily sales of a
# lemonade stand.

class InvalidSalesItemError(Exception):
    "Exception for invalid sales item"
    pass

class MenuItem:
    '''
    Represents a menu item to be offered for sale at the lemonade stand
    '''
    def __init__(self, item_name, wholesale_cost, selling_price):
        "Creates a MenuItem with specific name, wholesale cost, and selling price"
        self._item_name = item_name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        "Returns menu item's name"
        return self._item_name

    def get_wholesale_cost(self):
        "Returns menu item's wholesale cost"
        return self._wholesale_cost

    def get_selling_price(self):
        "Returns menu item's selling price"
        return self._selling_price


class SalesForDay:
    '''
    Represents the sales for a particular day
    '''

    def __init__(self, number_of_days, sales_dictionary):
        "Creates an object that will represent the sales for a particular day"
        self._day = number_of_days
        self._sales_dictionary = sales_dictionary

    def get_day(self):
        "Returns the particular day associated with the item sales"
        return self._day

    def get_sales_dict(self):
        "Returns a dictionary whose keys are the names of the items sold and whose values are the numbers of those items sold that day"
        return self._sales_dictionary

class LemonadeStand:
    '''
    Represents a lemonade stand
    '''
    def __init__(self, stand_name):
        "Creates a lemonade stand with specific name"
        self._stand_name = stand_name
        # not sure about these:
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        "Returns lemonade stand's name"
        return self._stand_name

    def get_menu(self):
        "Returns lemonade stand's name"
        return self._menu

    def add_menu_item(self, menu_item):
        "Takes as a parameter a MenuItem object and adds it to the menu dictionary"
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, dictionary_of_items_sold):
        "Adds records of today's sales to a list of all sales"

        items_sold = dictionary_of_items_sold

        # Check to see if all items sold are valid items on menu
        for name_of_sales_item in items_sold:
            if name_of_sales_item not in self._menu:
                raise InvalidSalesItemError

        # Add menu items that didn't sell to list of sold items
        for name_of_item in self._menu:
            if name_of_item not in items_sold:
                items_sold[name_of_item] = 0

        # Add record of sales for today to the list of all record sales
        new_sales_for_today = SalesForDay(self._current_day, items_sold)
        self._sales_record.append(new_sales_for_today)
        self._current_day += 1

    def sales_of_menu_item_for_day(self, day, name_of_menu_item):
        "Returns the number of that item sold on that day"

        record_of_sales_for_day = {}

        for sales in self._sales_record:
            if sales.get_day() == day:
                record_of_sales_for_day = sales.get_sales_dict()

        sales_of_menu_item_for_day = record_of_sales_for_day[name_of_menu_item]

        return sales_of_menu_item_for_day

    def total_sales_for_menu_item(self, name_of_menu_item):
        "Returns the total number of that item sold over the history of the stand"

        total_sales_for_menu_item = 0

        for day in range(0, self._current_day, 1):
            total_sales_for_menu_item += self.sales_of_menu_item_for_day(day, name_of_menu_item)

        return total_sales_for_menu_item

    def total_profit_for_menu_item(self, name_of_menu_item):
        "Returns the total profit on an item over the history of the stand"

        menu_item = self._menu[name_of_menu_item]

        profit_on_item = (menu_item.get_selling_price() - menu_item.get_wholesale_cost())

        total_profit_for_menu_item = (self.total_sales_for_menu_item(name_of_menu_item) * profit_on_item)

        return total_profit_for_menu_item

    def total_profit_for_stand(self):
        "Returns the total profit on all items sold over the history of the stand"

        total_profit_for_stand = 0

        for item in self._menu:
            total_profit_for_stand += self.total_profit_for_menu_item(item)

        return total_profit_for_stand

def main():
    lemonade_stand = LemonadeStand("Bleu's Lemonade Stand")

    small = MenuItem("Small Lemonade", 0.5, 1)
    medium = MenuItem("Medium Lemonade", 0.75, 1.5)
    large = MenuItem("Large Lemonade", 1, 2)

    lemonade_stand.add_menu_item(small)
    lemonade_stand.add_menu_item(medium)
    lemonade_stand.add_menu_item(large)

    sales_on_first_day = {
        "Small Lemonade" : 10,
        "Large Lemonade" : 20,
        "Cookie"         : 5  #will cause program to run an error
    }

    try:
        lemonade_stand.enter_sales_for_today(sales_on_first_day)
    except InvalidSalesItemError:
        print("Invalid. An item in the sales record is not on the menu.")
    else:
        print("Sales record has been updated.")

if __name__ == '__main__':
    main()
