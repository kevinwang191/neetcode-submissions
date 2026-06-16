class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before = [1]*n
        after = [1]*n
        total_b = 1
        for i in range(n):
            before[i] = total_b 
            total_b *= nums[i]
        total_a = 1
        for i in range(n-1, -1, -1):
            after[i] = total_a
            total_a *= nums[i]
        res = [1]*n
        for i in range(n):

            res[i] = before[i] * after[i]

        return res
