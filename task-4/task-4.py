from datetime import datetime, timedelta

# Функція для визначення майбутніх днів народження
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    # Проходимо по кожному користувачу в списку
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув в цьому році, розглядаємо дату на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Розраховуємо кількість днів до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Якщо день народження відбувається протягом наступного тижня
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() >= 5:  # Якщо день народження припадає на вихідний
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))  # Переносимо на наступний понеділок
            
            # Додаємо інформацію про користувача та дату привітання до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    # Повертаємо список з інформацією про користувачів та датами привітань
    return upcoming_birthdays

# Словник з інформацією про користувачів та їхні дні народження
users = [
    {"name": "John Doe", "birthday": "1985.05.10"},
    {"name": "Jane Smith", "birthday": "1990.05.06"}
]

# Використання функції get_upcoming_birthdays
upcoming_birthdays = get_upcoming_birthdays(users)

# Виводимо список привітань на цьому тижні
print("Список привітань на цьому тижні:", upcoming_birthdays)