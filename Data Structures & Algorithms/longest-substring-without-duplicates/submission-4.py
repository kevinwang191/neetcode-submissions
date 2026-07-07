class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char = set()
        total = 0
        if len(s) == 0:
            return 0
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[l])
                l+=1
            char.add(s[right])
            total = max(total , right-l + 1)
        return total