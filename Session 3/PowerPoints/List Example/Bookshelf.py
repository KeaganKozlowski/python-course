# Creating an empty bookshelf
bookshelf = []
# Adding books to the bookshelf
bookshelf.append("Harry Potter")
bookshelf.append("Lord of the Rings")

print("My bookshelf after adding books:", bookshelf)
# Removing a book from the bookshelf 
removed_book = bookshelf.pop(1)  # Removing the book at index 1 
print("Removed book:", removed_book)
print("My bookshelf after removing a book:", bookshelf)
# Rearranging books on the bookshelf 
bookshelf[1] = "Game of Thrones"
print("My bookshelf after rearranging books:", bookshelf)
# Accessing a book on the bookshelf
first_book = bookshelf[0]
print("The first book on my bookshelf:", first_book)