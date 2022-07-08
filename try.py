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



def domino_pilling(n, m,a):
   
    square = n * m
    one_domino = a * a
    check_n=-1
    check_m= -1
    count = 0
    num_domino = square/one_domino
    if square% one_domino == 0:
        return square/ one_domino
    else:
        while check_n != 0:
            if n == a:
                check_n = 0
            elif n- a >0:
                n =n- a
                count += 1
            else:
                count += 1
                check_n = 0
        while check_m != 0:
            if m ==a:
                check_m = 0
            elif m- a >0:
                m =m- a
                count += 1
            else:
                count += 1
                check_m =0

        return count
    






