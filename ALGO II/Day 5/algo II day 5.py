class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        
        if n < m:
            return []
        
        window = {}
        pmap = {}
        
        for i in range(m):
            if p[i] not in pmap:
                pmap[p[i]] = 1
            else:
                pmap[p[i]] += 1
                
        ans = []
        
        # window initialization
        for i in range(0, m):
            if s[i] in window:
                window[s[i]] += 1
            else:
                window[s[i]] = 1
        
        if window == pmap:
            ans.append(0)
                
        for i in range(1, n-m+1):
            
            # window updation by reducing frequency of prev window element if present in smap else deleting 
            # and adding/increasing frequency of next element (nxt)
            
            prev = s[i-1]
            if prev in window:
                window[prev] -= 1
                if window[prev] == 0:
                    del window[prev]

            nxt = s[i+m-1]
            if nxt in window:
                window[nxt] += 1
            else:
                window[nxt] = 1

            if window == pmap:
                ans.append(i)
                    
        return ans
