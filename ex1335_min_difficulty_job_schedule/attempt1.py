from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # special cases
        if n == d:
            return sum(jobDifficulty)
        if n < d:
            return -1
        if d == 1:
            return max(jobDifficulty)

        w = n - d + 1  # width of the valid data
        DP = [[float("inf")] * w for _ in range(d - 1)]

        # DP[k][j] = solution of (k+1)-th day, for job from 0th to j-th index

        DP[0] = [max(jobDifficulty[: j + 1]) for j in range(w)]
        for k in range(1, d - 1):  # loop for days:
            for j in range(w):  # loop for joblist (columns)
                #
                last_row = [
                    DP[k - 1][m] + max(jobDifficulty[k + m : k + j + 1])
                    for m in range(j + 1)
                ]

                DP[k][j] = min(last_row)
                print(f"(k={k},j={k+j}): {last_row} -> {min(last_row)}")

            print(DP[k])

        # last row, k = d-1
        k, j = d - 1, w - 1
        last_row = [
            DP[k - 1][m] + max(jobDifficulty[k + m : k + j + 1]) for m in range(j + 1)
        ]
        result = min(last_row)

        return result
