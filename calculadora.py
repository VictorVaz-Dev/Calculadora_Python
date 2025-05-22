import random

# ---------------- Calculadora ----------------
def calculadora():
    print("\n🧮 Calculadora")
    print("Operações disponíveis: +  -  *  /")

    while True:
        try:
            a = float(input("Digite o primeiro número: "))
            operador = input("Digite o operador (+, -, *, /): ")
            b = float(input("Digite o segundo número: "))

            if operador == '+':
                resultado = a + b
            elif operador == '-':
                resultado = a - b
            elif operador == '*':
                resultado = a * b
            elif operador == '/':
                if b == 0:
                    resultado = "Erro: divisão por zero"
                else:
                    resultado = a / b
            else:
                resultado = "Operador inválido."

            print(f"Resultado: {resultado}")
        except ValueError:
            print("⚠️ Entrada inválida. Tente novamente.")
            continue

        continuar = input("\nFazer outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            break


# ---------------- Gerador de Senhas ----------------
def gerador_senhas():
    print("\n🔐 Gerador de Senhas")
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'
    try:
        comprimento = int(input("Digite o tamanho da senha: "))
        senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
        print(f"Senha gerada: {senha}")
    except ValueError:
        print("⚠️ Entrada inválida. Por favor, digite um número.")


# ---------------- Jogo da Forca (Simples) ----------------
def jogo_da_forca():
    print("\n🎯 Jogo da Forca")
    palavras = ['python', 'programa', 'calculadora', 'jogo', 'codigo']
    palavra = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra]
    tentativas = 6

    while tentativas > 0 and '_' in letras_descobertas:
        print(' '.join(letras_descobertas))
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas -= 1
            print(f"Letra incorreta. Tentativas restantes: {tentativas}")

    if '_' not in letras_descobertas:
        print(f"Parabéns! Você acertou: {palavra}")
    else:
        print(f"Você perdeu. A palavra era: {palavra}")


# ---------------- Menu Principal ----------------
def menu():
    while True:
        print("\n========= MENU DE UTILITÁRIOS =========")
        print("1 - Calculadora")
        print("2 - Gerador de Senhas")
        print("3 - Jogo da Forca")
        print("4 - Sair")
        print("========================================")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            calculadora()
        elif opcao == '2':
            gerador_senhas()
        elif opcao == '3':
            jogo_da_forca()
        elif opcao == '4':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# ---------------- Executa o menu ----------------
menu()
