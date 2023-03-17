print("Bem vindo ao jogo de adivinhação!")

secret_number = 42

guess = input("Digite o seu número: ")

print("Você digitou ", guess)

guess = int(guess)

if(secret_number == guess):
    print("Você acertou!")
else:
    print("Você errou.")