class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        clean_set = set()

        # Step 1: initialise
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    clean_set.add((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        # Step 2: BFS
        while q and clean_set:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        clean_set.discard((nr, nc))
                        q.append((nr, nc))
            minutes += 1

        # Step 3: return result
        return minutes if not clean_set else -1
