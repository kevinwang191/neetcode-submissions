class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            cur = nums[i]
            diff = target - cur  
            
            if diff in seen:
                return [seen[diff], i] 

            seen[cur] = i 