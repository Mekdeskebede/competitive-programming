class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i, task in enumerate(tasks):
            tasks[i] = task + [i]
       
        heapq.heapify(tasks)
        ans, time, buf_queue = [], 0, []
        
        while tasks or buf_queue:
            
            while tasks and tasks[0][0] <= time or not buf_queue:
                
                st, proc_time, ind = heapq.heappop(tasks)
                heapq.heappush(buf_queue, (proc_time, ind, st))
                
            proc_time, idx, start_time = heapq.heappop(buf_queue)
            ans.append(idx)
            
            if time < start_time:
                time += start_time - time
                
            time += proc_time
        return ans