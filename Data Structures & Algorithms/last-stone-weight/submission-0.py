class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if x < y:
                new_num = y - x
                heapq.heappush_max(stones, new_num)

        return stones[0] if len(stones) == 1 else 0
                


        