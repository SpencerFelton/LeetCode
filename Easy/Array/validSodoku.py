class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValidBox(box):
            for keys in box:
                if box[keys] > 1 and keys != ".":
                    return False
        row = 0
        column = 0
        square_dicts = [{},{},{},{},{},{},{},{},{}]
        for x in range(0, 9):
            row_dict = {}
            col_dict = {}

            for y in range(0,9): # row check
                if board[x][y] not in row_dict:
                    row_dict[board[x][y]] = 1
                else:
                    row_dict[board[x][y]] += 1

            for z in range(0, 9): # column check
                if board[z][x] not in col_dict:
                    col_dict[board[z][x]] = 1
                else:
                    col_dict[board[z][x]] += 1

            for i in range(0, 9): # 3x3 square check
                if board[x][i] not in square_dicts[(x//3)*3 + i//3]:
                    square_dicts[(x//3)*3 + i//3][board[x][i]] = 1
                else:
                    square_dicts[(x//3)*3 + i//3][board[x][i]] += 1

            if(isValidBox(row_dict) == False):
                return False
            if(isValidBox(col_dict) == False):
                return False

        for dicts in square_dicts:
            if(isValidBox(dicts) == False):
                return False
        return True
