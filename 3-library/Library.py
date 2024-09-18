# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 1/24/2023
# Description: The following program represents a library that contains
# various library items, and is used by various patrons.

class LibraryItem:
    '''
    Represents a library item that a patron can check out from a library
    '''

    def __init__(self, library_item_id, title):
        "Creates a LibraryItem with a title and unique identifier"

        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        "Returns library item's ID"
        return self._library_item_id

    def get_title(self):
        "Returns library item's title"
        return self._title

    def get_location(self):
        "Returns library item's location"
        return self._location

    def set_location(self, location):
        "Sets library item's location"
        self._location = location

    def get_checked_out_by(self):
        "Returns which patron has library item"
        return self._checked_out_by

    def set_checked_out_by(self, patron):
        "Sets which patron has library item"
        self._checked_out_by = patron

    def get_date_checked(self):
        "Returns library item's checked-out date"
        return self._date_checked_out

    def set_date_checked(self, date):
        "Sets library item's checked-out date"
        self._date_checked_out = date

    def get_requested_by(self):
        "Returns which patron has requested item be placed on hold"
        return self._requested_by

    def set_requested_by(self, patron):
        "Sets which patron has requested item be placed on hold"
        self._requested_by = patron


class Book(LibraryItem):
    '''
    Represents a book that a patron can check out from a library
    '''

    def __init__(self, library_item_id, title, author):
        "Creates a Book with an author in addition to all the data members of a LibraryItem"

        super().__init__(library_item_id, title)
        self._author = author
        self._check_out_length = 21

    def get_author(self):
        "Returns a book's author"
        return self._author

    def get_check_out_length(self):
        "Returns a book's check-out length"
        return self._check_out_length


class Album(LibraryItem):
    '''
    Represents an album that a patron can check out from a library
    '''

    def __init__(self, library_item_id, title, artist):
        "Creates an Album with an artist in addition to all the data members of a LibraryItem"

        super().__init__(library_item_id, title)
        self._artist = artist
        self._check_out_length = 14

    def get_artist(self):
        "Returns an album's artist"
        return self._artist

    def get_check_out_length(self):
        "Returns an album's check-out length"
        return self._check_out_length


class Movie(LibraryItem):
    '''
    Represents a movie that a patron can check out from a library
    '''

    def __init__(self, library_item_id, title, director):
        "Creates a movie with a director in addition to all the data members of a LibraryItem"

        super().__init__(library_item_id, title)
        self._director = director
        self._check_out_length = 7

    def get_director(self):
        "Returns a movie's director"
        return self._director

    def get_check_out_length(self):
        "Returns a movie's check-out length"
        return self._check_out_length


class Patron:
    '''
    Represents a patron of a library
    '''

    def __init__(self, patron_id, name):
        "Creates a LibraryItem with a name and unique identifier"

        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_fine_amount(self):
        "Returns how much the Patron owes the Library in late fines"
        return self._fine_amount

    def add_library_item(self, library_item):
        "Adds the specified LibraryItem to checked_out_items"
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        "Removes the specified LibraryItem to checked_out_items"
        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        "Adds the specified LibraryItem to checked_out_items"
        self._fine_amount += amount

    def get_patron_id(self):
        "Returns a Patron's ID"
        return self._patron_id

    def get_checked_out_items(self):
        "Returns a list of the patron's checked-out items"
        return self._checked_out_items


class Library:
    '''
    Represents a library that contains various library items, and is used by various patrons
    '''

    def __init__(self):
        "Creates a Library with a collection of the LibraryItems and a collection of the Patrons"

        self._holdings = []
        self._members = []
        self._current_date = 0

    def get_holdings(self):
        "Returns a list of the Library's items"
        return self._holdings

    def get_members(self):
        "Returns a list of the Library's items"
        return self._members

    def get_current_date(self):
        "Returns the current day at the library"
        return self._current_date

    def add_library_item(self, library_item):
        "Adds the specified LibraryItem to the collection of the Library's items"
        self._holdings.append(library_item)

    def add_patron(self, patron):
        "Adds the specified Patron to the list of the Library's members"
        self._members.append(patron)

    def lookup_library_item_from_id(self, item_id):
        "Returns the LibraryItem object corresponding to the ID parameter"

        library_item = None

        for item in self._holdings:
            if item.get_library_item_id() == item_id:
                library_item = item

        return library_item



    def check_out_library_item(self, patron_id, library_item_id):
        "If an item is available and not on hold, checks out item to library member"

        library_item = self.lookup_library_item_from_id(library_item_id)
        patron = self.lookup_patron_from_id(patron_id)

        if patron is None:
            print("patron not found")
        else:
            if library_item is None:
                print("item not found")
            else:
                if library_item.get_location() == "CHECKED_OUT":
                    print("item already checked out")
                elif library_item.get_location() == "ON_HOLD_SHELF" and library_item.get_requested_by() != patron:
                    print("item on hold by other patron")
                else:
                    library_item.set_checked_out_by(patron)
                    library_item.set_date_checked(self._current_date)
                    library_item.set_location("CHECKED_OUT")
                    library_item.set_requested_by(None)
                    patron.add_library_item(library_item)
                    print("check out successful")

    def return_library_item(self, library_item_id):
        "Returns library item to library if it has been checked out"

        library_item = self.lookup_library_item_from_id(library_item_id)

        if library_item is None:
            print("item not found")
        elif library_item.get_location() != "CHECKED_OUT":
            print("item already in library")
        else:
            patron = library_item.get_checked_out_by()
            patron.remove_library_item(library_item)

            if library_item.get_requested_by() is not None:
                library_item.set_location("ON_HOLD_SHELF")
            else:
                library_item.set_location("ON_SHELF")

            library_item.set_checked_out_by(None)

            print("return successful")

    def request_library_item(self, patron_id, library_item_id):
        "Places a library item on hold for a patron"

        library_item = self.lookup_library_item_from_id(library_item_id)
        patron = self.lookup_patron_from_id(patron_id)

        if patron is None:
            print("patron not found")
        else:
            if library_item is None:
                print("item not found")
            else:
                if library_item.get_requested_by() is not None:
                    print("item already on hold")
                else:
                    library_item.set_requested_by(patron)

                    if library_item.get_location() == "ON_SHELF":
                        library_item.set_location("ON_HOLD_SHELF")

                    print("request successful")

    def pay_fine(self, patron_id, amount):
        "Adjusts fine balance of specified patron"

        patron = self.lookup_patron_from_id(patron_id)
        payment = (-1 * amount)

        if patron is None:
            print("patron not found")
        else:
            patron.amend_fine(payment)
            print("payment successful")

    def increment_current_date(self):
        "Increments date and increases fines for overdue items for all patrons"

        self._current_date += 1

        for patron in self._members:
            for item in patron.get_checked_out_items():
                days_checked_out = (self._current_date - item.get_date_checked())
                if days_checked_out > item.get_check_out_length():
                    patron.amend_fine(.10)

b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
print(b1.get_author())
print(a1.get_artist())
print(m1.get_director())

p1 = Patron("abc", "Felicity")
p2 = Patron("bcd", "Waldo")

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_patron(p1)
lib.add_patron(p2)

lib.check_out_library_item("bcd", "456")
for _ in range(7):
    lib.increment_current_date()  # 7 days pass
lib.check_out_library_item("abc", "567")
loc = a1.get_location()
lib.request_library_item("abc", "456")
for _ in range(57):
    lib.increment_current_date()  # 57 days pass
p2_fine = p2.get_fine_amount()
lib.pay_fine("bcd", p2_fine)
lib.return_library_item("456")