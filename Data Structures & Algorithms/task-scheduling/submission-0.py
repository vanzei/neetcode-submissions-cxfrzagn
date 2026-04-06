class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        h = []
        for lt, ct in counter.items():
            h.append(-ct)
        
        heapq.heapify(h)
        time = 0

        q = deque()
        while h or q :
            time +=1

            if h:
                cnt = 1 + heapq.heappop(h)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(h,q.popleft()[0])

        return time

        
