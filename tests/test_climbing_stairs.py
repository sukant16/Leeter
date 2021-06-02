import unittest

from easy.climbing_stairs import Solution 


class TestClimbStairs(unittest.TestCase):
    def test_example_1(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(3), 3, "Number of ways to climb 3 stairs should be 3") 


if __name__ == "__main__":
    unittest.main()