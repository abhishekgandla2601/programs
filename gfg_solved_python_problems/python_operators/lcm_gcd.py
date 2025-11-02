# Given two integers a and b, You have to compute their LCM and GCD and return an array
# containing their LCM and GCD.

class Solution:
    def lcmAndGcd(self, a: int, b: int) -> list[int]:
        # Find GCD using Euclidean algorithm
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        g = gcd(a, b)
        # LCM formula: (a * b) // gcd(a, b)
        l = (a * b) // g

        # Return [LCM, GCD]
        return [l, g]
