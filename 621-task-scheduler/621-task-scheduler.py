class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n== 0:
            return len(tasks)
        
        frq = defaultdict(int)
        for i in tasks:
            frq[i] += 1
        print(frq)
        
        frq_values = list(frq.values())
        frq_values.sort()
        frq_values.reverse()
        count = 0
        
        while len(frq_values) > count and frq_values[count] ==frq_values[0]:
            count += 1
            
        task = (frq_values[0] -1) * ( n+1 ) + count
        if task > len(tasks):
            return task
        else:
            return len(tasks)
        