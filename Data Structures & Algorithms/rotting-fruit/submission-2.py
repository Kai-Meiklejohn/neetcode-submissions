class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_fruits = set()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruits.add((r, c))

        minutes = 0
        while q and fresh_fruits:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        fresh_fruits.discard((nr, nc))
                        q.append((nr, nc))
                        grid[nr][nc] = 2
            minutes += 1

        return minutes if not fresh_fruits else -1

