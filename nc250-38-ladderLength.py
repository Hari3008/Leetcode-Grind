class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if the word is not present in the word list
        if endWord not in wordList:
            return 0
        
        # Make a adj list for the pattern words
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*"+ word[i+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*"+ word[j+1:]
                    for neiNode in nei[pattern]:
                        if neiNode not in visit:
                            visit.add(neiNode)
                            q.append(neiNode)
            res+=1

        return 0
