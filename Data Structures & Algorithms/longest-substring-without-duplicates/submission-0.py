class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupe = set()
        maxy = 0 

        l = 0
        for r in range(len(s)):
            while s[r] in dupe:
                dupe.remove(s[l])
                l+=1
            dupe.add(s[r])

            maxy = max(maxy, len(dupe))

        return maxy
            

        