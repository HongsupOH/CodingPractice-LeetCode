from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = defaultdict(list)

    def addWord(self, word) -> None:
        """
        Adds a word into the data structure.
        """
        self.dic[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        if '.' not in word:
            return word in self.dic[len(word)]
        check = []
        for ele in self.dic[len(word)]:
            count = 0
            for i,ch in enumerate(word):
                if ch!=ele[i] and ch!='.':
                    break
                else:
                    count+=1
            if count==len(word):
                check.append(ele)
        if len(check)==0:
            return False
        return True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
