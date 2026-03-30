class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crawl = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in crawl.children:
                crawl.children[char] = TrieNode()
            crawl = crawl.children[char]
        
        crawl.isEndOfWord = True
        return 
        

    def search(self, word: str) -> bool:
        crawl = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in crawl.children:
                return False
            crawl = crawl.children[char]
        
        return crawl.isEndOfWord

        

    def startsWith(self, word: str) -> bool:
        crawl = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in crawl.children:
                return False
            crawl = crawl.children[char]
        
        return True
        