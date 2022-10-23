class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        check = []
        arr.sort(reverse = True)
        for i in range(len(arr)):
            if check and arr[i] in check:
                return True
            check.append(arr[i] / 2)
            check.append(arr[i] * 2)
        return False