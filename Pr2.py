import numpy as np

# Створення вектора (1, 2, 3)
vector = np.array([1, 2, 3])

# Виведення вектора і типу масиву
print("Вектор:", vector)
print("Тип масиву:", type(vector))

# Створення матриці
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Виведення матриці
print("\nМатриця:")
print(matrix)

# Створення нульової матриці розміром (4, 5)
zero_matrix = np.zeros((4, 5))

# Виведення нульової матриці
print("\nНульова матриця:")
print(zero_matrix)

# Створення одиничної матриці розміром (3, 3)
identity_matrix = np.identity(3)

# Виведення одиничної матриці
print("\nОдинична матриця:")
print(identity_matrix)

# Виведення розміру матриці
print("\nРозмір матриці:", matrix.shape)

# Створення матриць A і B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, -2, -3], [-4, -5, -6]])

# Операції додавання і віднімання для матриць A і B
addition_result = A + B
subtraction_result = A - B

# Виведення результатів
print("\nСума матриць A і B:")
print(addition_result)
print("\nРізниця матриць A і B:")
print(subtraction_result)

# Поелементне множення матриць A і B
elementwise_multiply_result = A * B

# Виведення результату
print("\nПоелементне множення матриць A і B:")
print(elementwise_multiply_result)

# Додавання константи b=2 до матриці A
b = 2
A_plus_b = A + b

# Виведення результату
print("\nМатриця A плюс константа b:")
print(A_plus_b)

# Створення матриць
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 1], [1, 1], [1, 1]])

# Множення матриці A на матрицю B
matrix_multiply_result = np.dot(A, B)

# Виведення результату
print("\nМноження матриці A на матрицю B:")
print(matrix_multiply_result)

# Створення векторів
v = np.array([1, 2, 3])
u = np.array([1, 1, 1])

# Знаходження Евклідової норми
norm_v = np.linalg.norm(v)
norm_u = np.linalg.norm(u)

# Виведення результату
print("\nЕвклідова норма вектора v:", norm_v)
print("Евклідова норма вектора u:", norm_u)
