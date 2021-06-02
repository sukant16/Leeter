class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        step = 2 if len(s) % 2 else 1
        for i in range(1, len(s) // 2 + 1, step):
            if s[:i] * (len(s) // i) == s:
                return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        s_fold = s[1:] + s[:-1]

        return s in s_fold


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedSubstringPattern("abab"))
    print(sol.repeatedSubstringPattern("aba"))
    print(sol.repeatedSubstringPattern("abaabaaba"))
    print(sol.repeatedSubstringPattern("aaaaaaaaaaaaa"))
    print(sol.repeatedSubstringPattern2("a"))
    print(sol.repeatedSubstringPattern("abccbabccbabccbabccbabccb"))

