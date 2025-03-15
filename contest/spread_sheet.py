from utils import *

class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = []
        self.rows = rows
        # row0 = []
        # for i in range(65, 91):
        #     row0.append(chr(i))
        # self.grid.append(row0)
        for _ in range(rows):
            self.grid.append([0]*26)    

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65
        # print(f"col: {col}")
        row = int(cell[1:]) - 1
        # print(f"row: {row}")
        if row >= self.rows:
            return
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        if "+" in formula:
            s1, s2 = formula.split("+")
            s1 = s1[1:]
            print(f"s1, s2: {s1}, {s2}")
            if not s1.isdigit():
                col = ord(s1[0]) - 65
                row = int(s1[1:]) - 1
                s1 = self.grid[row][col]
            if not s2.isdigit():
                col = ord(s2[0]) - 65
                row = int(s2[1:]) - 1
                s2 = self.grid[row][col]
            return int(s1) + int(s2)
        else:
            if not formula.isdigit():
                col = ord(formula[0]) - 65
                row = int(formula[1:]) - 1
                formula = self.grid[row][col]
            return int(formula)
                
    def print(self):
        print(self.grid)
solution = Spreadsheet(1000)
solution.setCell("A1000", 100000)
solution.setCell("C2", 5)
# solution.print()
print(solution.getValue("=A1000+0"))
