import unittest
from Library import LibraryItem, Book, Album, Movie, Patron, Library

class LibraryTester(unittest.TestCase):

    def test_1(self):
        "Tests the functions of the LibraryItem Class"

        new_library_item = LibraryItem("ID123", "title123")
        print(f"Test 1")
        print(f"Item ID: {new_library_item.get_library_item_id()}")
        print(f"Item name: {new_library_item.get_title()}")

        print(f"Item location: {new_library_item.get_location()}")
        print(f"Item currently checked out by: {new_library_item.get_checked_out_by()}")
        print(f"Item was checked out on day: {new_library_item.get_date_checked()}")
        print(f"Item was requested by: {new_library_item.get_requested_by()}")

        new_library_item.set_location("Test location")
        new_library_item.set_checked_out_by("Test Patron")
        new_library_item.set_date_checked(1)
        new_library_item.set_requested_by("Test Requester")

        print(f"New Item location: {new_library_item.get_location()}")
        print(f"Item currently checked out by: {new_library_item.get_checked_out_by()}")
        print(f"Item was checked out on day: {new_library_item.get_date_checked()}")
        print(f"Item was requested by: {new_library_item.get_requested_by()}")

    def test_2(self):
        "Tests the functions of the Book Class"

        book = Book("Book ID", "Book title", "Book author")

        print(f"Book ID: {book.get_library_item_id()}")
        print(f"Book name: {book.get_title()}")
        print(f"Book author: {book.get_author()}")
        print(f"Max check-out days: {book.get_check_out_length()}")

    def test_3(self):
        "Tests the functions of the Album Class"

        album = Album("Album ID", "Album title", "Album artist")

        print(f"Album ID: {album.get_library_item_id()}")
        print(f"Album name: {album.get_title()}")
        print(f"Album artist: {album.get_artist()}")
        print(f"Max check-out days: {album.get_check_out_length()}")
        print(f"Item was checked out on day: {album.get_date_checked()}")

    def test_4(self):
        "Tests the functions of the Movie Class"

        movie = Movie("Movie ID", "Movie title", "Movie director")

        print(f"Movie ID: {movie.get_library_item_id()}")
        print(f"Movie name: {movie.get_title()}")
        print(f"Movie director: {movie.get_director()}")
        print(f"Max check-out days: {movie.get_check_out_length()}")
        print(f"Item location: {movie.get_location()}")

    def test_5(self):
        "Tests the functions of the Patron Class"

        patron = Patron("Test ID", "Test Name")

        print(f"Fines owed: {patron.get_fine_amount()}")

        patron.amend_fine(1.5)
        print(f"Updated fines owed: {patron.get_fine_amount()}")

        patron.amend_fine(-.5)
        print(f"Updated fines owed: {patron.get_fine_amount()}")

        print(f"Patron ID: {patron.get_patron_id()}")
        print(f"Patron items: {patron.get_checked_out_items()}")

        patron.add_library_item("book")
        patron.add_library_item("movie")
        print(f"Updated Patron items: {patron.get_checked_out_items()}")

        patron.remove_library_item("movie")
        print(f"Updated Patron items: {patron.get_checked_out_items()}")

    def test_6(self):
        "Tests the functions of the Library Class"

        library = Library()

        print(f"Test: Empty library on day 1")
        print(f"Library collection: {library.get_holdings()}")
        print(f"Library members: {library.get_members()}")
        print(f"Library date: {library.get_current_date()}")

        patron = Patron("Patron ID", "Patron Name")
        patron_2 = Patron("Patron 2 ID", "Patron 2 Name")
        patron_3 = Patron("Patron 3 ID", "Patron 3 Name")
        book = Book("Book ID", "Book title", "Book author")
        album = Album("Album ID", "Album title", "Album artist")
        movie = Movie("Movie ID", "Movie title", "Movie director")

        library.add_library_item(book)
        library.add_library_item(album)
        library.add_library_item(movie)
        library.add_patron(patron)
        library.add_patron(patron_2)
        library.add_patron(patron_3)
        print(f"Test: Updated library")
        print(f"Updated library collection: {library.get_holdings()}")
        print(f"Updated members: {library.get_members()}")

        print(f"Test: Look up items and patrons")
        print(f"Look up library item: {library.lookup_library_item_from_id('Wrong ID')}")
        print(f"Look up patron: {library.lookup_patron_from_id('Wrong ID')}")

        print(f"Test: Check out and return items")
        library.check_out_library_item("Patron ID", "Book ID")
        library.check_out_library_item("Patron 2 ID", "Album ID")
        library.check_out_library_item("Patron 3 ID", "Movie ID")
        library.return_library_item("Wrong ID")
        library.check_out_library_item("Patron 2 ID", "Book ID")

        print(f"Test: Request items")
        library.request_library_item("Patron 2 ID", "Book ID")
        library.request_library_item("Patron 3 ID", "Book ID")

        print(f"Test: Check out book on hold by another person")
        library.return_library_item("Wrong ID")
        library.check_out_library_item("Patron 3 ID", "Book ID")

        print(f"Test: Increment date and fines")
        for _ in range(30):
            library.increment_current_date()

        print(f"Library date: {library.get_current_date()}")
        print(f"Patron 1 checked out items: {patron.get_checked_out_items()}")
        print(f"Patron 1 fines: {patron.get_fine_amount()}")
        print(f"Patron 2 checked out items: {patron_2.get_checked_out_items()}")
        print(f"Patron 2 fines: {patron_2.get_fine_amount()}")
        print(f"Patron 3 checked out items: {patron_3.get_checked_out_items()}")
        print(f"Patron 3 fines: {patron_3.get_fine_amount()}")

        library.pay_fine("Patron x ID", .9)
        print(f"Update Patron 1 fines: {patron.get_fine_amount()}")
        library.pay_fine("Patron 2 ID", 1)
        print(f"Update Patron 2 fines: {patron_2.get_fine_amount()}")
        library.pay_fine("Patron 3 ID", 1.5)
        print(f"Update Patron 3 fines: {patron_3.get_fine_amount()}")