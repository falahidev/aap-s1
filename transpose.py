matrix = []
transpose = []

r = int(input().strip())
c = int(input().strip())

for i in range(r):
    elements = input().strip().split()
    if len(elements) != c: quit()
    elements = [int(a) for a in elements]
    matrix.append(elements)


for i in range(c):
    transpose_row = []
    for j in matrix:
        transpose_row.append(j[i])
    transpose.append(transpose_row)


for i in range(r):
    print(matrix[i])

for i in range(c):
    print(transpose[i])