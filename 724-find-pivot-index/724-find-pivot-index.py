class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
#         for i in range(len(nums)):
#             if i == 0:
#                 if sum(nums[1:]) == 0:
#                     return 0
#                 else:
#                     continue
#             if i == len(nums) - 1:
#                 if sum(nums[:len(nums) -1]) == 0:
#                     return len(nums) -1
#                 else:
#                     continue
#             sum1 = sum(nums[:i])
#             sum2 = sum(nums[i+1:])
#             if sum1 == sum2:
#                 return i
#             else:
#                 continue
                
#         return -1

        sum1 = []
        sum2 = []
        for i in range(len(nums)):
            if  sum1:
                sum1.append(sum1[-1] + nums[i])
                sum2.append(sum2[-1] + nums[-i-1])
                
            else:
                sum1.append(nums[i])
                sum2.append(nums[-i-1])

        for i in range(len(nums)):
            if sum1[i] == sum2[-i-1]:
                return i
        return -1
        