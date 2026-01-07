# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self._sorted_word = sorted(self.word)

    def match(self, words):
        matchingList = []

        for word in words:
            lower_word = word.lower()

            if lower_word == self.word:
                continue

            if self._sorted_word == sorted(lower_word):
                matchingList.append(word)

        return matchingList

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])



