import math
def suma(num1, num2):
    resultado = num1+num2
    return resultado

def resta(num1, num2):
    resultado = num1-num2
    return resultado

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

def division(num1, num2):
    if num2==0:
        return "No se puede dividir entre cero"
    else:
        resultado = num1/num2
        return resultado
    

def potencia(base, exponente):
    if base==0 and exponente==0:
        return "0^0 esta indefinido"
    else:
        resultado = math.pow(base, exponente)
        return resultado

def raizCuadrada(num):
    if num<0:
        return "El numero debe ser positivo"
    else:
        resultado = math.sqrt(num)
        return resultado

def factorialR(num):
    if num<0:
        return "El numero debe ser positivo"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorialR(num - 1)

def factorial(num):
    if num<0:
        return "El numero debe ser positivo"
    elif num == 0 or num == 1:
        return 1
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado



