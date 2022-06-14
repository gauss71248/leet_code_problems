class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def flatten(l):
            return [x for xs in l for x in xs]
        def convert_to_small_sudoku(s,i,j):
           return flatten([[s[3*i+k][3*j+l] for k in range(0,3)] for l in range(0,3)])
        def convert_to_small_sudokus(s):
            return flatten([[convert_to_small_sudoku(s,i,j) for i in range(0,3)] for j in range(0,3)])
        def check_line(l):
            l_without_dot = list(filter(lambda x: x != ".", l))
            return len(set(l_without_dot)) == len(l_without_dot)
        def check_board(s, b):
            if len(s)==0:
                return b
            else:
                return check_board(s[1:],check_line(s[0]) and b)
        return check_board(board, True) and check_board(convert_to_small_sudokus(board), True)
            