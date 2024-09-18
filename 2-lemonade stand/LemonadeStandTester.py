# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/18/2023
# Description: The following program contains unit tests for the Class LemonadeStand, which records
# menu items and daily sales of a lemonade stand.

import unittest
from LemonadeStand import InvalidSalesItemError, MenuItem, SalesForDay, LemonadeStand

class LemonadeStandTester(unittest.TestCase):
    '''
    Contains unit tests for the Class LemonadeStand
    '''

    def test_1(self):
        "Tests the functions of the MenuItem Class"

        new_menu_item = MenuItem("Socks", 1, 10)
        print(f"Test 1")
        print(f"Item name: {new_menu_item.get_name()}")
        print(f"Item's wholesale cost: {new_menu_item.get_wholesale_cost()}")
        print(f"Item's selling price: {new_menu_item.get_selling_price()}")

    def test_2(self):
        "Tests the functions of the SalesForDay Class"

        test_sales = {
        "Socks" : 10,
        "Shirts" : 20,
        }

        new_sales = SalesForDay(0, test_sales)

        print(f"Test 2")
        print(f"Day of sale: {new_sales.get_day()}")
        print(f"Dictionary of sales: {new_sales.get_sales_dict()}")

    def test_3(self):
        "Tests initiation and get_name, add_menu_item and enter_sales_for_today functions of LemonadeStand Class"

        new_stand = LemonadeStand("Test Stand")

        self.assertEqual(new_stand.get_name(), 'Test Stand')

        print(f"Test 3")
        print(f"Stand name: {new_stand.get_name()}")

        test_item = MenuItem ("Balloons", 1, 5)
        new_stand.add_menu_item(test_item)

        test_sales = {
            "Balloons": 10,
            "Cake": 20
        }

        try:
            new_stand.enter_sales_for_today(test_sales)
        except InvalidSalesItemError:
            print("Invalid. An item in the sales record is not on the menu.")
        else:
            print("Sales record has been updated.")

    def test_4(self):
        "Tests sales_of_menu_item_for_day and total_sales_for_menu_item functions of LemonadeStand Class"

        new_stand = LemonadeStand("Test Stand 2")

        test_item = MenuItem("Pen", 1, 5)
        new_stand.add_menu_item(test_item)

        test_sales_1 = {
            "Pen": 10
        }

        new_stand.enter_sales_for_today(test_sales_1)

        print(f"Test 4")
        print(f"Sales of test item on day 0: {new_stand.sales_of_menu_item_for_day(0, 'Pen')}")

        test_sales_2 = {
            "Pen": 30
        }

        new_stand.enter_sales_for_today(test_sales_2)

        print(f"Sales of test item on day 1: {new_stand.sales_of_menu_item_for_day(1, 'Pen')}")
        print(f"Total sales of test item: {new_stand.total_sales_for_menu_item('Pen')}")

    def test_5(self):
        "Tests total_profit_for_menu_item and total_profit_for_stand functions of LemonadeStand Class"

        new_stand = LemonadeStand("Test Stand 3")

        test_item = MenuItem("Puppy", 1, 6)
        new_stand.add_menu_item(test_item)
        test_item_2 = MenuItem("Kitten", 1, 11)
        new_stand.add_menu_item(test_item_2)

        test_sales_1 = {
            "Puppy": 1
        }

        test_sales_2 = {
            "Puppy": 2,
            "Kitten": 4
        }

        new_stand.enter_sales_for_today(test_sales_1)
        new_stand.enter_sales_for_today(test_sales_2)

        print(f"Test 5")
        print(f"Total sales of test item 1: {new_stand.total_sales_for_menu_item('Puppy')}")
        print(f"Total sales of test item 2: {new_stand.total_sales_for_menu_item('Kitten')}")
        print(f"Total profit for test item 1: {new_stand.total_profit_for_menu_item('Puppy')}")
        print(f"Total profit for test item 2: {new_stand.total_profit_for_menu_item('Kitten')}")
        print(f"Total profit: {new_stand.total_profit_for_stand()}")

        self.assertAlmostEqual(new_stand.total_profit_for_stand(), 55)
