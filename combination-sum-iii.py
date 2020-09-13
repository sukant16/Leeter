from typing import List
from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        max_num = min(n, 10)
        return [list(comb) for comb in combinations(range(1, max_num), k) if sum(comb) == n]


