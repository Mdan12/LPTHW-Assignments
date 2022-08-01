
# prints the sentence How old are you? WITH SPACE AFTERWARDS INSTED OF return
print("How old are you?", end=' ')
# User input
age = input()
# Print the sentence How tall are you? WITH SPACE AFTERWARDS INSTED OF return
print("How tall are you?", end=' ')
# User input
height = input()
# Print the sentence How much do you weigh? WITH SPACE AFTERWARDS INSTED OF return
print("How much do you weigh?", end=' ')
# User input
weight = input()

# Prints So, you're (result of 1st user input) old, (result from 2nd user input)
# tall and (result from 3rd input) heavy.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Imports argv functions from sys to this code. Easier to import functions
# than have all the functions already avaiable in all scripts.
# If all are imported, every script would big a huge file.
from sys import argv

# These are the arguments used for argv.
script, filename = argv

# opens the name of the file that user inputs when opening this script.
# F.ex. if I want to run this script and open ex14.py I would Type
# python ex26.py ex14.py making filename = ex14.py and script = ex26.py
txt = open(filename)

# Prints Here's your file ex14.py (In this case it's ex14.py,
# can be any file you open). f before the string makes it so you can
# use functions inside of the string.
print(f"Here's your file {filename}:")
# Reads everything inside the file, letting user see it in PowerShell
print(txt.read())
# Prints Type the filename again:
print("Type the filename again:")
# prints >  and allows for user input.
file_again = input("> ")

# Opens the file user wrote in the input. Doesn't have to be the same file
# as before but it opens it.
txt_again = open(file_again)

# Reads everything inside the file for user.
print(txt_again.read())

# Prints Let's practice everything
print('Let\'s practice everything.')
# Prints You'd need to know 'bout escapes with \ that do
# newlines and      tabs.
print('''You\'d need to know \'bout escapes)
      with \\ that do \n newlines and \t tabs.''')

#Literally just a string. \n is return, \t is tab.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Prints ------------
print("--------------")
# Prints the poem from line 59 - 64
print(poem)
# Prints ------------
print("--------------")

# This is an integer literal
five = 10 - 2 + 3 - 6

# Prints This should be five: (The result of five, which in this case is 5)
# f again is for using functions within a string.
print(f"This should be five: {five}")

# This is a def function. started is the argument.
# secret_formula is the function name.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# This is a temporary function made just for the function's run.
# In this case start_point replaces started.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Prints With a starting point of: (The result of start point,
# which in this case is 10000)
print("With a starting point of: {}".format(start_point))
# Prints We'd have (The result of 10000 * 500) beans, (The result of beans / 1000)
# jars, and (the result of jars / 100).
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.".format(start_point))
# This changes the function temporarily of start_point to the result of 10000 / 10
start_point = start_point / 10
# Prints We can also do that this way:
print("We can also do that this way:")
# formula is the result secret_formula(start_point). It just makes the writing
# shorter.
formula = secret_formula(start_point)
# prints We'd have (the result of beans) beans, (the result of jars) jars,
# and (the result of crates) crates.
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.".format(start_point))

# integers
people = 20
cats = 30
dogs = 15

# If the result of cats is a higher number than the result of people,
# it prints Too many cats! The world is doomed!
if people < cats:
    print("Too many cats! The world is doomed!")
# If the result of people is a higher number than the result of cats,
# it prints Not many cats! The world is saved!
if people > cats:
    print("Not many cats! The world is saved!")
# Same applies to this one, more dogs prints The world is drooled on!
if people < dogs:
    print("The world is drooled on!")
# Fewer dogs prints The world is dry!
if people > dogs:
    print("The world is dry!")

# This literally adds 5 to the result of dogs we had previous.
# Making dogs = 20
dogs += 5
# Same as before, but this time it's if people are more or the same as dogs
# it prints People are greater than or equal to dogs
if people >= dogs:
    print("People are greater than or equal to dogs.")
# Prints People are less than or equal to dogs if there are more dogs,
# or the same amount.
if people <= dogs:
    print("People are less than or equal to dogs.")
# Prints if there are just as many dogs as people.
if people == dogs:
    print("People are dogs.")
