from collections import deque

file = open("input", "r", encoding="utf-8")

n, m = map(int, file.readline().strip().split(","))
x, y = map(int, file.readline().strip().split(","))
new_color = file.readline().strip().replace("'", "")

matrix = []

for i in range(n):
    line = file.readline().strip()
    line = line[1:-1]
    parts = line.split(", ")

    row = []
    for j in parts:
        row.append(j.replace("'", ""))

    matrix.append(row)

file.close()

old_color = matrix[x][y]

if old_color != new_color:
    q = deque()
    q.append((x, y))

    while q:
        i, j = q.popleft()

        if matrix[i][j] == old_color:
            matrix[i][j] = new_color

            if i - 1 >= 0:
                if matrix[i - 1][j] == old_color:
                    q.append((i - 1, j))

            if i + 1 < n:
                if matrix[i + 1][j] == old_color:
                    q.append((i + 1, j))

            if j - 1 >= 0:
                if matrix[i][j - 1] == old_color:
                    q.append((i, j - 1))

            if j + 1 < m:
                if matrix[i][j + 1] == old_color:
                    q.append((i, j + 1))

file = open("output.txt", "w", encoding="utf-8")

for row in matrix:
    file.write("[")
    for i in range(len(row)):
        file.write("'" + row[i] + "'")
        if i != len(row) - 1:
            file.write(", ")
    file.write("]\n")

file.close()