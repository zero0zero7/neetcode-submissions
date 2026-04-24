class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for num in nums:
            if num in num_count.keys():
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        top_nums = [list(num_count.keys())[0]]
        top_counts = [list(num_count.values())[0]]
        for num, count in list(num_count.items())[1:]:
            added = False
            for idx in range(len(top_nums)):
                if count <= top_counts[idx]:
                    top_nums.insert(idx, num)
                    top_counts.insert(idx, count)
                    added = True
                    break
                else:
                    continue
            if not added:
                top_nums.append(num)
                top_counts.append(count)
            if len(top_nums) > k:
                top_nums.pop(0)
                top_counts.pop(0)
        return top_nums
