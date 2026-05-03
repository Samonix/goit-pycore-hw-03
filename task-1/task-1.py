from datetime import datetime

# Введення дати у форматі 'РРРР-ММ-ДД'
set_date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

# Функція для розрахунку кількості днів від заданої дати до сьогоднішньої дати
def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримуємо поточну дату
        today = datetime.today()
        
        # Розраховуємо різницю між поточною датою та заданою датою
        difference = today - input_date
        
        # Повертаємо різницю у днях як ціле число
        return difference.days
    except ValueError:
        return "Невірний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'."
        # Приклад використання

# Виведе кількість днів від заданої дати до сьогоднішньої дати
print(get_days_from_today(set_date))  