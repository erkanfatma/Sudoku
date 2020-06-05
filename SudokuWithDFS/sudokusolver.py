"""
Sudoku with Depth First Search Algorithm
"""

import numpy as np
import copy as cp
import time
from termcolor import colored

class sudoku_solution(object):
    def __init__(self, sd):
        row = []
        col = []
        for i in range(9):
            for j in range(9):
                if sd[i][j] == 0:
                    row.append(i)
                    col.append(j)
        #first, we need to find all empty positions and mark them
        self.row = row
        self.col = col
        self.sd = sd


    def order(self):# this function just help you accelerate your speed, just shrink the search tree, you can ignore it.
        small_sudoku = [[],[],[], [],[],[], [],[],[]]
        for n in range(9):
            for m in range(9):
                small_n = (m//3) + (n//3)*3
                small_m = (m%3) + (n%3)*3
                small_sudoku[n].append(self.sd[small_n][small_m])
        #seond, we find 9 small sudokus to constrain available elements
        sdt = np.transpose(self.sd) # sd transpose
        weight_value = []
        for i in range(len(self.row)):
            count = 0
            for val in [1,2,3,4,5,6,7,8,9]:
                if (val not in self.sd[self.row[i]]) and (val not in sdt[self.col[i]]) and (val not in small_sudoku[(self.row[i]//3)*3 + (self.col[i]//3)]):
                    count += 1
            weight_value.append(count)
        order_row = []
        order_col = []
        for i in range(min(weight_value),max(weight_value)+1):
            for n in range(len(self.row)):
                if weight_value[n] == i:
                    order_row.append(self.row[n])
                    order_col.append(self.col[n])
        self.row = order_row
        self.col = order_col

    def available(self, i):# find the available digits for the current empty box.
        small_sudoku = [[],[],[], [],[],[], [],[],[]]
        for n in range(9):
            for m in range(9):
                small_n = (m//3) + (n//3)*3
                small_m = (m%3) + (n%3)*3
                small_sudoku[n].append(self.sd[small_n][small_m])
        #seond, we find 9 small sudokus to constrain available elements
        sdt = np.transpose(self.sd) # sd transpose
        available = []
        for val in [1,2,3,4,5,6,7,8,9]:
            if (val not in self.sd[self.row[i]]) and (val not in sdt[self.col[i]]) and (val not in small_sudoku[(self.row[i]//3)*3 + (self.col[i]//3)]):
                available.append(val)
        #print(i)
        #print(self.sd[self.row[i]])
        #print(sdt[self.col[i]])
        #print(small_sudoku[(self.row[i]//3)*3 + (self.col[i]//3)])
        #print(available)
        return available
        # judge if elements are qualified before taking


    def fill(self, list):# fill the current state to check if it's right.
        count = 0
        for i in range(len(list)):
            if list[i] != 0:
                count += 1
            self.sd[self.row[i]][self.col[i]] = list[i]
        #print(count)
        #print(list)
        #print(self.sd)
        return count # how many elements it fill in

    def depth_search(self):
        self.order()#you know you can ignore this functioin,it's all right to delete this.
        visited = 0
        L = []# L is to store states.
        space = 0

        exist = [0 for i in range(len(self.row))]# it will help us reset soduku back to original state if it's already calculated
        L.append(exist)
        while True:
            if space < len(L):
                space = len(L)
            if len(L) != 0:
                exist = L[-1]
                i = self.fill(exist)
                if i == len(self.row):
                    break
            else:
                print("This sudoku is wrong.")
                break
            # judge the current situation
            choice = self.available(i)
            # find available value for the next
            L.pop()
            visited += 1
            if len(choice) == 0:
                #print(L)
                continue

            for val in choice:
                exist[i] = val
                #print(exist)
                L.append(cp.deepcopy(exist))
        return self.sd, visited, space
#visited is a value to display how many nodes we've visited during the whole process
#space is a value to display how many memory we used but keep in mind, here the unit is a sudoku


# DISPLAYS THE SOLVED SUDOKU IN THE GRID FORMAT
def display(board):
    for r in range(9):
        if r in [0, 3, 6]:
            print("-------------------------------------------")
        for c in range(9):
            if c in [3, 6]:
                print(' | ', board[r][c], ' ', end=' ')
            else:
                print(board[r][c], ' ', end=' ')
        print(end='\n')


sd_diff = [[4,0,0, 0,0,0, 0,7,5],
           [0,3,0, 0,0,0, 1,6,0],
           [0,0,0, 0,0,2, 0,0,0],
           [0,0,3, 7,0,0, 8,0,0],
           [0,0,0, 1,0,8, 0,2,0],
           [0,0,0, 0,3,0, 0,0,0],
           [0,0,0, 9,0,0, 7,1,4],
           [1,0,0, 0,0,6, 0,9,0],
           [0,4,9, 0,0,3, 0,0,0]]

if __name__ == '__main__':
    print(colored("Sudoku that will be solved", "blue"))
    display(sd_diff)
    print("-------------------------------------------")
    print("\n")

#below is what we trying to test the speed of depth first search algorithm
    print(colored("Congratulations! Sudoku solved", "blue"))
    sudoku = sudoku_solution(sd_diff)
    begin = time.time()
    result, visited, space = sudoku.depth_search()
    end = time.time()

    display(result)
    print("-------------------------------------------")

    print(colored("\nThe algorithm took {0:0.1f} seconds to find solution"
                  .format(end - begin), "blue"))

    print("Visited", colored( visited, "blue"))
    print("Space",colored( space,"blue"))
