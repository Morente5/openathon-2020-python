'''1-100 even numbers from given 1-100 list
1. Not using list comprehension
2. Using list comprehension
'''

# Given 1-100 list
lista = [*range(1, 101)]

resultado1 = []
for value in lista:
  if not value%2:
    resultado1.append(value)
print(resultado1)

resultado2 = [value for value in lista if not value % 2]
print(resultado2)
