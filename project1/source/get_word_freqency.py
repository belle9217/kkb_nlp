import json
def get_word_frequency(word):
    with open('dictionary.json', 'r') as f:
        dictionary = json.load(f)
    if word in dictionary:
        return dictionary[word]
    else:
        return 1e-10
