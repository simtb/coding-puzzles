class Solution:
    def can_transform(self, a: str, b: str) -> bool:
        n: int = len(a)
        diff: int = 0
        can: bool = True
        
        for i in range(n):
            if (a[i] != b[i]):
                diff += 1
                if diff > 1:
                    can = False
                    break
        return can
    

            
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ans: int = None
        seen: set = set()
        
        queue: deque = deque()
        
        queue.appendleft((beginWord, 1))
        seen.add(beginWord)
        i = 0
        while (queue and ans == None):
            i += 1
            current: tuple = queue.pop()
            current_word: str = current[0]
            transformations: int = current[1]
                
            if current_word == endWord:
                print(i)
                ans = transformations
                break
            for word in wordList:
                if (word not in seen and self.can_transform(current_word, word)):
                    queue.appendleft((word, transformations + 1))
                    seen.add(word)
        if ans is None:
            return 0
        else:
            return ans