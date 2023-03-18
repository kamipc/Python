print("Bem vindo ao jogo de adivinhação!")

secret_number = 42
tries = 3
round = 1

for round in range(1, tries + 1):
#while(round <= tries):
    print("Tentativa {} de {}".format(round, tries)) 
    guess = input("Digite um número entre 1 e 100: ")
    #input sempre volta o resultado como string

    print("Você digitou ", guess)

    if(guess < 1 or guess > 100):
        print("Número inválido. O número deve ser entre 1 e 100.")
        #continue para pula para a próxima iteração
        #sem fazer o restante do código
        continue

    guess = int(guess)

    #para adicionar condição no else usa elif
    if(guess == secret_number):
        print("Você acertou!")
        #break encerra e vai finalizar o loop do 
        #for ou while e seguir o código
        break
    else:
        if(guess > secret_number):
            print("Incorreto! Seu número é maior do que o número secreto")
        else:
            print("Incorreto! Seu número é menor do que o número secreto")
    
    #round = round + 1

print("Fim de Jogo.")