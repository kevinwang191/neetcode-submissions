class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        hash_t = defaultdict(list)
        res = {}
        for n in nums:
           hash_t[n]
        for n in nums:
            if n-1 not in hash_t:
                res[n] = 1
        for n in res:
            cur = n
            while cur+1 in hash_t:
                res[n] += 1
                cur += 1
        return max(res.values())
           
                