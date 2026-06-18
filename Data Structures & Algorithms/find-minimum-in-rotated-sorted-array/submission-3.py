class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        if right == left:
            return nums[0] 
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid] > nums[left]:
                    left = mid+1
                else:
                    right = mid
                
