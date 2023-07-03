class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        if len(cookies) == k:
            return max(cookies)
        
        self.result = 100000000
        childs = [0] * k
        
        def DFS(cookies , index , childs , max_value):
            if index >= len(cookies):
                self.result = min(self.result , max_value)
                return
            for child_no in range(len(childs)):
                childs[child_no] += cookies[index]
                current_max_value = max(max_value , childs[child_no])
                DFS(cookies , index + 1, childs , current_max_value)
                childs[child_no] -= cookies[index]
        
        DFS(cookies , 0 , childs , 0)
        return self.result