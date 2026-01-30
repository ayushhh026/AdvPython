# Magic methods = Dunder methods (double underscore) __init__,__Str__ etc
#                 They are automatically called by many of Pythons's built-in operations.
#                 They allow developers to define or customize the behavior of objects


class Book:
    def __init__(self, title, author, num_pages):
        self.title= title
        self.author = author
        self.num_pages=num_pages

    def __str__(self): # Allows you to write directly print the objects without the methods 
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
        
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title

book1 = Book("The Hobbit", "J.R.R Tolkien",310)
book2 = Book("Harry potter", "J.K. Rowling",210)
book3 = Book("Harry potter", "J.K. Rowling",223)

print(book1) 
print(book3 == book2) # eq allow change the behavior of the object

# normally if you use print(book2<book3)
# you get this error  --TypeError: '<' not supported between instances of 'Book' and 'Book'

print(book2<book3)
print(book2>book3)
print(book1.num_pages + book2.num_pages) #this works properly but print(book1+book2) wil give error to fix that make dunder add method
print(book1+book2)#encapsulation not showing what are we adding 

print("Harry" in book3)

print(book1['title'])