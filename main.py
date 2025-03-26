def addmultiplenumbers(list_numbers):
    total_sum = 0  
    for number in list_numbers:
        total_sum= total_sum + number
    return total_sum

numbers = [5, 7, 9]
print("La suma es: ", addmultiplenumbers(numbers))

def multiplymultiplenumbers(list_numbers):
    total_mult = 1
    for number in list_numbers:
        total_mult = total_mult * number
    return total_mult

numbers = [5,-7,9.3]
print("La multiplicacion es: ", addmultiplenumbers(numbers))

def isiteven(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
number = 8
print("El numero es par: ", isiteven(number))

def isitaninteger(number):
    answer = isinstance(number, int)
    return answer

number = 8
print("El numero es entero: ", isitaninteger(number))

