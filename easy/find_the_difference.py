from collections import defaultdict, deque


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = deque(t)
        for i in s:
            t.remove(i)

        return t.pop()


if __name__ == '__main__':

    sol = Solution()
    print(sol.findTheDifference(s = "abcd", t = "abcde"))
