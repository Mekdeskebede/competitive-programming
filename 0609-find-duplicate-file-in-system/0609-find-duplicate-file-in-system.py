class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        hash_map = defaultdict(list)
        for path in paths:
            
            path_list = path.split(" ")
            n = len(path_list)
            
            for i in range(1,n):
                idx = path_list[i].index("(")
                hash_map[path_list[i][idx+1:-1]].append(f"{path_list[0]}/{path_list[i][:idx]}")
        ans = []
        for key, val in hash_map.items():
            if len(val) >1:
                ans.append(val)
                
        return ans
            
        