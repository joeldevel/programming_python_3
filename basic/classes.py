'''
    name: classes.py
    purpose: show basic python 3 classes
    author: joeldevel
    date: Augus 2020
    usage: in the console: python3 classes.py
'''
# a class is like a template for create many
# object
class book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def data(self):
        print(f"title: {self.title}, author: {self.author}")

# Let's create a book instance
principia = book( 'Philosophiæ Naturalis Principia Mathematica','Newton', 1687)
# use a method book
principia.data()
