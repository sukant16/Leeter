'''
Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri],
for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ).
Return an array containing the result for the given queries.

Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
The binary representation of the elements in the array are:
1 = 0001
3 = 0011
4 = 0100
8 = 1000
The XOR values for queries are:
[0,1] = 1 xor 3 = 2
[1,2] = 3 xor 4 = 7
[0,3] = 1 xor 3 xor 4 xor 8 = 14
[3,3] = 8
'''

from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_arr = [0]
        for a in arr:
            xor_arr.append(xor_arr[-1]^a)

        ans = []
        for i, j in queries:
            ans.append(xor_arr[j+1] ^ xor_arr[i])
        return ans

if __name__=='__main__':
    sol = Solution()
    ans1 = sol.xorQueries(arr=[1,3,4,8], queries=[[0,1],[1,2],[0,3],[3,3]])
    assert(ans1 == [2,7,14,8]), 'wrong logic'

    ans2 = sol.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]])
    assert(ans2 == [8,0,4,4]), 'wrong logic'