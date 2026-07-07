class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            seen[n] = i 
        for i, n in enumerate(nums):
            if target - n in seen and seen[target- n] != i:
                return [i, seen[target- n]]