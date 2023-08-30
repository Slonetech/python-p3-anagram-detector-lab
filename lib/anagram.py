class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        self.word_list = word_list
        matches = []
        for word in self.word_list:
            if sorted(word) == sorted(self.word):
                matches.append(word)
        return matches

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])