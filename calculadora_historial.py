a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operación (+, -, *, /): ")
if op == "+":
 resultado = a + b
elif op == "-":
 resultado = a - b
elif op == "*":
 resultado = a * b
elif op == "/":
 resultado = a / b
else:
 resultado = "Operación no válida"
print(f"Resultado: {resultado}")