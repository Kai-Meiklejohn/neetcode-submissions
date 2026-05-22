class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        heap = []

        for i, task in enumerate(tasks):
            task.append(i)
        
        tasks.sort()

        res = []
        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            while i < n and tasks[i][0] <= time:
                enqueue, process, index = tasks[i]
                heapq.heappush(heap, (process, index))
                i += 1

            process, index = heapq.heappop(heap)
            time += process
            res.append(index)

        return res


