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
# Same as before, but this time if the people are more or equal to dogs
# it prints People are greater than or equal to dogs
if people > dogs:
    print("People are greater than or equal to dogs.")
#
if people < dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
