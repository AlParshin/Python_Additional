# Напишите функцию для транспонирования матрицы:
# Пример: [[1,2,3],[4,5,6]] --> [[1,4],[2,5],[3,6]]

def transp(m):
    t = [[0, 0], [0, 0], [0, 0]]
    for i in range(len(m)):
        for j in range(len(m[i])):
            t[j][i] = m[i][j]
    return t


matrix = [[1, 2, 3], [4, 5, 6]]
print(transp(matrix))
