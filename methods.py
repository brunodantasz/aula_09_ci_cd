def area_of_rectangle(width, height):
    area = width*height
    return area
 
def perimeter_of_rectangle(width, height):
    perimeter = 2 * (width + height)
    return perimeter

def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b
