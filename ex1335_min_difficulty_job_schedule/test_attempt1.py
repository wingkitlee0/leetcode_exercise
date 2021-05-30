from attempt1 import Solution


class TestAttempt1:
    def test_0001(self):
        sol = Solution()
        result = sol.minDifficulty(
            jobDifficulty=[6, 5, 4, 3, 2, 1],
            d=2,
        )
        assert result == 7

    def test_0002(self):
        sol = Solution()
        result = sol.minDifficulty(
            jobDifficulty=[1, 1, 1],
            d=3,
        )
        assert result == 3

    def test_0003(self):
        sol = Solution()
        result = sol.minDifficulty(
            jobDifficulty=[9, 9, 9],
            d=4,
        )
        assert result == -1

    def test_0004(self):
        sol = Solution()
        result = sol.minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3)
        assert result == 15

    def test_0005(self):
        sol = Solution()
        result = sol.minDifficulty(
            jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444],
            d=6,
        )
        assert result == 843
