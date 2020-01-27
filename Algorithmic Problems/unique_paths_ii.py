class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = [[0 for i in range(len(obstacleGrid[0]))]
                for j in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue  # Obstacle is here, so no path can be created
                elif i == 0 and j == 0:
                    memo[i][j] = 1  # Starting position of the grid
                elif i-1 < 0:
                    memo[i][j] = memo[i][j-1]
                elif j-1 < 0:
                    memo[i][j] = memo[i-1][j]
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]

        # Return the summed value of the bottom right corner
        return memo[-1][-1]
