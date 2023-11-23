import pandas as pd
import matplotlib.pyplot as plt

# Зчитайте файл players_20.csv
df_data = pd.read_csv('players_20.csv')

# Виведіть перші 5 рядків
print(df_data.head())
print("\n")

# Отримайте розміри об'єкту DataFrame
shape = df_data.shape
print("Розміри об'єкту DataFrame:", shape)

# Отримайте список стовпців міток
df_columns = list(df_data.columns)
print("Список стовпців міток:", df_columns)

# Перелік стовпців, які видалю
useless_columns = ['dob', 'sofifa_id', 'player_url', 'long_name', 'body_type', 'real_face', 'loaned_from', 'nation_position', 'nation_jersey_number']

# Видаліть вказані вище мітки стовпців
df_dropped = df_data.drop(columns=useless_columns, axis=1)
print("\n")

# Виведіть останні 5 рядків за стовпцем 'weight_kg'
last_5_rows_weight_kg = df_dropped['weight_kg'].tail(5)
print(last_5_rows_weight_kg)
print("\n")

# Виведіть перші 5 рядків за двома стовпцями 'short_name' і 'weight_kg'
first_5_rows_short_name_weight_kg = df_dropped[['short_name', 'weight_kg']].head(5)
print(first_5_rows_short_name_weight_kg)

# Розрахунок BMI
df_dropped['BMI'] = df_dropped['weight_kg'] / ((df_dropped['height_cm'] / 100) ** 2)
print("\n")
# Виведення перших 5 рядків DataFrame зі стовпцем 'BMI'
print(df_dropped[['short_name', 'weight_kg', 'height_cm', 'BMI']].head())
print("\n")
# Вивести перші п'ять рядків зі стовпцями 'short_name' і 'BMI'
print(df_dropped[['short_name', 'BMI']].head())


# Побудова гістограми розподілу гравців за віком
plt.hist(df_dropped['age'], bins=20, color='darkorange', edgecolor='purple')
plt.title('Розподіл гравців за віком')
plt.xlabel('Вік')
plt.ylabel('Кількість гравців')
plt.show()
