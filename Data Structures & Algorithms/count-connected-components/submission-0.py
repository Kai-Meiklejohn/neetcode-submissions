class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        count = 0
        visited = set()
        adjMap = defaultdict(list)
        for a, b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)

        def dfs(cur):
            if cur in visited:
                return 

            visited.add(cur)

            for nxt in adjMap[cur]:
                dfs(nxt)

        for cur in range(n):
            if cur not in visited:
                dfs(cur)
                count += 1
            
        return count