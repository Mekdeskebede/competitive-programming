class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        arr = []
        while x > 0:
            arr.append(x%10)
            x = x//10
        l = 0
        r = len(arr)-1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True
    