import nltk
nltk.download('words')
from nltk.corpus import words
from itertools import permutations

def find_valid_words(jumbled_words, dictionary):
    valid_words = []
    
    for jumbled_word in jumbled_words:
        permutations_list = [''.join(p) for p in permutations(jumbled_word)]
        permutations_list = [word.lower() for word in permutations_list if word[0].isupper()]
        # Check each permutation against the dictionary
        for word in permutations_list:
            if word in dictionary:
                valid_words.append(word)
                break 
    
    return valid_words

# Load the English dictionary
dictionary = words.words()
# Has to add this word into the dictionary cause nltk does not have 'has' this word
dictionary.append('has') 

# Example usage
jumbled_words = ['haTt', 'enPros', 'asH', 'eMvito']
valid_words = find_valid_words(jumbled_words, dictionary)
print(valid_words)