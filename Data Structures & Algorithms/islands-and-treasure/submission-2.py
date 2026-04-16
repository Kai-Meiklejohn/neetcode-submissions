class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def add_to_queue(r, c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or
                grid[r][c] == -1):
                return 
            
            q.append((r, c))
            visited.add((r, c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        counter = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = counter

                add_to_queue(r + 1, c)
                add_to_queue(r - 1, c)
                add_to_queue(r, c + 1)
                add_to_queue(r, c - 1)

            counter += 1

                    
        