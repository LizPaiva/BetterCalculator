
def addmultiplenumbers(numeros):
    return sum(numeros)

def multiplymultiplenumbers(numerosM):
    result = 1
    for i in numerosM:
        result *= i
    return result

def isiteven(numbers):
    if numbers % 2 == 0:
        print("El numero es par: true")
        return True
    else:
        print("El numero no es par: false")
        return False
   
def isitaninteger(numbers):
    if numbers == int(numbers):
        print("El numero es entero")
        return True
    else:
        print("El numero no es entero")
        return False
   
def main():
    print("Hello learners!")
    numbers = [1, 2, 3, 4]
    print("La suma es: ", addmultiplenumbers(numbers))
    numeroMulti = [2,4,6]
    print("La multiplicacion es: ", multiplymultiplenumbers(numeroMulti))
    numeroBoolean = 8
    print(isiteven(numeroBoolean))
    numeroEntero = 2.1
    print(isitaninteger(numeroEntero))
   

if __name__ == "__main__":
    main()
