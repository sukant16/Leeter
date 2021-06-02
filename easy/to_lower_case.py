class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(char)+32) if (64<ord(char)<91) else char for char in str])

if __name__ == '__main__':
    sol = Solution()

    ans1 = sol.toLowerCase("hEllO")
    assert (ans1 == "hello"), 'wrong'

    ans2 = sol.toLowerCase("LOVELY")
    assert (ans2 == "lovely"), 'wrong'