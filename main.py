import guessgame

print("Escolha o jogo:")
game = int(input("(1) Jogo da Adivinhação (2)Jogo da Forca"))

if(game == 1):
    guessgame.play()
elif(game == 2):
    print("jogo a ser criado")
else:
    print("Escolha inválida")