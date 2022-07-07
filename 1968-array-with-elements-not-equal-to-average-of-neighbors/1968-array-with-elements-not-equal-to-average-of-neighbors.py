class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(arr):
            if len(arr) > 1:
  
         # Finding the mid of the array
                mid = len(arr)//2

                # Dividing the array elements
                L = arr[:mid]

                # into 2 halves
                R = arr[mid:]

                # Sorting the first half
                mergeSort(L)

                # Sorting the second half
                mergeSort(R)

                i = j = k = 0

                # Copy data to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
            return arr

        sortedArr = mergeSort(nums)
        leftCounter = 0
        rightCounter = len(nums) - 1
        outPut = []

        while len(outPut) < len(nums):
            outPut.append(sortedArr[leftCounter])
            leftCounter += 1

            if leftCounter <= rightCounter:
                outPut.append(sortedArr[rightCounter])
                rightCounter -= 1
        return outPut
        