class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = [False] * (len(s) + 1)
        words[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    words[i] = words[i+len(w)]

                if words[i] == True:
                    break

        return words[0]

        