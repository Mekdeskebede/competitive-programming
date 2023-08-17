class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hashMap={}
        hashMap[" "] = " "
        asci=97
        
        for i in range(len(key)):
            if key[i] not in hashMap:
                hashMap[key[i]]=chr(asci)
                asci+=1

        ans=""   
        for i in range(len(message)):
                ans+=hashMap[message[i]]  
        return ans  