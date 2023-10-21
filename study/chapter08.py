# 람다 함수 사용 예제
f = lambda x, y: x * y
print(f(2, 5))

# 맵 리듀스 예제
exercise = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
f = lambda x: x**3 - 2*x**2 + 1
print(list(map(f, exercise)))

f = lambda x, y: x * y
print(list(map(f, exercise, exercise)))

print(list(map(lambda x: x - 2 if x % 2 == 0 else x, exercise)))

from functools import reduce
print(reduce(lambda x, y: x + y, exercise))

# 가변 인수 예제
def aster(a, *args):
    print(a, args)
    print(type(args))

aster(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def aster1(a, **argvs):
    print(a, argvs)
    print(type(argvs))

aster1(1, b=2, c=3, d=4, e=5, f=6)

def aster2(a, *args):
    print(a, args)
    print(type(args))

aster2(1, *(2, 3, 4, 5, 6))

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)

for data in zip(*[[1, 2], [3, 4], [5, 6]]):
    print(data)
    print(type(data))

# 선형대수학 예제
x = [1, 3]
y = [5, 2]
z = [3, 4]

# 벡터 덧셈
result = []
for i in range(len(x)):
    result.append(x[i] + y[i] + z[i])
print(result)

# 벡터 덧셈 (리스트 컴프리헨션 사용)
result = [sum(s) for s in zip(x, y, z)]
print(result)

# 벡터 덧셈 함수 정의
def vector_addition(*args):
    return [sum(t) for t in zip(*args)]
print(vector_addition(x, y, z))

# 행렬 덧셈
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[4, 1], [7, 2]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)

# 행렬 원소 비교
matrix_a = [[2, 2], [2, 2]]
matrix_b = [[2, 2], [2, 2]]
print(all([row[0] == value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row]))

# 논리 연산
print(any([False, False, False]))
print(any([False, True, False]))
print(all([False, True, True]))
print(all([True, True, True]))

# 행렬 전치
matrix_a = [[1, 2, 3, 4], [5, 6, 7, 8]]
result = [[element for element in t] for t in zip(*matrix_a)]
print(result)

# 행렬 곱셈
matrix_a = [[1, 5, 2], [2, 6, 4]]
matrix_b = [[2, 3], [6, 2], [3, 1]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)