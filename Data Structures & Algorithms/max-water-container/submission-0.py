class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)-1
        i = 0 
        j = length 
        res = 0
        while i < j:
            area = min(heights[i], heights[j])*length

            res = max(res, area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -=1
            length -= 1
        return res