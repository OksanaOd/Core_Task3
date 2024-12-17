import random
# Hometask 2
#генерує набір унікальних випадкових чисел у межах заданих параметрів 
def get_numbers_ticket(min, max, quantity):
  list_digitals = []
  i=0  
  while i < quantity :
    new_elem = random.randint(min,max)
    if list_digitals.count(new_elem)==0:
      #ця умова виключає неунікальні числф
      list_digitals.append(new_elem)
      i= i + 1
  return sorted(list_digitals)    

min = int(input("Ввведить MIN , яке не менше 1 "))
max = int(input("Ввведить MAX, яке не більше 1000 "))
quantity = int(input("Ввведить quantity ")) 
if min<1 or max>1000 or (max-min)<0 :
  print("MIN та MAX повинні бути між 1 то 1000,та MAX повинен бути більше MIN ")
elif (max-min+1)<quantity :
  print(f"при введених MIN та MAX , quantity має бути не більше {max-min+1}")
else:
  numbers_ticket=get_numbers_ticket(min, max, quantity)
  print("Випадкові числа:", numbers_ticket)