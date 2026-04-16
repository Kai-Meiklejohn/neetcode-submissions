class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        from_pacific = set()
        from_atlantic = set()
        result = []

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if ((rows > row >= 0) and (cols > col >= 0) and
                    heights[r][c] <= heights[row][col]):
                    dfs(row, col, visited)

        for c in range(cols):
            dfs(0, c, from_pacific)
        for r in range(rows):
            dfs(r, 0, from_pacific)

        for c in range(cols):
            dfs(rows - 1, c, from_atlantic)
        for r in range(rows):
            dfs(r, cols - 1, from_atlantic)


        for ocean in from_pacific:
            if ocean in from_atlantic:
                result.append(ocean)

        return result
