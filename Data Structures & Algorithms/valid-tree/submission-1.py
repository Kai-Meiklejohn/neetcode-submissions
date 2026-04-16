class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        edgeMap = defaultdict(list)
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        def dfs(cur, prev):
            if cur in visited:
                return False

            visited.add(cur)

            for nxt in edgeMap[cur]:
                if nxt == prev:
                    continue
                if not dfs(nxt, cur):
                    return False

            return True

        return dfs(0, -1) and n == len(visited)

