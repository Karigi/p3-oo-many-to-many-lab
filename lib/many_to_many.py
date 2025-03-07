class Author:
    all = []
    def __init__(self,name=''):
        if isinstance(name,str):
            self.name = name
            Author.all.append(self)
        else:
            raise Exception("title should be a string")

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
        


class Book:
    all = []
    def __init__(self,title=''):
        if isinstance(title,str):
            self.title = title
            Book.all.append(self)
        else:
            raise Exception("title should be a string")

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]
  


class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author) and isinstance(book,Book) \
        and isinstance(date,str) and isinstance(royalties,int):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)
            Contract.contracts_by_date(self.date)
        else:
            raise Exception("author-Author object, book-Book object, name-string, royalties-integer")
        
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]


