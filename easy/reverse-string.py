from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s)-1
        start = 0
        half = int((end+1)/2)
        while start < half:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1


if __name__=="__main__":
    sol = Solution()
    s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
    print(s)
    sol.reverseString(s)
    print(s)