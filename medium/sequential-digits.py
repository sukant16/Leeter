from typing import List
from math import nan


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        start = 10
        start_len = end_len = 1
        for i in range(1, 10):
            if (low // (10 ** i) < 10) and (low // (10 ** i) > 0):
                start = low // (10 ** i)
                start_len = i

            if (high // (10 ** i) < 10) and (high // (10 ** i) > 0):
                # end = high // (10 ** i)
                end_len = i
                break
        print(start_len, end_len, start)

        def gen_num(digit, num_length):
            if digit > 9:
                return nan
            elif num_length > 0:
                return digit * (10 ** num_length) + gen_num(digit+1, num_length-1)
            else:
                return digit

        for l in range(start_len, end_len+1):
            for s in range(1, 9):
                num = gen_num(s, l)
                if (num is not nan) and (num <= high) and (num >= low):
                    ans.append(num)
        return ans

    def better_solution(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []

        for i in range(2, 10):
            for j in range(0, 9):
                # 2 -> 12 23 34 45 ...
                # 3 ->  123 234 345 ..
                if i + j < 10:
                    num = int(s[j:i+j])
                    # print(num)
                    if low <= num <= high:
                        ans.append(num)
                    elif num > high:
                        break
            else:
                continue
            break
        return ans

    def sol_using_deque(self, low: int, high: int) -> List[int]:
        ans = []
        from collections import deque

        queue = deque(range(1,10))

        while queue:
            elem = queue.popleft()
            if elem > high:
                break
            elif low <= elem <= high:
                ans.append(elem)

            last_digit = elem % 10
            if last_digit < 9: queue.append(elem*10 + last_digit + 1)

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.better_solution(234, 2314))
    # print(sol.better_solution(10, 99))
    print(sol.better_solution(10, 30000))

    print(sol.sol_using_deque(234, 2314))
    # print(sol.better_solution(10, 99))
    print(sol.sol_using_deque(10, 30000))

