from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        def set_intersection(s1, s2):
            return [i for i in s1 if i in s2]

        if len(set1) < len(set2):
            return set_intersection(set1, set2)
        else:
            return set_intersection(set2, set1)


if __name__ == '__main__':
    sol = Solution()
    sol.intersection([2,3,4,5], [4,5,6,6])

