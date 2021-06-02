from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costA = []
        refunds = []
        for i in costs:
            costA.append(i[0])
            refunds.append(i[1] - i[0])
        total_cost = sum(costA)
        n = int(len(costs) / 2)
        min_cost = total_cost + sum(sorted(refunds)[:n])
        return min_cost


if __name__=='__main__':
    sol = Solution()
    costs = [[10,20],[30,200],[400,50],[30,20]]
    print(sol.twoCitySchedCost(costs))