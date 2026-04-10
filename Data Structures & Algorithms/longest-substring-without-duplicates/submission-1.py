class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxy = 0
        l = 0
        holder = set()

        for r in range(len(s)):
            while s[r] in holder:
                holder.remove(s[l])
                l+=1
            holder.add(s[r])

            maxy = max(maxy, len(holder))

        return maxy
            

        