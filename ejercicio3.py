# Escribir un programa
# que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

print("¿Cuántas horas usted trabajó?")
horas = int(input())
print("¿Cuánto le pagan por hora?")
coste = int(input())
paga = horas * coste
print("Su paga de este mes es:", paga)
quit(print("Fin del código"))