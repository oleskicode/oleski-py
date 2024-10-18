class WordCounter:

    known_words = {}

    def add_word(self, word: str):
        if word in self.known_words:
            self.known_words[word] += 1
        else:
            self.known_words[word] = 1  # key value =1

    def get_count(self, word: str) -> int:
        if word in self.known_words:
            return self.known_words[word]
        else:
            return 0

    def __str__(self):
        return str(self.known_words)


wc = WordCounter()
wc.add_word("apple")
wc.add_word("apple")
wc.add_word("apple")
wc.add_word("banana")
wc.add_word("banana")

print(wc)

assert wc.get_count("apple") == 3
assert wc.get_count("banana") == 2
assert wc.get_count("cucumber") == 0
