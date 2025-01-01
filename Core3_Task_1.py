from datetime import datetime, date, timedelta
#Hometask 1
#розрахує кількість днів між заданою датою і поточною датою
def string_to_date(date_string):
  return datetime.strptime(date_string, "%Y-%m-%d").date()

def get_days_from_today(date):
  try:
    days_return = (datetime.today().date()-string_to_date(date)).days
    return days_return 
  except:
    print("Вхідна дата має некоректний формат")   
  
days_from_today = get_days_from_today('2024-12-07')
if days_from_today != None:
  print("кількість днів між заданою і поточною датою є", days_from_today)