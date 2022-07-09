from audioop import reverse
from collections import defaultdict
import re
from tabnanny import check
from numpy import sort


# def merge(intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """

        # merged = []

        # for i in range(0,len(intervals),2):

        #     if intervals[i][1] > intervals[i+1][0]:
        #         merged.append([intervals[i][0],intervals[i+1][1]])

        #     else:
        #         merged.append([intervals[i][0],intervals[i][1]])
        #         merged.append([intervals[i+1][0],intervals[i+1][1]])
                 
        # return merged

#         intervals = sorted(intervals)
        
#         if len(intervals)>1:
#             mergedlist = []
#             mergedlist.append(intervals[0])
#             for i in range(1,len(intervals)):
#                 if mergedlist[-1][1] < intervals[i][0]:
#                     mergedlist.append(intervals[i])
#                 else:      
#                     mergedlist[-1][1]=max(intervals[i][1],mergedlist[-1][1])
#                 print(mergedlist)
#             return mergedlist
#         else:
#             return intervals
# print(merge([[1,3],[2,6],[8,10],[15,18]]))

# for i in range(0,4,2):
#     print(i)



# maxi = []
# for i in l:
    
#     while i >= 10: 
#         i = i // 10
#     maxi.append(i)

#     print(i)
# for i in maxi:
    
# print(sort(maxi))

# def rearrangeArray(nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         for i in range(1,len(nums)-1):
#             if (nums[i-1] + nums[i+1]) / 2 == nums[i]:
#                 for j in nums[i:]:
    
#                     if (nums[i-1] + j) / 2 != nums[i]:
                        
#                         nums[i+1],nums[nums.index(j)] = nums[nums.index(j)],nums[i+1]
#                         break
#         return nums
    
    
# print(rearrangeArray([3,2,1]))    






# def findOriginalArray(changed):
#         """
#         :type changed: List[int]
#         :rtype: List[int]
#         """
#         original =[]
#         for i in changed:
#             original.append(i)
#         for i in sort(changed):
#             for j in sort(changed):
                
#                 if changed.index(i) != changed.index(j) and j == 2*i:
                    
                    
#                     original.pop(original.index(j))
#                     # print(original.index(j))
#                     break
#                 else:
#                     continue
#         print(changed)
#         print(original)
#         if len(original) == len(changed)/2:
            
#             return original
#         else:
#             return []

# print(findOriginalArray([0,3,2,4,6,0]))


def sorting(a):
    # Write your code here
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                
            else:
                continue
    return a

def minSetSize(arr):
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

        print(frequencies)
        count += 1
        check -= max_frq
        print(count)
        print(check)

    return count

print(minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))



# frequency = defaultdict(int)
# n = len([3,3,3,3,5,5,5,2,2,7])

# for i in [3,3,3,3,5,5,5,2,2,7]:
#     frequency[i] +=1 
# frequencies = list(frequency.values())
# print(frequencies)
# count = 0
# while count > n/2:
#     # for i in frequency:
#     # max_frq = max(frequency.values())
#     # [keys for keys, value in frequency.items() if value == max_frq frequency[]]
#     frequencies = list(frequency.values())
#     max_frq = max(frequencies)
#     frequencies.pop(frequencies.index(max_frq))

#     count += max_frq
# print(count)



   






      


