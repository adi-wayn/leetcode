import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cycles = 0
        freq = {} # task -> frequency
        queue = [] # [(frequency, ready_time)]

        for t in tasks:
            freq[t] = freq.get(t, 0) - 1

        maxHeap = list(freq.values())
        heapq.heapify(maxHeap)

        while maxHeap or queue:
            cycles += 1
            if queue and queue[0][1] == cycles:
                heapq.heappush(maxHeap, queue.pop(0)[0])
            
            if maxHeap:
                curTask = heapq.heappop(maxHeap)
            
                curTask += 1
                if curTask == 0:
                    continue

                queue.append((curTask, cycles + n + 1))
            
        return cycles