"""
Sudoku with Constraint satisfaction problems with Backtracking
"""

from termcolor import colored
from csp import *
import time

# Display the solution of sudoku in the grid format
def display(board):
    for r in range(9):
        if r in [0, 3, 6]:
            print("-------------------------------------------")
        for c in range(9):
            if c in [3, 6]:
                print(' | ', board[r][c].value, ' ', end=' ')
            else:
                print(board[r][c].value, ' ', end=' ')
        print(end='\n')


# returns a list of initialized variables
def init_variables():
    #çözülmek istenen sudoku tanımı
    lists_var = [[0, 7, 0, 0, 4, 2, 0, 0, 0],
                 [0, 0, 0, 0, 0, 8, 6, 1, 0],
                 [3, 9, 0, 0, 0, 0, 0, 0, 7],
                 [0, 0, 0, 0, 0, 4, 0, 0, 9],
                 [0, 0, 3, 0, 0, 0, 7, 0, 0],
                 [5, 0, 0, 1, 0, 0, 0, 0, 0],
                 [8, 0, 0, 0, 0, 0, 0, 7, 6],
                 [0, 5, 4, 8, 0, 0, 0, 0, 0],
                 [0, 0, 0, 6, 1, 0, 0, 5, 0]]

    for i in range(9):
        for j in range(9):
            #to create Variable set in CSP
            var = Variable(i, j, lists_var[i][j])
            lists_var[i][j] = var

    return lists_var


# Returns True if variable_to_check is valid input into board
# Checks horizontal, vertical, and box
# Does NOT actually input variable_to_check into board
# This still needs to be tested
def is_valid_input(empty_var, variable_to_check, board):
    row_loc = empty_var.row
    col_loc = empty_var.col

    # check horizontally
    for c in range(len(board[row_loc])):
        if (c == col_loc):
            continue
        if (board[row_loc][c].value == variable_to_check):
            return False

    # check vertically
    for r in range(len(board)):
        if (r == row_loc):
            continue
        if (board[r][col_loc].value == variable_to_check):
            return False

    # check box
    box_row = row_loc / 3
    box_col = col_loc / 3
    top_left_row = int(box_row) * 3
    top_left_col = int(box_col) * 3
    row_indecies_to_check = [top_left_row, top_left_row + 1, top_left_row + 2]
    col_indecies_to_check = [top_left_col, top_left_col + 1, top_left_col + 2]
    for r in row_indecies_to_check:
        for c in col_indecies_to_check:
            if (r == row_loc and c == col_loc):
                continue
            if (board[r][c].value == variable_to_check):
                return False

    return True


# Recursive Backtracking Solver
def Back_Tracking_Search(csp):
    if csp.complete(csp.board):  # if assignment is complete then
        return True  # return assignment

    empty_var = csp.find_empty(csp.board)

    if empty_var == None:
        return False

    for domain_var in empty_var.domain:  # for each value in Order-Domain-Value(variable, assignment, csp) do
        valid = is_valid_input(empty_var, domain_var, csp.board)
        if valid:  # if value is consistent with assignment given Constraints[csp] then
            csp.board[empty_var.row][empty_var.col].value = domain_var  # add {variable = value} to assignment

            # result = Recursive-backtracking(assignment, csp) / if result is not failure then
            if Back_Tracking_Search(csp):
                return True  # return result
            ev = Variable(empty_var.row, empty_var.col, 0)
            csp.board[empty_var.row][empty_var.col] = ev  # remove {variable = value} from assignment

    return False  # return FAILURE


def main():
    # create a 2D lists of variables
    board = init_variables()
    display(board)

    # create CPS instance to represent the board
    csp = CSP(board)

    # start timer
    starttime = time.time()

    # solution is boolean value. True when there's a solution. False otherwise
    solution = Back_Tracking_Search(csp)

    # stop timer
    endtime = time.time()

    if solution == True:
        print(colored("Congratulations! Sudoku solved", "blue"))
        display(csp.board)

        print(colored("\nThe algorithm took {0:0.1f} seconds to find solution"
                      .format(endtime - starttime), "blue"))

    else:
        print(colored("Sudoku provided has no solution", "blue"))
        print(colored("\nThe algorithm took {0:0.1f} seconds to find solution"
                      .format(endtime - starttime), "blue"))


if __name__ == "__main__":
    main()
