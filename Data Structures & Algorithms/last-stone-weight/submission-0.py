
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use negative values to simulate a max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Pop the two heaviest stones
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0
