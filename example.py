even_numbers = [num for num in range(51) if  num % 2 == 0]

print(even_numbers)

numbers = [1, 2, 3, 4, 5]

result = [(num, "even") if num % 2 == 0 else (num, "odd") for num in numbers]

print (result)