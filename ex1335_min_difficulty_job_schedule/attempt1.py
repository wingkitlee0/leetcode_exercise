from typing import List
import sys


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
        # DP = [[float("inf")] * w for _ in range(d - 1)]
        # DP[k][j] = solution of (k+1)-th day, for job from 0th to j-th index

        # last_row of DP
        last_row = [max(jobDifficulty[: j + 1]) for j in range(w)]

        for k in range(1, d - 1):  # loop for days:
            current_row = [None for _ in range(w)]

            for j in range(w):  # loop for joblist (columns)
                max_job_diff = jobDifficulty[k + j]
                min_value = float("inf")
                for m in range(j + 1):
                    current = jobDifficulty[k + j - m]
                    if current > max_job_diff:
                        max_job_diff = current

                    value = last_row[j - m] + max_job_diff

                    if value < min_value:
                        min_value = value

                current_row[j] = min_value

            last_row = current_row

        # last row, k = d-1
        k, j = d - 1, w - 1
        # last_row = [
        #     DP[k - 1][m] + max(jobDifficulty[k + m : k + j + 1]) for m in range(j + 1)
        # ]
        current_row = [
            last_row[m] + max(jobDifficulty[k + m : k + j + 1]) for m in range(j + 1)
        ]
        result = min(current_row)

        return result
