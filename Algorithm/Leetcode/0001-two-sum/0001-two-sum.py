class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [idx, dic[target - num]]
            
            dic[num] = idx
        