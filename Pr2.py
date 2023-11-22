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

#Завдання 3
# Створення нульової матриці розміром (4, 5)
zero_matrix = np.zeros((4, 5))

# Виведення нульової матриці
print("\nНульова матриця:")
print(zero_matrix)

#Завдання 4
# Створення одиничної матриці розміром (3, 3)
identity_matrix = np.identity(3)

# Виведення одиничної матриці
print("\nОдинична матриця:")
print(identity_matrix)

#Завдання 5
# Виведення розміру матриці
print("\nРозмір матриці:", matrix.shape)


