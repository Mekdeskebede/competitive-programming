class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s + " "
        sort = []
        str_arr = []
        temp = ""
        for i in s:
            # print(i)  
            if i == " ":
                str_arr.append(temp)
                temp = ""
                continue
            temp = temp + i
        print(str_arr)
        
        for i in range(len(str_arr)):
            sort.append("")
        print(sort)
        for i in str_arr:
            m = i[-1]
            sort[int(m)-1]= i[:len(i)-1]
        print(sort)

        return " ".join(sort)