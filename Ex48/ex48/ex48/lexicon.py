direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
fillers = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']



def scan(input):
    sentence = []
    lexicon = {'north': 'direction',
               'south': 'direction',
               'east': 'direction',
               'go': 'verb',
               'kill': 'verb',
               'eat': 'verb',
               'the': 'stop',
               'in': 'stop',
               'of': 'stop',
               'bear': 'noun',
               'princess': 'noun'
               }

    words = input.split() # Splits input(which is defined in other file)
    # into a list where each word is an item.
    for word in words: # for loop, used to iterate over the list.
        if word in lexicon.keys(): # if one of the items in the list is a keyname
        #in the dictionary lexicon.
            sentence.append((lexicon[word], word)) # adds the word plus its value to sentence

        elif word.isdigit(): # but if a item in list is a number
            word = int(word) # makes the item (which is a string) into an integer
            sentence.append(('number', word)) #adds 'number' and the int to sentence
        else: #if none of the two above apply
            sentence.append(('error', word)) # it adds 'error' and the item to sentence
    return sentence # used to exit for loop.
