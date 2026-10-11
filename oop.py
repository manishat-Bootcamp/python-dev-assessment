class Book:
    def __init__(self, title, author, year, summary):
        self.title = title
        self.author = author
        self.year = year
        self.summary = summary

book1 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997, "A young wizard discovers his magical heritage and begins his education at Hogwarts.")
book2 = Book("The Alchemist", "Paul Coelho", 1988, "A Shepherd travels in search of treasure and discovers the meaning of his personal legend.")
book3 = Book("A Man Called Ove", "Fredrik Backman", 2012, "A grumpy yet kind-hearted man forms unexpected connections with his neighbours.")
books = [book1, book2, book3]
for book in books:
    print("Title:", book.title)
    print("Author:", book.author)
    print("Year:", book.year)
    print("Summary:", book.summary)
    print("-" * 30)