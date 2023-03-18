print("Bem vindo ao jogo de adivinhação!")

secret_number = 42
tries = 3
round = 1


#pode ser feito com while onde seria no lugar do for
#while(round <= tries):
#porém no fim do while teria de se adicionar 
#round = round + 1 
#para incrementar o while até o ponto de saida.
for round in range(1, tries + 1):

    print("Tentativa {} de {}".format(round, tries)) 
    guess = input("Digite um número entre 1 e 100: ")
    #input sempre volta o resultado como string

    print("Você digitou ", guess)

    if(guess < 1 or guess > 100):
        print("Número inválido. O número deve ser entre 1 e 100.")
        #continue pula para a próxima iteração do for/while
        continue

    guess = int(guess)

    #para adicionar condição no else usa elif
    if(guess == secret_number):
        print("Você acertou!")
        #break encerra o for/while finalizando o loop
        #seguindo para o código seguinte de fora
        break
    else:
        if(guess > secret_number):
            print("Incorreto! Seu número é maior do que o número secreto")
        else:
            print("Incorreto! Seu número é menor do que o número secreto")

print("Fim de Jogo.")