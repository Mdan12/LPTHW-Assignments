# These are lists.
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# For every result in the_count it will print This is count (first item inside
# the list), return, This is count (2nd item inside the list) and on and on.
for number in the_count:
    print(f"This is count {number}")

# Same as for number, but it prints every result of fruits.
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Same as for change, but it prints every result of change.
for i in change:
    print(f"I got {i}")

# This too is a list,
elements = []

# In this case it gives it a range from 0 - 5 (Because 6 equals to 5).
for i in range(0, 6):
    print(f"Adding {i} to the list.")
# This adds i to the elements list, making elements = [0, 1, 2, 3, 4, 5]
    elements.append(i)
# Same as line 12 and 13
for i in elements:
    print(f"Element was: {i}")
