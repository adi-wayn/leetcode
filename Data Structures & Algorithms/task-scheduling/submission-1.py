import heapq

class Solution: 
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        freq = {} # task -> frequency
        queue = deque() # [(frequency, ready_time)]

        for t in tasks:
            freq[t] = freq.get(t, 0) - 1

        maxHeap = list(freq.values())
        heapq.heapify(maxHeap)

        while maxHeap or queue:
            cycles += 1

            if not maxHeap:
                cycles = queue[0][1]
            
            else:
                curTask = heapq.heappop(maxHeap)
                curTask += 1
                if curTask:
                    queue.append((curTask, cycles + n))

            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return cycles