# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa
# corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es
# <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

print("Introduce tu peso (en kg)")
peso = int(input())
print("Introduce tu estatura (en metros)")
estatura = int(input())
imc = peso / (estatura**2)
print("Tu índice de masa corporal es:", f'{imc:.2f}')
