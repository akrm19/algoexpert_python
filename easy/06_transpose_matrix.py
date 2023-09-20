def transposeMatrix(matrix):
    # Write your code here.
    transposed = []

    for colIdx in range(len(matrix[0])):
        newRow = []
        for rowIdx in range(len(matrix)):
            newRow.append(matrix[rowIdx][colIdx])
        transposed.append(newRow)

    return transposed
