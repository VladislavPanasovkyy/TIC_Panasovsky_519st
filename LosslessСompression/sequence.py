import random
import string
import collections
import math
import matplotlib.pyplot as plt

# Функція для обчислення характеристик послідовності та збереження їх у файл
def process_sequence(sequence, sequence_name, N_sequence, results_table):
    # Розрахунок кількості байт для збереження послідовності
    Original_sequence_size = len(sequence)

    # Визначення розмірності алфавіту
    unique_chars = set(sequence)
    sequence_alphabet_size = len(unique_chars)

    # Розрахунок ймовірностей появи символів
    counts = collections.Counter(sequence)
    probability = {symbol: count / N_sequence for symbol, count in counts.items()}

    # Розрахунок середньої ймовірності
    mean_probability = sum(probability.values()) / len(probability)

    # Визначення типу ймовірності
    equal = all(abs(prob - mean_probability) < 0.05 * mean_probability for prob in probability.values())
    uniformity = "рівна" if equal else "нерівна"

    # Розрахунок ентропії
    entropy = -sum(p * math.log2(p) for p in probability.values())

    # Розрахунок надмірності джерела
    if sequence_alphabet_size > 1:
        source_excess = 1 - entropy / math.log2(sequence_alphabet_size)
    else:
        source_excess = 1

    # Збереження результатів у файл results_sequence.txt
    with open("sequence.txt", "a") as file:
        file.write(f"{sequence_name}:\n")
        file.write(f"Послідовність: {sequence}\n")
        file.write(f"Розмір алфавіту: {sequence_alphabet_size}\n")
        file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n")
        file.write(f"Ймовірності появи символів: {', '.join([f'{symbol}={prob:.4f}' for symbol, prob in probability.items()])}\n")
        file.write(f"Середня ймовірність: {mean_probability:.4f}\n")
        file.write(f"Однорідність: {uniformity}\n")
        file.write(f"Ентропія: {entropy:.4f}\n")
        file.write(f"Надмірність джерела: {source_excess:.4f}\n\n")

    # Додавання результатів до таблиці
    results_table.append([sequence_alphabet_size, round(entropy, 2), round(source_excess, 2), uniformity])


# Задання розмірності та кількості елементів '1'
N_sequence = 100
student_number = 11
last_name = "Панасовський"
group_number = 519


# Генерація тестової послідовності №1 та розрахунок параметрів:

# Генерація послідовності
list1 = ['1'] * student_number
list0 = ['0'] * (N_sequence - student_number)
sequence_1 = ''.join(random.sample(list1 + list0, N_sequence))

