#String
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#Prints the text
print("Wait there are not 10 things in that list. Let's fix that.")
#Turns ten_things into elements.
stuff = ten_things.split(' ')
#Elements
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#If stuff does not equal to 10, it removes one element from more_stuff.
#Prints adding: (The element that was removed)
#Next it adds an item from next_one to stuff.
#Prints There are (number of how many elements are in stuff) items now.
while len(stuff) != 10:
  next_one = more_stuff.pop()
  print("Adding: ", next_one)
  stuff.append(next_one)
  print(f"There are {len(stuff)} items now.")
#prints the text + every element in stuff.
print("There we go: ", stuff)
#Prints the text
print("Let's do some things with stuff.")
#Prints element number 2
print(stuff[1])
#Prints the 1st from last element in stuff.
print(stuff[-1])
#Prints the element it deletes from stuff.
print(stuff.pop())
#Prints every element in stuff as a string with space between them.
print(' '.join(stuff))
#Prints elements number 4 and 5, number 6 is not included.
print('#'.join(stuff[3:5]))
