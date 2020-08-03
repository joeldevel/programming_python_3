'''
    name: lists.py
    purpose: show basic python 3 lists
    author: joeldevel
    date: Augus 2020
    usage: in the console: python3 lists.py
'''
# A helper to make more readable the output
def separator( description='' ):
    print( 30 * '_' )
    print( description.upper() )

def showResults( list, description ):
    separator( description )
    for element in list:
        print( f"We have a {element}")


# A list is a sequence of elements
ourList = [ 'pencil', 'sketchbook', 'sharpener']

showResults( ourList, 'a list')

# We can add an element to the end
ourList.append('brush');
showResults( ourList, 'append')

# or in some position
ourList.insert(2, "calculator")
showResults( ourList, 'insert')

ourList.pop(-1);
showResults( ourList, 'pop')
