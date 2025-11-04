single_digits = range(0, 10)
squares = []
for every_number in single_digits:
  print(every_number)
  squares.append(every_number ** 2)
print(squares)
cubes = [every_number ** 3 for every_number in single_digits]
print(cubes)