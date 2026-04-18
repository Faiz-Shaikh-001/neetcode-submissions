class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col, val in enumerate(board[row]):
                if val == '.':
                    continue
                if not self.valid_in_row(val, row, board):
                    return False
                if not self.valid_in_col(val, col, board):
                    return False
                if not self.valid_in_box(val, row, col, board):
                    return False

        return True

    def valid_in_row(self, num: int, row: int, board: List[List[str]]) -> bool:
        if num in board[row] and board[row].count(num) > 1:
            return False
        return True
    
    def valid_in_col(self, num: int, col: int, board: List[List[str]]) -> bool:
        count = 0
        for i in range(9):
            if board[i][col] == num:
                count += 1
        if count > 1:
            return False
        return True
    
    def valid_in_box(self, num: int, row: int, col: int, board: List[List[str]]) -> bool:
        row_from = (row//3) * 3
        col_from = (col//3) * 3
        count = 0
        for i in range(row_from, row_from+3):
            for j in range(col_from, col_from+3):
                if board[i][j] == num:
                    count += 1
        if count > 1:
            return False
        return True