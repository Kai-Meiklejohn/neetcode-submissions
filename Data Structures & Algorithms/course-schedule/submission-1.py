class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = defaultdict(list)

        for src, pre in prerequisites:
            preMap[src].append(pre)

        visited = set()

        def dfs(src):
            if src in visited:
                return False
            if preMap[src] == []:
                return True
            
            visited.add(src)

            for pre in preMap[src]:
                if not dfs(pre):
                    return False

            visited.discard(src)
            preMap[src] = []
            return True
            
        for src in range(numCourses):
            if not dfs(src):
                return False

        return True

        