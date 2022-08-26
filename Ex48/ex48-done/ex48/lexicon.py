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
    words = input.split()
    for word in words:
        if word in lexicon.keys():
            sentence.append((lexicon[word], word))
        elif word.isdigit():
            word = int(word)
            sentence.append(('number', word))
        else:
            sentence.append(('error', word))
    return sentence
