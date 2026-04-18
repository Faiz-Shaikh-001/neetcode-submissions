class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        if self.isValidRow(board, n) and self.isValidColumn(board, n) and self.isValidSquare(board, n):
            return True
        return False
    
    def isValidRow(self, board: List[List[str]], n: int) -> bool:
        for i in range(n):
            row = [board[i][x] for x in range(n) if board[i][x] != '.']
            if self.containsDuplicate(row):
                return False
        
        return True
            

    def isValidColumn(self, board: List[List[str]], n) -> bool:
        for i in range(n):
            column = [board[j][i] for j in range(n) if board[j][i] != '.']
            if self.containsDuplicate(column):
                return False
        
        return True
            

    def isValidSquare(self, board: List[List[str]], n) -> bool:
        for i in range(0, n, 3): # row 0, 3, 6
            for j in range(0, n, 3):
                idx = 0
                row = []
                while idx in range(3):
                    seg = board[i + idx][j:j + 3]
                    for x in seg:
                        if x != '.':
                            row.append(x)    
                    idx += 1
                if self.containsDuplicate(row):
                    return False
        return True
            
    
    def containsDuplicate(self, arr: List[int]):
        return len(set(arr)) != len(arr)