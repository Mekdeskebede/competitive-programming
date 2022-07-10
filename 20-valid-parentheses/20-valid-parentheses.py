class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        tag_dict= defaultdict(str)
        tag_dict["{"]= "}"
        tag_dict["["]= "]"
        tag_dict["("]= ")"

        for i in s:
            if len(stack)!=0:
                if tag_dict[stack[-1]]== i:
                    # print(stack.pop())
                    stack.pop()
                else:
                    stack.append(i)
            else:

                stack.append(i)
        if len(stack)==0:
            return True
        else:

            return False
        
        