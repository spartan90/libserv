#have all models based on part A pdf details

class Book:
    def __init__(self,bookId,title,author,genre):
        self.bookId = str(bookId)
        self.title = title
        self.author = author
        self.genre = genre
        self.isAvailable = True

class Member:
    def __init__(self,memberID,name,age,contact):
        self.memberId = str(memberID)
        self.name = name
        self.age = age
        self.contact = contact
        self.booksBorrowed = []

### Audit trail for reporting purpse
class BookAuditTrail:
    def __init__(self,id,bookId,memberId,action):
        self.id = id
        self.bookId = bookId
        self.memberId = memberId
        self.action = action

