'''
    name: functions.py
    purpose: show basic python 3 functions
    author: joeldevel
    date: Augus 2020
    usage: in the console: python3 functions.py
'''

# To create a function we use the def keyword
def print_something():
    print("Welcome to the world of functions!")

# and we call them like this
print_something()

# We can of course pass them arguments
def join_words( word1, word2):
    return word1 + ' ' + word2 + '!'

print( join_words( "hello", "Johan") )
