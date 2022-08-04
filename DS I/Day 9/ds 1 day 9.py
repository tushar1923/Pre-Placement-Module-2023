class Solution:
    def isValid(self, s: str) -> bool:
        g=[]
        n=')}]'
        k='({['
        h=[]
        for i in s:
            if i in k:
                g.append(i)
          # pushing into stack  
            if i in n:
                h.append(i)
                if len(g):
                    f=g.pop()
                    if i==n[0] and f == k[0] or i==n[1] and f == k[1] or i == n[2] and f==k[2]:
					#checking the condition valid pattern or not
                        h.pop()
                        continue
                        
                    else:
                        return False
        if len(g)==0 and len(h) == 0:
            return True
        else:
            return False