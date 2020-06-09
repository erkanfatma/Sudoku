"""
Sudoku with Constraint satisfaction problems with Backtracking
"""

class CSP:
    def __init__(self, puzzleboard):
        self.puzzleboard = puzzleboard

    # finds empty variable in the puzzleboard
    def empty(self, puzzleboard):
        for row in puzzleboard:
            for variable in row:
                if variable.value == 0:
                    return variable

    # find if puzzleboard solved or not
    def complete(self, puzzleboard):
        for i in range(9):
            for j in range(9):
                if puzzleboard[i][j].value == 0:
                    return False

                if self.complete_helper(puzzleboard, i, j) == False:
                    return False

        return True

    # evaluate completeness of a puzzleboard
    def complete_helper(self, puzzleboard, row, col):
        if len(puzzleboard) == 0:
            return False

        value = puzzleboard[row][col].value

        # check vertically
        for r in range(len(puzzleboard)):
            if (r == row):
                continue
            if (puzzleboard[r][col].value == value):
                return False

        # check horizontally
        for c in range(len(puzzleboard[row])):
            if (c == col):
                continue
            if (puzzleboard[row][c].value == value):
                return False

        # check 3x3 box
        box_row = row / 3
        box_col = col / 3
        top_left_row = int(box_row) * 3
        top_left_col = int(box_col) * 3
        row_indecies_to_check = [top_left_row, top_left_row + 1, top_left_row + 2]
        col_indecies_to_check = [top_left_col, top_left_col + 1, top_left_col + 2]
        for r in row_indecies_to_check:
            for c in col_indecies_to_check:
                if (r == row and c == col):
                    continue
                if (puzzleboard[r][c].value == value):
                    return False

        return True

# to define empty cells and which numbers can be chosen for selected empty cell
class Vars:
    def __init__(self, row, column, value=0):
        self.value = value
        self.row = row
        self.col = column
        self.domain = self.definedomain(value)

    # initializes domain of the variable
    def definedomain(self, value):
        # to find available numbers of empty cell
        domain = []
        for i in range(1, 10):
            #to evaluate domains if value can get these numbers
            if i != value:
                domain.append(i)

        return domain
