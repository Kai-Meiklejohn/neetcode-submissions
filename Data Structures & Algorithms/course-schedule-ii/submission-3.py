class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        result = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            cycle.discard(crs)
            visited.add(crs)
            result.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result
