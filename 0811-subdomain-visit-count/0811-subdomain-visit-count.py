class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        hashtable = defaultdict()
        
        for domain in cpdomains:
            rep , dom = domain.split(' ')
            dom = dom.split('.')
            
            if len(dom) == 2:
                d1 = ".".join(dom)
                d2 = dom[1]
                
                hashtable[d1] = hashtable.get(d1,0) + int(rep)
                hashtable[d2] = hashtable.get(d2,0) + int(rep)

            else:
                d1 = ".".join(dom[1:])
                d2 = ".".join(dom)
                d3 = dom[2]
                
                hashtable[d1] = hashtable.get(d1,0) + int(rep)
                hashtable[d2] = hashtable.get(d2,0) + int(rep)
                hashtable[d3] = hashtable.get(d3,0) + int(rep)
        
        ans = []
        for key, val in hashtable.items():
            ans.append(" ".join([str(val),key]))
        
        return ans
            