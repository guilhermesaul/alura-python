print("*"*40)
print("Bem vindo no jogo de Adivinhação!")
print("*"*40)
num_secreto = 42
tentativas = 5
rodada = 1
while rodada <= tentativas:
    print(f"Rodada {rodada} de {tentativas}")
    rodada += 1
    chute = int(input("Digite o seu número: "))
    print(f"Você digitou {chute}")
    if num_secreto == chute:
        print("Você acertou")
        break
    elif chute > num_secreto:
        print("Errado! O seu chute foi maior que o número secreto")
    else:
        print("Errado! O seu chute foi menor que o número secreto")
print("Fim do jogo")