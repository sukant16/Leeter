# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B
# to indicate the cows.
# Example 1:
#
# Input: secret = "1807", guess = "7810"
#
# Output: "1A3B"
#
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.


from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = B = 0
        secret_map = Counter(secret)
        for index, num in enumerate(guess):
            if num == secret[index]:
                A += 1
                if secret_map.get(num) <= 0:
                    B -= 1
                else:
                    secret_map.subtract(num)
            elif secret_map.get(num, 0) > 0:
                B += 1
                secret_map.subtract(num)

        return f'{A}A{B}B'

