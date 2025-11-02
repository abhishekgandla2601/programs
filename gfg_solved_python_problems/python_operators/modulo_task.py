# Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).

class Solution:
    def modTask(self, N):
        # If N = 1, return 1 (as per test case)
        if N == 1:
            return 1

        # For N >= 2, best K is floor(N/2) + 1, but ensure K < N
        k = N // 2 + 1
        if k >= N:
            k = N - 1
        return k
