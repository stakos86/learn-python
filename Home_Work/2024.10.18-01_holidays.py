import holidays
from datetime import datetime, timedelta

current_date = datetime.now().date()

# russian_holidays = holidays.Russia(years=2024)
# for date, name in sorted(russian_holidays.items()):
#     print(f"{date}: {name}")

russian_holidays = holidays.Russia()
holidays_2024 = russian_holidays.get(current_date.year)
nearest_three = sorted(holidays_2024.items(), key=lambda x: abs(x[0] - current_date))[:3]
for date, name in nearest_three:
    print(f"{date}: {name}")