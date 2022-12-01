class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target-nums[i] in seen:
                return([i, seen[target-nums[i]]])
            else:
                seen[n] = i 
        return [] 