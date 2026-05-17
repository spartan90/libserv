#have all models based on part A pdf details

class Book:
    def __init__(self,bookId,title,author,genre):
        self.bookId = str(bookId)
        self.title = title
        self.author = author
        self.genre = genre
        self.isAvailable = True

    def __str__(self):
        status = "Available" if self.isAvailable else "Borrowed"
        return f"[{self.bookId}] '{self.title}' written by {self.author} ({self.genre}) - {status}"

class Member:
    def __init__(self,memberID,name,age,contact):
        self.memberId = str(memberID)
        self.name = name
        self.age = age
        self.contact = contact
        self.booksBorrowed = []

    def __str__(self):
        return f"Member [{self.memberId}]: {self.name} | Contact: {self.contact}"

### Audit trail for reporting purpse
class BookAudit:
    def __init__(self,id,bookId,memberId,action):
        self.id = id
        self.bookId = bookId
        self.memberId = memberId
        self.action = action

