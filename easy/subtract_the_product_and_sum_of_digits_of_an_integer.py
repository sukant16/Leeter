from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        prod = reduce(lambda x, y: x*y, digits)
        add = sum(digits)
        return (prod - add)
