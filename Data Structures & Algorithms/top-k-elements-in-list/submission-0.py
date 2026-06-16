class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq_list = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_list[freq].append(num)
        res = []
        for i in range(len(freq_list)-1, 0,-1):
            for n in freq_list[i]:
                res.append(n)

                if len(res) == k:
                    return res
