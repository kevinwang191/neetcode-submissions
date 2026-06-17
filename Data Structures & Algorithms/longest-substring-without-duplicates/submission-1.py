class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_t = {}
        start = 0
        max_l = 0 
        for i in range(len(s)):
            if s[i] in hash_t:
                start = max(hash_t[s[i]]+1,start)
            hash_t[s[i]] = i
            length = i - start + 1
            max_l = max(max_l, length)
        return max_l
