'''def areaTriangulo(base, altura):
    return (base * altura) / 2

triangulo1 = areaTriangulo(10, 5)
triangulo2 = areaTriangulo(7, 3)

print("El área del triángulo 1 es:", triangulo1)
print("El área del triángulo 2 es:", triangulo2)'''

# Usando una función lambda para calcular el área de un triángulo
areaTriangulo = lambda base, altura: (base * altura) / 2 
print("El área del triángulo 1 es:", areaTriangulo(10, 5))
print("El área del triángulo 2 es:", areaTriangulo(7, 3))
print("")
alcubo = lambda x: x ** 3
print("El cubo de 2 es:", alcubo(2))
print("")
destacar_valor = lambda comision:"{}$".format(comision)
print(destacar_valor(500))