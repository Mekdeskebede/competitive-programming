from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))
adj_list = defaultdict(list)
for i in range(n):
    adj_list[i+1].append(arr[i])
    
# print(adj_list)
# color = [-1] * n
# curr = 0


class Solution:

    WHITE = 0
    GRAY = 1
    BLACK = -1

    def canFinish(self, n, prerequisites):
        def dfs(i: int) -> bool:
            if color[i] == self.GRAY:
                return True
            if color[i] == self.BLACK:
                return False
            
            color[i] = self.GRAY
            for j in prerequisites[i]:
                if dfs(j):
                    return True

            color[i] = self.BLACK
            return False

        # graph = defaultdict(list)
        # for u, v in prerequisites:
        #     graph[u].append(v)

        color = [self.WHITE] * n
        return not any(map(dfs, range(n)))

s = Solution()
cycle = False
if s.canFinish(1,adj_list):
    print("YES")
else:
    print("NO")
# if cycle:
#     print("YES")
# else:
#     print("NO")




