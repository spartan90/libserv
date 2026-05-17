from collections import Counter

from models import Book, Member, BookAudit

'''This is a servie layer'''
'''This will have functions like add,return, reporting and supporting utility functions like validation,mock data adding'''
class LibManagementService:
    def __init__(self):
        self.books = {}
        self.members= {}
        self.auditTrail = []
        self.mockData()
        self.auditId = 101

    ##borrow book function
    def borrow_book(self, memberId, bookId):
        #validate if the correct request
        if self.valid_request(memberId, bookId):
            #check if book available
            if self.isBookAvailable(bookId):
                ##udpate the book object and make it unavailable
                book = self.books[bookId]
                book.isAvailable = False
                ##update member object map the book with member
                member = self.members[memberId]
                member.booksBorrowed.append(book)
                self.auditId = self.auditId +1
                #keep audit logs for reporting
                auditLog = BookAudit(self.auditId,bookId,memberId,"Borrow")
                self.auditTrail.append(auditLog)

                return f"Success: '{book.title}' successfully issued to {member.name}."
            else:
                print("Book Not Available Currently")


    ##return book function
    def return_book(self, memberId, bookId):
        ##validate the request
        if self.valid_request(memberId, bookId):
            book = self.books[bookId]
            member = self.members[memberId]

            if book in member.booksBorrowed:
                ##remove from member list
                member.booksBorrowed.remove(book)
                ##make book available
                book.isAvailable = True

                self.auditId = self.auditId + 1
                # keep audit logs for reporting
                auditLog = BookAudit(self.auditId, bookId, memberId, "Return")
                self.auditTrail.append(auditLog)

                return f"Success: '{book.title}' returned by {member.name}."

            else:
                print("Book not allocated to member")


    ##show all books
    def show_available_books(self):
        return [book for book in self.books.values() if book.isAvailable]

    ##show active members who has borrowd books
    def show_member_borrowed_books(self):
        return [member for member in self.members.values() if len(member.booksBorrowed) > 0]


    ##search by title or author
    def search_by_author_or_title(self,searchTxt):
        searchTxt = searchTxt.strip().lower()
        return [
            book for book in self.books.values()
            if searchTxt in book.title.lower() or searchTxt in book.author.lower()
        ]

    ##find the most popular genere
    def show_popular_genere(self):
        borrowed_genres = [
            self.books[trail.bookId].genre
            for trail in self.auditTrail
            if trail.action == "Borrow" and trail.bookId in self.books
        ]

        if not borrowed_genres:
            return None, 0

        genre_counts = Counter(borrowed_genres)
        most_common_genre, count = genre_counts.most_common(1)[0]
        return most_common_genre, count


    ##Basic Validation
    def valid_request(self, memberId, bookId):
        ##validate the request is valid
        if memberId not in self.members:
            print("Member is not registered in System")
            return False
        if bookId not in self.books:
            print("Book is not in System")
            return False
        return True

    ##check book availability
    def isBookAvailable(self,bookId):
        book = self.books[bookId]
        return book.isAvailable

    def mockData(self):
        ### add sample books
        book1 = Book("1", "Myth and Mythiya", "Devdut Pattnaik", "Philosophical ")
        self.books.__setitem__(book1.bookId,book1)
        book2 = Book("2", "Mahagatha", "Satyarth Naik", "Mythological ")
        self.books.__setitem__(book2.bookId, book2)
        book3 = Book("3", "Open To Work", "Ryan Rolslansky", "Non Fictional ")
        self.books.__setitem__(book3.bookId, book3)
        book4 = Book("4", "Indian Should Invest", "Vinod", "Non Fictional ")
        self.books.__setitem__(book4.bookId, book4)

        ## add sample members
        member1 = Member("1001","Rohit Tambat", 35,"Pune")
        self.members.__setitem__(member1.memberId,member1)
        member2 = Member("1002", "Aditi", 33, "Pune")
        self.members.__setitem__(member2.memberId, member2)
        member3 = Member("1003", "Raunak", 34, "Mumbai")
        self.members.__setitem__(member3.memberId, member3)




