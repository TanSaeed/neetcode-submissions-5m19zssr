class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        maxf = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # We can use this to make time go from
                                          # O(26n) to O(n)

            while (r-l+1) - maxf > k:
                count[s[l]] =  count.get(s[l]) - 1
                l+=1

            res = max(res, r-l +1) 
        return res

        