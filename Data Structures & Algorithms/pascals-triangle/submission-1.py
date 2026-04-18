class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def get_row(n):
            row = [1]
            for i in range(1, n+1):
                row.append(int(round(row[i-1] * ((n + 1 - i) / i))))
            
            return row
        
        rows = []
        for i in range(numRows):
            rows.append(get_row(i))
        
        return rows