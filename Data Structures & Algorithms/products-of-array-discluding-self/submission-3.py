class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1]
        for i in range(1, len(nums)):
            left_prods.append(left_prods[i-1]*nums[i-1])
        right_prods = [1]
        for i in range(len(nums)-2, -1, -1):
            right_prods.insert(0, right_prods[0]*nums[i+1])
        ans = []
        # print(left_prods, right_prods)
        for i in range(len(nums)):
            ans.append(right_prods[i] * left_prods[i])
        return ans