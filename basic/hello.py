'''
    name: hello.py
    purpose: show basic python 3 features
    author: joeldevel
    date: July 2020
    usage: in the console: python3 hello.py
'''
# In python 3 print requires the use of parenteheses
# This is how we print to the screen
print ( "hello" )

# A variable does not need a key word, nor a type
words_to_the_public = "We must fight from the inside"
print ( words_to_the_public )

# And the content type can change
words_to_the_public = 4444

print( words_to_the_public )

# We can interpolate variables' values like this
car_brand = "Mercedes Benz"
someone_desire = f"I want to buy a { car_brand }"
print( someone_desire )

# And create a string with break lines without using scape characters
juliet_said = """O Romeo, Romeo! wherefore art thou Romeo?
Deny thy father and refuse thy name;
Or, if thou wilt not, be but sworn my love,
And I'll no longer be a Capulet
"""
print( juliet_said )
