from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(1, len(s)+1):
            for word in wordDict:
                if dp[i-len(word)] and s[:i].endswith(word):
                    dp[i] = True

        return dp[-1]


'''
s = 'leetcode'
word_dict = ['leet', 'code']
i =1,2,3 -> nothing
i =4, dp[0] = True, s[:4] = "leet" endswith "leet"
i=5, d[1]=False
i= 6,7 -> nothing
i=8, dp[4]= True, s[:8] = "leetcode" endswith "code"
dp[8]=True
'''