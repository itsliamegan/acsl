from typing import Optional, List, Dict


class Piece:
    A = "A"
    B = "B"
    C = "C"

    @classmethod
    def get_next_piece(cls, piece: str) -> str:
        if piece == cls.A:
            return cls.B

        elif piece == cls.B:
            return cls.C

        elif piece == cls.C:
            return cls.A


class Cell:
    BLOCKED = "■"
    CIRCLE = "●"

    def __init__(self, number: int, content: Optional[str] = None):
        self.number = number
        self.content = content

    def __repr__(self):
        if self.content:
            return self.content

        else:
            return str(self.number)


class Grid:
    def __init__(self, rows: int, cols: int, *blocked_numbers: List[int]):
        self.cells = []
        number = 0

        for row in range(rows):
            self.cells.append([])

            for _ in range(cols):
                number += 1
                cell = Cell(number)

                if number in blocked_numbers:
                    cell.content = Cell.BLOCKED

                self.cells[row].append(cell)

    def __repr__(self):
        grid = ""
        longest_character_length = 0

        for row in self.cells:
            for cell in row:
                if len(str(cell)) > longest_character_length:
                    longest_character_length = len(str(cell))

        for row in self.cells:
            grid += "\n"
            for cell in row:
                grid += str(cell).ljust(longest_character_length + 1, " ")

        return grid

    def get_position_of_number(self, number: int) -> Optional[Dict[str, int]]:
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                if self.cells[row][col].number == number:
                    return {"row": row, "col": col}

        return None

    def get_cell_at_number(self, number: int) -> Optional[Cell]:
        position = self.get_position_of_number(number)

        if position is None:
            return None

        row = position["row"]
        col = position["col"]

        return self.cells[row][col]

    # This method is really ugly, but I needed to do it quickly and I'll probably
    # never touch it again, so it works
    def find_path(self, starting_number: int) -> str:
        starting_position = self.get_position_of_number(starting_number)
        row = starting_position["row"]
        col = starting_position["col"]
        is_left_to_right = col == 0
        path = ""
        current_piece = Piece.A
        solved = False

        while not solved:
            try:
                if is_left_to_right:
                    if col >= len(self.cells[0]):
                        solved = True
                        break

                    if current_piece == Piece.A:
                        if col == 0:
                            can_place = (
                                self.cells[row][col].content is None and
                                self.cells[row][col + 1].content is None and
                                self.cells[row][col + 2].content is None
                            )
                        else:
                            can_place = (
                                self.cells[row][col - 1].content == Cell.CIRCLE and
                                self.cells[row][col].content is None and
                                self.cells[row][col + 1].content is None and
                                self.cells[row][col + 2].content is None
                            )

                        if can_place:
                            self.cells[row][col].content = Cell.CIRCLE
                            self.cells[row][col + 1].content = Piece.A
                            self.cells[row][col + 2].content = Cell.CIRCLE
                            path += Piece.A
                            col += 3

                        else:
                            current_piece = Piece.get_next_piece(current_piece)
                            continue

                    elif current_piece == Piece.B:
                        if col == 0:
                            can_place = False

                        else:
                            can_place = (
                                self.cells[row][col - 1].content == Cell.CIRCLE and
                                self.cells[row][col].content is None and
                                self.cells[row + 1][col].content is None and
                                self.cells[row + 1][col + 1].content is None
                            )

                        if can_place:
                            self.cells[row][col].content = Cell.CIRCLE
                            self.cells[row + 1][col].content = Piece.B
                            self.cells[row + 1][col + 1].content = Cell.CIRCLE
                            path += Piece.B
                            row += 1
                            col += 2

                        else:
                            current_piece = Piece.get_next_piece(current_piece)
                            continue

                    elif current_piece == Piece.C:
                        if col == 0:
                            can_place = (
                                self.cells[row][col].content is None and
                                self.cells[row][col + 1].content is None and
                                self.cells[row + 1][col + 1].content is None and
                                self.cells[row + 2][col + 1].content is None
                            )

                        else:
                            can_place = (
                                self.cells[row][col - 1].content == Cell.CIRCLE and
                                self.cells[row][col].content is None and
                                self.cells[row][col + 1].content is None and
                                self.cells[row + 1][col + 1].content is None and
                                self.cells[row + 2][col + 1].content is None
                            )

                        if can_place:
                            self.cells[row][col].content = Cell.CIRCLE
                            self.cells[row][col + 1].content = Piece.C
                            self.cells[row + 1][col + 1].content = Piece.C
                            self.cells[row + 2][col + 1].content = Cell.CIRCLE
                            path += Piece.C
                            row += 2
                            col += 2

                        else:
                            current_piece = Piece.get_next_piece(current_piece)
                            continue

                else:
                    max_col = len(self.cells[0]) - 1

                    if col <= 0:
                        solved = True
                        break

                    if current_piece == Piece.A:
                        if col == max_col:
                            can_place = (
                                self.cells[row][col].content is None and
                                self.cells[row][col - 1].content is None and
                                self.cells[row][col - 2].content is None
                            )

                        else:
                            can_place = (
                                self.cells[row][col + 1].content == Cell.CIRCLE and
                                self.cells[row][col].content is None and
                                self.cells[row][col - 1].content is None and
                                self.cells[row][col - 2].content is None
                            )

                        if can_place:
                            self.cells[row][col].content = Cell.CIRCLE
                            self.cells[row][col - 1].content = Piece.A
                            self.cells[row][col - 2].content = Cell.CIRCLE
                            path += Piece.A
                            col -= 3

                        else:
                            current_piece = Piece.get_next_piece(current_piece)
                            continue

                    elif current_piece == Piece.B:
                        if col == max_col:
                            can_place = (
                                self.cells[row][col].content is None and
                                self.cells[row][col - 1].content is None and
                                self.cells[row - 1][col - 1].content is None and
                                row - 1 >= 0 and
                                col - 1 >= 0
                            )

                        else:
                            can_place = (
                                self.cells[row][col + 1].content == Cell.CIRCLE and
                                self.cells[row][col].content is None and
                                self.cells[row][col - 1].content is None and
                                self.cells[row - 1][col - 1].content is None and
                                row - 1 >= 0 and
                                col - 1 >= 0
                            )

                        if can_place:
                            self.cells[row][col].content = Cell.CIRCLE
                            self.cells[row][col - 1].content = Piece.B
                            self.cells[row - 1][col - 1].content = Cell.CIRCLE
                            path += Piece.B
                            row -= 1
                            col -= 2

                        else:
                            current_piece = Piece.get_next_piece(current_piece)
                            continue

                    elif current_piece == Piece.C:
                        if col == 0:
                            can_place = (
                                self.cells[row][col].content is None and
                                self.cells[row - 1][col].content is None and
                                self.cells[row - 2][col].content is None and
                                self.cells[row - 2][col - 1].content is None and
                                row - 2 >= 0 and
                                col - 1 >= 0
                            )

                        else:
                            can_place = (
                                self.cells[row][col + 1].content == Cell.CIRCLE and
                                self.cells[row][col].content is None and
                                self.cells[row - 1][col].content is None and
                                self.cells[row - 2][col].content is None and
                                self.cells[row - 2][col - 1].content is None and
                                row - 2 >= 0 and
                                col - 1 >= 0
                            )

                        if can_place:
                            self.cells[row][col].content = Cell.CIRCLE
                            self.cells[row - 1][col].content = Piece.C
                            self.cells[row - 2][col].content = Piece.C
                            self.cells[row - 2][col - 1].content = Cell.CIRCLE
                            path += Piece.C
                            row -= 2
                            col -= 2

                        else:
                            current_piece = Piece.get_next_piece(current_piece)
                            continue

                current_piece = Piece.get_next_piece(current_piece)

            except:
                current_piece = Piece.get_next_piece(current_piece)
                continue

        if not is_left_to_right:
            return path[::-1]

        else:
            return path


for _ in range(5):
    numbers = [int(s) for s in input().split(" ")]
    rows = numbers[0]
    cols = numbers[1]
    blocked_numbers = numbers[4::]
    starting_number = numbers[2]

    grid = Grid(rows, cols, *blocked_numbers)
    print(grid.find_path(starting_number))
