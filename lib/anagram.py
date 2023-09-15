# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        self.possible_anagrams = possible_anagrams
        self.results = []

        # Thought process
        # Check for a match
        # First sort the words
        # Iterate through the words, if a sigle word sorted equals to the word, then return the word. else return an empty list
        for word in possible_anagrams:
            if sorted(word) == sorted(self.word):
                self.results.append(word)
        
        return self.results
    

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))