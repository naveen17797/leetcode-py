class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]
        for i in range(1, rowIndex + 1):
            temp = [1]
            for j in range(1,len(prev_row)):
                temp.append(prev_row[j-1] + prev_row[j])
            temp.append(1)
            prev_row = temp
        return prev_row