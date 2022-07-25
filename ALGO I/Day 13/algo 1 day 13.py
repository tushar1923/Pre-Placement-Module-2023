class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for m in range(32):
            if 2**m == n:
                return True
        
        return False
