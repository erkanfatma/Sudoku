"""
Sudoku with Constraint satisfaction problems with Backtracking
"""

from termcolor import colored
from csp import *
import time

# Display the sudoku in the grid format on the screen
def display(puzzleboard):
    for r in range(9):
        if r in [0, 3, 6]:
            print("-------------------------------------------")
        for c in range(9):
            if c in [3, 6]:
                print(' | ', puzzleboard[r][c].value, ' ', end=' ')
            else:
                print(puzzleboard[r][c].value, ' ', end=' ')
        print(end='\n')


# returns a list of variables
def initialize():
    #initial sudoku
    sudoku_puzzle =  [[0, 0, 0, 1, 0, 0, 0, 7, 0],
                     [7, 3, 0, 0, 9, 0, 0, 0, 0],
                     [2, 0, 0, 0, 6, 4, 0, 3, 0],
                     [0, 0, 6, 0, 0, 1, 0, 4, 0],
                     [0, 0, 1, 3, 0, 0, 0, 2, 6],
                     [0, 0, 0, 2, 0, 0, 8, 0, 0],
                     [0, 6, 8, 4, 0, 0, 9, 0, 0],
                     [3, 0, 0, 9, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0]]


    for i in range(9):
        for j in range(9):
            #to create Variable set in CSP that is called Vars
            var = Vars(i, j, sudoku_puzzle[i][j])
            sudoku_puzzle[i][j] = var

    return sudoku_puzzle


# Returns True if checkvariable is valid input into puzzleboard
# Does NOT actually input checkvariable into puzzleboard
def controlinput(empty_var, checkvariable, puzzle):
    row_location = empty_var.row
    col_location = empty_var.col

    # check horizontally
    for c in range(len(puzzle[row_location])):
        if (c == col_location):
            continue
        if (puzzle[row_location][c].value == checkvariable):
            return False

    # check vertically
    for r in range(len(puzzle)):
        if (r == row_location):
            continue
        if (puzzle[r][col_location].value == checkvariable):
            return False

    # check box
    box_row = row_location / 3
    box_col = col_location / 3
    top_left_row = int(box_row) * 3
    top_left_col = int(box_col) * 3
    row_indecies_to_check = [top_left_row, top_left_row + 1, top_left_row + 2]
    col_indecies_to_check = [top_left_col, top_left_col + 1, top_left_col + 2]
    for r in row_indecies_to_check:
        for c in col_indecies_to_check:
            if (r == row_location and c == col_location):
                continue
            if (puzzle[r][c].value == checkvariable):
                return False

    return True


# Recursive Backtracking Solver
def BackTrackingSearch(csp):
    # check if assignment complete
    if csp.complete(csp.puzzleboard):
        # return assignment
        return True

    empty_var = csp.empty(csp.puzzleboard)

    if empty_var == None:
        return False

    # for each value in Order-Domain-Value(variable, assignment, csp) do
    for domain_var in empty_var.domain:
        valid = controlinput(empty_var, domain_var, csp.puzzleboard)
        # if value is consistent with assignment given Constraints[csp] then
        if valid:
            # add {variable = value} to assignment
            csp.puzzleboard[empty_var.row][empty_var.col].value = domain_var

            #Recursive-backtracking(assignment, csp)
            if BackTrackingSearch(csp):
                return True  # result
            ev = Vars(empty_var.row, empty_var.col, 0)
            csp.puzzleboard[empty_var.row][empty_var.col] = ev  # remove {variable = value} from assignment

    # Failure
    return False


def main():
    # create variables
    puzzleboard = initialize()
    display(puzzleboard)

    # create CPS instance
    csp = CSP(puzzleboard)

    starttime = time.time()

    # if solution exist then return true
    solution = BackTrackingSearch(csp)

    endtime = time.time()

    if solution == True:
        print(colored("Congratulations! Sudoku solved", "blue"))
        display(csp.puzzleboard)

        print(colored("\nThe algorithm took {0:0.4f} seconds to find solution"
                      .format(endtime - starttime), "blue"))

    else:
        print(colored("Sudoku provided has no solution", "blue"))
        print(colored("\nThe algorithm took {0:0.4f} seconds to find solution"
                      .format(endtime - starttime), "blue"))

if __name__ == "__main__":
    main()
