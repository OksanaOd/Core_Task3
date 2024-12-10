from datetime import datetime, date, timedelta

#Hometask 1
#розрахує кількість днів між заданою датою і поточною датою
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def get_days_from_today(date):
  days_return = (datetime.today().date()-string_to_date(date)).days
  return days_return 

days_from_today = get_days_from_today('2023.12.07')
print("кількість днів між заданою і поточною датою є", days_from_today)