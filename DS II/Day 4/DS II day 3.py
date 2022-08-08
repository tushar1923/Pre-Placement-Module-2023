class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = []
        for i in range(rowIndex+1):
            res = []
            for j in range(i+1):
                if j == 0 or j == i:
                    res.append(1)
                else:
                    res.append(temp[i-1][j]+ temp[i-1][j-1])
            temp.append(res)
        return res
