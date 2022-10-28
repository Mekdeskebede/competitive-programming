class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        p1 = 0
        p2 = 0
        n = len(ver1)
        m = len(ver2)
        while p1 < n or p2 < m:
            if p1 < n and p2 < m:
                if int(ver1[p1]) > int(ver2[p2]):
                    return 1
                elif int(ver1[p1]) < int(ver2[p2]):
                    return -1
                else:
                    p1 += 1
                    p2 += 1
            elif p1 >= n and p2 < m:
                if 0 < int(ver2[p2]):
                    return -1
                elif 0 > int(ver2[p2]):
                    return 1
                else:
                    p2 += 1
            elif p1 < n and p2 >= m:
                if 0 < int(ver1[p1]):
                    return 1
                elif 0 > int(ver1[p1]):
                    return -1
                else:
                    p1 += 1
        return 0