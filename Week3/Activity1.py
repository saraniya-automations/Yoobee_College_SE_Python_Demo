class Library:
    def __init__(self):
        # initializes books array
        self.books = []
    
    def setBook(self,bookName,bookAuthor,bookCategory):
        #Creates single book
        book = {
            'bookName':bookName, 'bookAuthor': bookAuthor, 'bookCategory':bookCategory
        }
        #Add created single book in to books array
        self.books.append(book)

    def getAllBooks(self):
        #take each book from array and prints
        for book in self.books:
            print('*******************')
            print('Book Name : ',book['bookName'])
            print('Book Author : ',book['bookAuthor'])
            print('Book Category : ',book['bookCategory'])
            print('*******************')


Library1 = Library()
Library1.setBook('Loads of rings','J.R.R. Tolkien','Fantasy')
Library1.setBook('War and Peace','tolstoy','Science')
Library1.getAllBooks()
    