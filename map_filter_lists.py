words = ["python", "java", "javasript", "C", "C++"]

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))



temp = [0, 10, 20, 30, 40, 50]

def convert(temp_in_c):
    return (temp_in_c * 9/5) + 32

temp_in_f = list(map(convert, temp))




#Labda

temp_using_lambda = list(map(lambda x:x * 9/5 + 32, temp))

temp_in_integer = []
for i in temp_using_lambda:
    tempreature = int(i)
    temp_in_integer.append(tempreature)
print(temp_in_integer)
