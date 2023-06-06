class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        self.res = 0
        def countPairs(left_arr, right_arr):
            l = 0
            r = 0
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] > 2 * right_arr[r]:
                    self.res += len(left_arr) - l
                    r += 1
                else:
                    l += 1

        def merge(left_arr, right_arr):
            # print(left_arr, right_arr)
            countPairs(left_arr, right_arr)
            new = []
            left = 0
            right = 0

            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] < right_arr[right]:
                    new.append(left_arr[left])
                    left += 1
                else:
                    new.append(right_arr[right])
                    right += 1

            new.extend(right_arr[right:])
            new.extend(left_arr[left:])
            return new

        def mergedSort(left,right,arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergedSort(left, mid, arr)
            right_half = mergedSort(mid + 1, right, arr)

            return merge(left_half,right_half)
        mergedSort(0,len(nums)-1,nums)
        return self.res