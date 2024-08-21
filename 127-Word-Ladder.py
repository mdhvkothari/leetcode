from typing import List


"""
    eg -    hit      ---- level 1
            / 
          hot        ---- level 2
           /\ 
         dot lot     ---- level 3
         /\   /\

"""

class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [(beginWord, 1)]
        s = set(wordList)
        s.discard(beginWord)
        while q:
            word, distance = q.pop(0)
            if word == endWord:
                return distance
            for i in range(len(word)):
                for j in range(ord('a'), ord('z')+1):
                    new_word = word[:i] + chr(j) + word[i+1:]
                    if new_word in s and word != endWord:
                        q.append((new_word, distance+1))
                        s.discard(new_word)
        return 0

        


