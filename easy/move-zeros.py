class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1

            fast += 1

    def for_loop(self, nums: list) -> None:
        pt = 0
        for i in range(len(nums)):
            if nums[pt] == 0 and nums[i] != 0:
                nums[pt], nums[i] = nums[i], nums[pt]

            if nums[pt] != 0:
                pt += 1