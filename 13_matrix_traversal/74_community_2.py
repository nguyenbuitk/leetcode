def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    row, col  = 0, cols-1
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else: col -= 1
    return False