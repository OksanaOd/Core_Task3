import re

#Hometask 3
# нормалізує телефонні номери до стандартного формату
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
  pattern = r"[;,\-:!\.() n t \\]"
  for num in raw_numbers:
    modified_text = '+380'+re.sub(pattern, "", num)[-9:]
    return modified_text

normalize_phone = [normalize_phone(num) for num in raw_numbers]
print("Преобразовані тел.номери:", normalize_phone)