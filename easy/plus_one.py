from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return [1]
        elif digits[n-1] < 9:
            digits[n-1] += 1
            return digits
        else:
            digits[n-1] = 0
            digits[:n-1] = self.plusOne(digits[:n-1])
            return digits

    def non_recursive_solution(self,  digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - i - 1
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([9, 9]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.non_recursive_solution([9, 9]))
    print(sol.non_recursive_solution(([4, 3, 2, 1])))