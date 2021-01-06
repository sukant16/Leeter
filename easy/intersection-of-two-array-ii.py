from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        def find_intersection(x1, x2):

            for i in x1:
                if i in x2:
                    ans.append(i)
                    x2[x2.index(i)] = None
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        if len(nums1) < len(nums2):
            find_intersection(nums1, nums2)
        else:
            find_intersection(nums2, nums1)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
    print(sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))



