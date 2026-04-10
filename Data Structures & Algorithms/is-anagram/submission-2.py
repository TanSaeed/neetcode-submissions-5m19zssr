class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

    # Python lets you use Counter as well, so you could just do:
    #  return Counter(s) == Counter(t)

    # You could also try soritng but this will give you a O(nlogn) and O(1 or n) for sorting
    # return sorted(s) == sorted(t)

        