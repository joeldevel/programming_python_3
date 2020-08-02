'''
    name: data_types.py
    purpose: show basic python 3 info about data types
    author: joeldevel
    date: August 2020
    usage: in the console: python3 data_types.py
'''
print( '### data types in python 3 \n' )

# We have integer and floats
num = 4
fraction = 6.7
print( 'num = ', num,'is of type', type( num ) )
print( 'fraction = ', fraction,'is of type', type( fraction ) )

# string 
# We can use ' and " to 
word = 'Eine '
words = "kleine nachmusic"
sentence = word + words
print( 'sentece =', sentence,'is of type', type( sentence ) )

# booleans
isItReal = True
print( 'istItReal =', isItReal,'is of type', type( isItReal ) )

