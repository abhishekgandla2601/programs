# Given an integer n. Write a program to return the last digit of the number.
class Solution:
    def lastDigit(self, n: int) -> int:
        # Return the last digit of the number
        return abs(n) % 10
