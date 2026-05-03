import random


# Функція для генерації унікальних та відсортованих чисел для лотерейного квитка
def get_numbers_ticket(min, max, quantity):
    # Перевірка на коректність вхідних даних
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        # Якщо вхідні дані некоректні, повертаємо порожній список
        return []


    # Генерація унікальних та відсортованих чисел
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    # Повертаємо відсортований список чисел
    return sorted(lottery_numbers)


# Приклад використання функції get_numbers_ticket
lottery_numbers = get_numbers_ticket(1, 49, 6)


# Виведе 6 унікальних та відсортованих чисел в заданому діапазоні
print("Ваші лотерейні числа:", lottery_numbers)