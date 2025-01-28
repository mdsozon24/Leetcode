class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def search(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or grid[i][j] == 0: return 0
            fish = grid[i][j]
            visit.add((i, j))
            grid[i][j] = 0
            for di, dj in d:
                fish += search(i + di, j + dj)
            return fish

        res = 0
        visit = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visit:
                    res = max(res, search(i, j))
        return res