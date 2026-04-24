class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        memo = defaultdict(int)

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r >= ROW or c >= COL or obstacleGrid[r][c] == 1:
                return 0
            if r == ROW - 1 and c == COL - 1:
                return 1

            memo[(r, c)] += dfs(r + 1, c)
            memo[(r, c)] += dfs(r, c + 1)

            return memo[(r, c)]

        return dfs(0, 0)