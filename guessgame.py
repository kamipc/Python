print("Bem vindo ao jogo de adivinhação!")

secret_number = 42
tries = 3
round = 1
while(round <= tries):
    guess = input("Tente advinhar um número: ")
    #input sempre volta o resultado como string

    print("Você digitou ", guess)

    guess = int(guess)

    #para adicionar condição no else usa elif
    if(guess == secret_number):
        print("Você acertou!")
    else:
        if(guess > secret_number):
            print("Incorreto! Seu número é maior do que o número secreto")
        else:
            print("Incorreto! Seu número é menor do que o número secreto")
    
    round = round + 1

print("Fim de Jogo.")