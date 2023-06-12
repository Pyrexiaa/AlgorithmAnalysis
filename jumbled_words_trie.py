import nltk
nltk.download('words')
from nltk.corpus import words

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.secret = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, words, secret):
        node = self.root
        for char in words:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.secret = secret
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        if node.is_end:
            return node.secret
        return None
    
trie = Trie()
# Load the English dictionary
dictionary = words.words()
# Has to add this word into the dictionary cause nltk does not have 'has' this word
dictionary.append('has') 
for i in dictionary:
    sorted_word = "".join(sorted(i.lower()))
    trie.insert(sorted_word, i)

jumbled_words = ['haTt', 'enPros', 'asH', 'eMvito']
for word in jumbled_words:
    sorted_word = "".join(sorted(word.lower()))
    secret = trie.search(sorted_word)
    if secret:
        decrypted = secret[0].upper() + secret[1:].lower()
        print(f"Jumbled Word: {word}, Decrypted Word: {decrypted}")
    else:
        print("No Match Found")