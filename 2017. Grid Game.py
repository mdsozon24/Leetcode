class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        prefix_top = [0] * n
        prefix_bottom = [0] * n

        prefix_top[0] = grid[0][0]
        prefix_bottom[0] = grid[1][0]

        for j in range(1, n):
            prefix_top[j] = prefix_top[j - 1] + grid[0][j]
            prefix_bottom[j] = prefix_bottom[j - 1] + grid[1][j]

        result = float('inf')
        for j in range(n):
            top_remaining = prefix_top[-1] - prefix_top[j]
            bottom_remaining = prefix_bottom[j - 1] if j > 0 else 0

            result = min(result, max(top_remaining, bottom_remaining))

        return result