# Визначення розмірності алфавіту
unique_chars = set(sequence_1)
Sequence_alphabet_size = len(unique_chars)

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_1)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №1:\n")
    file.write(f"Послідовність: {sequence_1}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №2 та розрахунок параметрів:

# Генерація послідовності
list1 = list(last_name)
list0 = ['0'] * (N_sequence - len(last_name))
sequence_2 = ''.join(list1 + list0)

# Визначення розмірності алфавіту
unique_chars = set(sequence_2)
Sequence_alphabet_size = len(unique_chars)

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_2)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №2:\n")
    file.write(f"Послідовність: {sequence_2}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №3 та розрахунок параметрів:

# Генерація послідовності
list1 = list(last_name)
list0 = ['0'] * (N_sequence - len(last_name))
sequence_3 = list1 + list0
random.shuffle(sequence_3)
sequence_3 = ''.join(sequence_3)

# Визначення розмірності алфавіту
unique_chars = set(sequence_3)
Sequence_alphabet_size = len(unique_chars)

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_3)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №3:\n")
    file.write(f"Послідовність: {sequence_3}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №4 та розрахунок параметрів:

# Створення списку букв прізвища та цифр номера групи
letters = list(last_name) + [int(digit) for digit in str(group_number)]

# Визначення довжини списку letters
n_letters = len(letters)

# Визначення кількості повторів всього списку letters у межах розміру формованої послідовності
n_repeats = N_sequence // n_letters

# Визначення залишку елементів, що залишається після визначення кількість повторів
remainder = N_sequence % n_letters

# Створення списку шляхом множення елементів списку letters на кількість повторів
list_sequence_4 = letters * n_repeats

# Додавання залишку елементів до створеного списку
list_sequence_4 += letters[:remainder]

# Представлення списку у вигляді рядку
sequence_4 = ''.join(map(str, list_sequence_4))

# Визначення розмірності алфавіту
unique_chars = set(sequence_4)
Sequence_alphabet_size = len(unique_chars)

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_4)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №4:\n")
    file.write(f"Послідовність: {sequence_4}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №5 та розрахунок параметрів:

# Задання розмірності та прізвища та номера групи
N_sequence = 100
last_name = "Панасовський"[:2]
group_number = 519

# Створення списку букв прізвища та цифр номера групи
letters = list(last_name) + [int(digit) for digit in str(group_number)]

# Ймовірність появи будь-якого елементу
Pi = 0.2

# Створення списку з урахуванням ймовірності
list_sequence_5 = [random.choice(letters) if random.uniform(0, 1) > Pi else random.choice([char for char in letters if char != last_name[0]]) for _ in range(N_sequence)]

# Перемішування елементів списку
random.shuffle(list_sequence_5)

# Представлення списку у вигляді рядку
sequence_5 = ''.join(map(str, list_sequence_5))

# Визначення розмірності алфавіту
unique_chars = set(sequence_5)
Sequence_alphabet_size = len(unique_chars)

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_5)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №5:\n")
    file.write(f"Послідовність: {sequence_5}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №6 та розрахунок параметрів:

# Задання розмірності та прізвища та номера групи
N_sequence = 100
last_name = "Панасовський"[:2]
group_number = 519

# Створення списку букв прізвища та цифр номера групи
letters = list(last_name) + [int(digit) for digit in str(group_number)]

# Ймовірність появи букв і цифр
P_letters = 0.7
P_digits = 0.3

# Визначення кількості букв та цифр
n_letters = int(P_letters * N_sequence)
n_digits = int(P_digits * N_sequence)

# Створення списку
list_sequence_6 = [random.choice(letters) for _ in range(n_letters)] + [random.choice(string.digits) for _ in range(n_digits)]

# Перемішування елементів списку
random.shuffle(list_sequence_6)

# Представлення списку у вигляді рядку
sequence_6 = ''.join(map(str, list_sequence_6))

# Визначення розмірності алфавіту
unique_chars = set(sequence_6)
Sequence_alphabet_size = len(unique_chars)

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_6)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №6:\n")
    file.write(f"Послідовність: {sequence_6}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №7 та розрахунок параметрів:

# Створення списку
elements = string.ascii_lowercase + string.digits
list_sequence_7 = [random.choice(elements) for _ in range(N_sequence)]

# Представлення списку у вигляді рядку
sequence_7 = ''.join(map(str, list_sequence_7))

# Визначення розмірності алфавіту
Sequence_alphabet_size = len(set(elements))

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_7)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №7:\n")
    file.write(f"Послідовність: {sequence_7}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Генерація тестової послідовності №8 та розрахунок параметрів:

# Створення рядка
sequence_8 = '1' * N_sequence

# Визначення розмірності алфавіту
Sequence_alphabet_size = 1  # оскільки алфавіт складається лише з одного символу

# Визначення кількості байт для збереження послідовності
Original_sequence_size = len(sequence_8)

# Збереження результатів у файл results_sequence.txt
with open("results_sequence.txt", "a") as file:
    file.write(f"Тестова послідовність №8:\n")
    file.write(f"Послідовність: {sequence_8}\n")
    file.write(f"Розмір алфавіту: {Sequence_alphabet_size}\n")
    file.write(f"Розмір послідовності (bytes): {Original_sequence_size}\n\n")


# Додавання всіх послідовностей до списку
original_sequences = [
    sequence_1, sequence_2, sequence_3,
    sequence_4, sequence_5, sequence_6,
    sequence_7, sequence_8
]

# Обробка кожної послідовності та збереження результатів у файл і таблицю
results_table = []
for idx, sequence in enumerate(original_sequences, start=1):
    process_sequence(sequence, f"Послідовність випробувань {idx}", N_sequence, results_table)

# Створення таблиці та збереження її у файл
fig, ax = plt.subplots(figsize=(14/1.54, len(original_sequences)/1.54))
ax.axis('off')

headers = ['Розмір алфавіту', 'Ентропія', 'Надмірність', 'Ймовірність']
row = [f"Послідовність {i}" for i in range(1, len(original_sequences) + 1)]

table = ax.table(cellText=results_table, colLabels=headers, rowLabels=row, loc='center', cellLoc='center')
table.set_fontsize(14)
table.scale(0.8, 2)

# Збереження таблиці та результатів
fig.savefig("Характеристики сформованих послідовностей.png")