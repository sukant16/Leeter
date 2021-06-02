class Solution:
    def __init__(self):
        self.squares_list = []

    def isHappy(self, n: int):
        nums = list(map(lambda x: int(x), list(str(n))))
        squares_sum = sum([i * i for i in nums])
        if squares_sum == 1:
            return True
        elif squares_sum in self.squares_list:
            return False
        else:
            self.squares_list.append(squares_sum)
            return self.isHappy(squares_sum)


if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(19), "wrong logic"
    assert sol.isHappy(25), "Wrong logic"