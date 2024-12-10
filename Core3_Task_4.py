from datetime import datetime, date, timedelta
import re

#Hometask 4
# виводить список колег, яких потрібно привітати з днем народження на один тиждень вперед.
users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Olesia Ouk", "birthday": "1990.12.14"}
]

def string_to_date(date_string):
  return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
  return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
  prepared_list = []
  for user in user_data:
    prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
  return prepared_list


def find_next_weekday(start_date, weekday):
  days_ahead = weekday - start_date.weekday()
  if days_ahead <= 0:
    days_ahead += 7
  return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
  if birthday.weekday() >= 5:
    return find_next_weekday(birthday, 0)
  return birthday


def get_upcoming_birthdays(users, days=7):
  upcoming_birthdays = []
  today = date.today()
  for user in users:
    birthday_this_year = user["birthday"].replace(year=today.year)
    if birthday_this_year < today:          
      birthday_this_year = user["birthday"].replace(year=today.year+1) #перенос след год
    if 0 <= (birthday_this_year - today).days <= days: #входит в бдиж 7 дней
      birthday_this_year= adjust_for_weekend(birthday_this_year) #перенос віходніх дней
      upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(birthday_this_year)})
  return upcoming_birthdays
    
prepared_users =prepare_user_list(users)
upcoming_birthdays =get_upcoming_birthdays(prepared_users) 
print(upcoming_birthdays)   