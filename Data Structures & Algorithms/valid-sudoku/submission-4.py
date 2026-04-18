class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':  
                    continue
                
                box_index = (row // 3) * 3 + (col // 3)

                
                if val in row_set[row] or val in col_set[col] or val in box_set[box_index]:
                    return False

                row_set[row].add(val)
                col_set[col].add(val)
                box_set[box_index].add(val)
        return True
