def find_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None,None
def isValid(puzzle,guess,row,col):
    row_pz = puzzle[row]
    if guess in row_px:
        return False
    col_pz = [puzzle[i][col] for i in range(9)]
    if guess in col_pz:
        return False
    row_s,col_s = (row//3)*3,(col//3)*3
    for r in range(row_s,row_s+3):
        for c in range(col_s,col_s+3):
            if puzzle[r][c] == guess:
                return False
    return True
def solve(puzzle):
    row,col = find_empty(puzzle)
    if row == None:
        return True
    for i in range(1,10):
        if isValid(puzzle,i,row,col):
            puzzle[row][col] = i
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col]=-1
    return False
    
    