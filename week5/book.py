from datetime import datetime

class Book:
    """A Book class demonstrating Python OOP fundamentals"""
    
    def __init__(self, title, author, year, isbn):
        """Initialize a Book instance with public and private attributes"""
        # Public instance attributes
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        
        # Private attribute (name-mangled)
        self.__checkout_count = 0
    
    def __str__(self):
        """Return human-friendly string representation"""
        return f"{self.title} by {self.author} ({self.year})"
    
    def __repr__(self):
        """Return developer-friendly string representation"""
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.isbn}')"
    
    def __eq__(self, other):
        """Books are equal if they have the same ISBN"""
        if not isinstance(other, Book):
            return False
        return self.isbn == other.isbn
    
    def checkout(self):
        """Increment the private checkout counter"""
        self.__checkout_count += 1
    
    def get_stats(self):
        """Return a dictionary with title and checkout count"""
        return {
            'title': self.title,
            'checkouts': self.__checkout_count
        }
    
    def age(self):
        """Calculate how old the book is"""
        current_year = datetime.now().year
        return current_year - self.year