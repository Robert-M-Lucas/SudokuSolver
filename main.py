import random
from typing import *
from solver import solve

saved_sudoku = open("sudoku2.txt", "r").read().replace("\n", "").replace(" ", "")
init_sudoku = saved_sudoku


def key(x):
    if x[1] is None:
        return 100
    else:
        return len(x[1])


def recursively_solve(sudoku, possible_values, depth=0):
    optimised_list = sorted(list(enumerate(possible_values)), key=key)
    # optimised_list = enumerate(possible_values)
    z = 0
    for i, p in optimised_list:
        """
        if depth < 4:
            print(z)
            z += 1
        """
        if p is not None:
            for p2 in p:
                new_sudoku = sudoku
                if len(sudoku) - 1 > i:
                    new_sudoku = new_sudoku[:i] + p2 + new_sudoku[i + 1:]
                else:
                    new_sudoku = new_sudoku[:i] + p2

                new_solved_sudoku, new_possible_values = solve(new_sudoku)
                if new_solved_sudoku is None: continue
                if "_" not in new_solved_sudoku: return new_solved_sudoku
                """
                    print("*****")
                    for x in range(9):
                        print(" ".join(sudoku[x * 9: x * 9 + 9]))
                    print()
                    for x in range(9):
                        print(" ".join(new_sudoku[x * 9: x * 9 + 9]))
                    print()
                    for x in range(9):
                        print(" ".join(new_solved_sudoku[x * 9: x * 9 + 9]))
                    print()
                """
                result = recursively_solve(new_solved_sudoku, new_possible_values, depth + 1)
                if result is None: continue
                if "_" not in result: return result


init_sudoku, init_possible_values = solve(init_sudoku)
if "_" in init_sudoku:
    solved_sudoku = recursively_solve(init_sudoku, init_possible_values)
else:
    print("Instant solve")
    solved_sudoku = init_sudoku

for x in range(9):
    print(" ".join(solved_sudoku[x * 9: x * 9 + 9]))
