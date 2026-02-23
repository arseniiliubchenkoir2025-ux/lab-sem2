


def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []

    m = len(matrix)
    n = len(matrix[0])
    result = []

    for diag in range(m + n - 1):
        t = []
        row_start = max(0, diag - n + 1)
        row_end = min(m - 1, diag)

        for i in range(row_start, row_end + 1):
            j = diag - i
            t.append(matrix[i][j])

        if diag % 2 == 0:
            result.extend(t[::-1])
        else:
            result.extend(t)

    return result

