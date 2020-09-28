from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        excess = []
        pot_pos = []
        for i, (g, c) in enumerate(zip(gas, cost)):
            excess.append(g - c)
            if  g-c > 0:
                pot_pos.append(i)

        if sum(excess) >= 0:
            for pos in pot_pos:
                cumsum = 0
                temp = excess[pos:] + excess[:pos]
                for j in temp:
                    cumsum += j
                    if cumsum < 0:
                        break
                else:
                    return pos
        else:
            return -1

    def o_n(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        gas_tank, start = 0, 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            gas_tank += g -c

            if gas_tank < 0:
                gas_tank =0
                start = i +1

        return start


if __name__ == '__main__':
    sol = Solution()
    print(sol.o_n([5,1,2,3,4], [4,4,1,5,1]))
    print(sol.o_n([1,2,3,4,5], [3,4,5,1,2]))
    print(sol.o_n([5,8,2,8], [6,5,6,6]))
    print(sol.o_n(gas = [2, 3, 4], cost = [3, 4, 3]))

