
# En este archivo debes implementar la función

def triangulo_simetrico(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m<=0:
        print("error: la altura debe ser un entero positivo")
        return
        
    #parte 1: triangulo creciente
    for 1 in range(1,m+1):
        print(s*1)
    #paerte 2:triangulo decreciente
    for i in range(m-1,0,-1):
        print(s*1)
    # TODO: implementar la lógica para generar el triángulo simétrico en ASCII
