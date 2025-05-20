def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("🧮 Calculadora simples em Python")
print("Operações disponíveis: +  -  *  /")

while True:
    try:
        a = float(input("\nDigite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        b = float(input("Digite o segundo número: "))

        if operador == '+':
            resultado = somar(a, b)
        elif operador == '-':
            resultado = subtrair(a, b)
        elif operador == '*':
            resultado = multiplicar(a, b)
        elif operador == '/':
            resultado = dividir(a, b)
        else:
            resultado = "Operador inválido."

        print(f"Resultado: {resultado}")
    except ValueError:
        print("⚠️ Entrada inválida. Tente novamente.")
        continue

    # Menu após o cálculo
    continuar = input("\nDeseja fazer outra fórmula? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando a calculadora. Até a próxima!")
        break
