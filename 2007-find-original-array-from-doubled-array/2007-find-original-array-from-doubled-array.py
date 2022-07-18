class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed.sort()
        original =[]
        queue = []
        for i in changed:
            # print(original)
            # print(queue)
            if queue and i == queue[0]:
                queue.pop(0)
            else:
                queue.append(i*2)
                original.append(i)
        if len(original) != len(changed)/2 or queue != []:
            print(original)
            return []
        else:
            return original