class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum = 0
        for num in nums:
            if num%2 == 0:
                even_sum += num
        print(even_sum)
        ans = []     
        for val,index in queries:
            if nums[index]%2 == 0:
                if val % 2 == 0:
                    even_sum += val
                else:
                    even_sum += - nums[index]
            else:
                if val % 2 != 0:
                    even_sum += + val + nums[index]
            ans.append(even_sum)
            nums[index] += val
        
        return ans