from datetime import datetime


# Соответсвие месяца и количества дней в нём
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def get_today_date() -> str:
    today_date = datetime.today().strftime('%d.%m.%Y')
    return today_date


def get_tomorrow_date() -> str:
    today_datetime = datetime.today()
    year = today_datetime.year
    month = today_datetime.month
    day = today_datetime.day
    # Проверка дополнительного дня в високосном году
    if month == 2 and year % 4 == 0:
        if day == 29:
            month += 1
            day = 1
        else:
            day += 1

    elif months[month] == day:
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        day = 1
    else:
        day += 1
    tomorrow_date = str(day) + '.' + str(month) + '.' + str(year)
    return tomorrow_date
