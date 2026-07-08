class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        res = 1
        q = deque()
        visit = set()

        q.append(beginWord)
        visit.add(beginWord)
        
        pat = collections.defaultdict(list)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                pat[pattern].append(w)

        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j+1:]
                    for nei in pat[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1
        return 0










        