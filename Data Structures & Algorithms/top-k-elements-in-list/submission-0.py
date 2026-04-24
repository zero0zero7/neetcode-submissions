class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            print(num_count)
            if num in num_count.keys():
                num_count[num] += 1
            else:
                num_count[num] = 1
        sorted_num_count = dict(sorted(num_count.items(), reverse=True, key = lambda x: x[1]))
        return list(sorted_num_count.keys())[:k]