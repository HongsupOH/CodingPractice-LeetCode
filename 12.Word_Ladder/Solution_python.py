class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        solution using bfs
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = [[beginWord]]
        visit = set()
        best = float('inf')
        while queue:
            path = queue.pop(0)
            word = path[-1]
            if word==endWord:
                best = min(best,len(path))
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i]+j+word[i+1:]
                    if new_word in wordSet and new_word not in visit:
                        new_path = path + [new_word]
                        visit.add(new_word)
                        queue.append(new_path)
        if best==float('inf'):
            return 0
        return best
    
