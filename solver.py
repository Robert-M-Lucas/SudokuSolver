def solve(sudoku):
    possible_values = [[str(i) for i in range(1, 10)] for _ in range(81)]

    for i, char in enumerate(sudoku):
        if char != "_":
            possible_values[i] = None

    # Algorithmic approach
    change = True
    while change:
        change = False

        for row in range(9):
            values_in_row = sudoku[row * 9:row * 9 + 9]
            for possible in range(9):
                index = row * 9 + possible
                if possible_values[index] is None: continue
                for p in possible_values[index].copy():
                    if p in values_in_row:
                        possible_values[index].remove(p)

        for column in range(9):
            values_in_column = "".join([sudoku[i * 9 + column] for i in range(9)])

            for possible in range(9):
                index = possible * 9 + column
                if possible_values[index] is None: continue
                for p in possible_values[index].copy():
                    if p in values_in_column:
                        possible_values[index].remove(p)

        for cellx in range(3):
            for celly in range(3):
                values_in_cell = ""
                x, y = celly * 3, cellx * 3
                for xoffset in range(3):
                    for yoffset in range(3):
                        values_in_cell += sudoku[(y + yoffset) * 9 + (x + xoffset)]

                for xoffset in range(3):
                    for yoffset in range(3):
                        index = (y + yoffset) * 9 + (x + xoffset)
                        if possible_values[index] is None: continue
                        for p in possible_values[index].copy():
                            if p in values_in_cell:
                                possible_values[index].remove(p)

        for i, possibilities in enumerate(possible_values.copy()):
            if possibilities is None: continue
            if len(possibilities) == 1:
                if len(sudoku) - 1 > i:
                    sudoku = sudoku[:i] + possibilities[0] + sudoku[i + 1:]
                else:
                    sudoku = sudoku[:i] + possibilities[0]
                possible_values[i] = None
                change = True
                break
            elif len(possibilities) == 0:
                return None, None

    return sudoku, possible_values
