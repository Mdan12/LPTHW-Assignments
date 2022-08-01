# imports functions from random, urlopen and sys to make coding easier.
import random
import urllib.request
import sys

# Strings.
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# This is a dictionary
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** ='***'":
        "From *** get the *** attribute and set it to '***'."
}

# If the word count in sys.argv equals to 2 and the word is english, it's True
# otherwise it's false.
# This only applies if you run the script with a 2nd word after python scriptname.
# If you don't type in a second word it doesn't do any of these.
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# readlines - reads the lines from the url in line 7.
# append - adds a single item to the existing list.
# strip - removes any spacing before the word and after the word.
# utf-8 - often the default encoding for python. UTF stands for unicode transformation format.
for word in urllib.request.urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

# This is a def function. snippet and phrase are the arguments
# convert is the function name.
def convert(snippet, phrase):
# class names is the result of random word in WORDS and capitalizes the first letter
# It also replaces %%% with the word.
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
# other_names is the result of a random word in WORDS that replaces *** in PHRASES
    other_names = random.sample(WORDS, snippet.count("***"))
# 2 strings.
    results = []
    param_names = []
# For the first word in i it replaces @@@ with that word.
    for i in range(0, snippet.count("@@@")):
# returns a random number between 1 and 3.
        param_count = random.randint(1,3)
# returns a random word from WORDS with a random number but all spaces are removed
# Except there's a comma and a space between the two, nothing else.
        param_names.append(', '.join(random.sample(WORDS, param_count)))
# Returns a : when using result.
    for sentence in snippet, phrase:
        result = sentence[:]

    #fake class names
# Replaces %%% with a word, and another word with : between the two.
        for word in class_names:
            result = result.replace("%%%", word, 1)

    #fake other names
# replaces *** with a word and another word with : betweehn the two.
        for word in other_names:
            result = result.replace("***", word, 1)

    #fake parametere lists
# replaces @@@ with a word and another word with : betweehn the two.
        for word in param_names:
            result = result.replace("@@@", word, 1)
# Adds result to results.
        results.append(result)
#sends the result back to the caller.
    return results

# keep going until they hit CTRL-D
# Lets me test the code for errors.
try:
# when it's true
    while True:
# Turns PHRASES into a list, meaning every word in PHRASES will have a seperate string.
# keys() returns a view object that displays a list of all the keys.
        snippets = list(PHRASES.keys())
# Shuffles around snippets, making the words random.
        random.shuffle(snippets)

        for snippet in snippets:
# Result of PHRASES[snippet]
            phrase = PHRASES[snippet]
# question and answer both are the result of what convert was defined as.
            question, answer = convert(snippet, phrase)

            if PHRASE_FIRST:
# This makes the question = answer and answer = question.
                question, answer = answer, question
# prints result of question.
            print(question)
# User input after >
            input("> ")
# Prints answer followed by the result of answer.
            print(f"ANSWER:  {answer}\n\n")
# If these do not work, it prints
# Bye
except EOFError:
    print("\nBye")
