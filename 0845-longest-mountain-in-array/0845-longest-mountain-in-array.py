class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        
        peek = 1
        longest = 0
        while peek < n - 1:
                
                if arr[peek] > arr[peek - 1] and arr[peek + 1] < arr[peek]:
                    count = 1
                    point = peek
                    while point > 0 and arr[point - 1] < arr[point]:
                        count += 1
                        point -= 1
                    
                    while peek < n -1 and arr[peek] > arr[peek + 1]:
                        count += 1
                        peek += 1
                    longest = max(longest, count)
                else:
                    peek += 1
        return longest
                        
                