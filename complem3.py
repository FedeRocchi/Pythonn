print("----------------------------")
print("Tp Complem 3")
print("----------------------------")


print("Ingrese el número de respuestas correctas:")
RC = int(input())
print("Ingrese el número de respuestas en blanco:")
RB = int(input())
print("Ingrese el número de respuestas incorrectas:")
RI = int(input())

PRC = int(RC*3)

PRB = int(RB*0)

PRI = int(RI*-1)

PF = int(PRC+PRB+PRI)

print("El puntaje final es:", PF)