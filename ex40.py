# Class Song has-a __init__ that takes self and lyrics parameters.
# Class is king.
# __init__ is required to create objects and is the core of object-oriented programming
class Song(object):
# self is a method, lyrics is the parameter.
# self represents the instance of the class. By using the self,
# we can access the attributes and methods of the class in python.
    def __init__(self, lyrics):
# lyrics is the object for the method self has the argument lyrics.
        self.lyrics = lyrics
# defines sing_me_a_song with self as the parameter
    def sing_me_a_song(self):
# For every line in self.lyrics it prints the line.
        for line in self.lyrics:
            print(line)

# happy_bday is the result of the class Song. Song now has a string attached to it.
happy_bday = Song(["Happy Birthday to you",
"I don't want to get sued",
"So I'll stop right there"])
# Same as happy_birthday but different string attached.
bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

# This prints every line in happy_bday because sing_me_a_song prints every line
# in the song.
happy_bday.sing_me_a_song()
# Same as before but with the string in bulls_on_parade
bulls_on_parade.sing_me_a_song()
