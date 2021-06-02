from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def find_intersection(l1, l2):
            ans = []
            counts = defaultdict(int)
            for i in l2:
                counts[i] += 1

            for j in l1:
                if counts[j] > 0:
                    ans.append(j)
                    counts[j] -= 1

            return ans

        if len(nums1) > len(nums2):
            return find_intersection(nums1, nums2)
        else:
            return find_intersection(nums2, nums1)

    def sorted_approach(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = j = k = 0
        while i < len(nums1):

            while j < len(nums2):

                if nums1[i] < nums2[j]:
                    i += 1
                    break
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    nums1[k] = nums1[i]
                    k += 1
                    j += 1
                    i += 1
                    break

        return nums1[:k]


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

    print(sol.sorted_approach(nums1=[1, 2, 2, 1], nums2=[2, 2]))
    print(sol.sorted_approach(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))



