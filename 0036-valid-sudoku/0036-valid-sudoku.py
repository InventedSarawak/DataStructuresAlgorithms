class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            temp_set_horizontal = set()
            temp_set_vertical = set()
            temp_set_sub_grid = set()
            count_empty_horizontal = count_empty_vertical = count_empty_sub_grid = 0

            for j in range(9):
                if board[i][j] == '.':
                    count_empty_horizontal += 1
                else:
                    temp_set_horizontal.add(board[i][j])
                if board[j][i] == '.':
                    count_empty_vertical += 1
                else:
                    temp_set_vertical.add(board[j][i])
                if board[3 * (i // 3) + (j // 3)][3 * (i % 3) + (j % 3)] == '.':
                    count_empty_sub_grid += 1
                else:
                    temp_set_sub_grid.add(board[3 * (i // 3) + (j // 3)][3 * (i % 3) + (j % 3)])
            
            if count_empty_horizontal + len(temp_set_horizontal) != 9 or count_empty_vertical + len(temp_set_vertical) != 9 or count_empty_sub_grid + len(temp_set_sub_grid) != 9:
                return False
        return True
                