class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(map(lambda x: 1 - len(str(x))%2, nums))
