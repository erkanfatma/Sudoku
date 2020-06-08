import bfs, time
from termcolor import colored

# Display the solution of  sudoku in the grid format
def displaytoscreen(board):
    for r in range(9):
        if r in [0, 3, 6]:
            print("-------------------------------------------")
        for c in range(9):
            if c in [3, 6]:
                print(' | ', board[r][c], ' ', end=' ')
            else:
                print(board[r][c], ' ', end=' ')
        print(end='\n')


if __name__ == '__main__':
    bfs.NotesNum = 0
    bfs.N = 9
    initState = [
        [0, 0, 0, 0, 4, 0, 6, 5, 0],
        [0, 8, 5, 0, 1, 0, 4, 0, 9],
        [9, 4, 6, 0, 0, 5, 0, 8, 0],
        [0, 3, 0, 9, 7, 0, 0, 1, 6],
        [8, 0, 7, 0, 5, 0, 9, 0, 4],
        [0, 1, 0, 4, 0, 0, 7, 2, 0],
        [0, 7, 8, 0, 9, 0, 3, 0, 2],
        [6, 0, 0, 0, 0, 7, 8, 4, 0],
        [4, 0, 2, 0, 8, 0, 0, 9, 0],
    ]

    print(colored("\nSudoku that will be solved", "blue"))
    displaytoscreen(initState)
    print("-------------------------------------------")
    print("\n")
    pro = bfs.Problem(initState)
    starttime = time.time()
    bfs.result = bfs.breadth_first_search(pro)
    endtime = time.time()

    if (bfs.result == None):
        print(colored("Sudoku can not be solved", "red"))
    else:
        print(colored("Congratulations! Sudoku solved", "blue"))

        displaytoscreen(bfs.result.state)
        print("-------------------------------------------")

    print(colored("\nThe algorithm took {0:0.3f} seconds to find solution"
                  .format(endtime - starttime), "blue"))

    print("The total child notes searched : ", colored(bfs.NotesNum, "green"))