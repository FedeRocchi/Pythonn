from lib2to3.pygram import python_grammar_no_print_statement
from tkinter.tix import PopupMenu


print("-----------------------------------")
print("Ejercicio 4")
print("-----------------------------------")

print("Ingrese el número de partidos ganados:")
PG = int(input())
print("Ingrese el número de partidos empatados:")
PE = int(input())
print("Ingrese el número de partidos perdidos:")
PI = int(input())

PPG = int(PG*3)

PPE = int(PE*0)

PPI = int(PI*-1)

PF = int(PPG+PPE+PPI)

print("El puntaje final es:", PF)