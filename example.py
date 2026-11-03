def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    
    numbers = ""
    for number in range(1, n+1):
        numbers += str(number)
    return numbers
    
        
print(number_pattern(4))