class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                slow_temp = nums[slow]
                fast_temp = nums[fast]
                nums[fast] = slow_temp
                nums[slow] = fast_temp
            if nums[slow] != 0:
                slow += 1
        return nums
                