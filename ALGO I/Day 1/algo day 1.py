# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n ==1:
            return 1
        else:
            beg = 1
            end = n
            lastBad = -1
            while beg <= end:
                mid = (beg + end) //2
                
                if isBadVersion(mid) == True:
                    lastBad = mid
                    end = mid-1
                else:
                    beg = mid + 1
            return lastBad
 