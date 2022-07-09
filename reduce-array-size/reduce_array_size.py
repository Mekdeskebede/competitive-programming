class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        frequency = defaultdict(int)
        n = len(arr)
        check = len(arr)
        count = 0

        for i in arr:
            frequency[i] +=1 
        frequencies = list(frequency.values())

        while check > n/2:

            
            max_frq = max(frequencies)
            frequencies.pop(frequencies.index(max_frq))

            count += 1
            check -= max_frq
            
        return count