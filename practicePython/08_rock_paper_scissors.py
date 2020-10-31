"""
Created on Wed Jul  1 23:01:32 2020

@author: jd.devroutine
"""
print("GRA >>> KAMIEŃ, PAPIER, NOŻYCE<<<")
player1 = input("Podaj nazwę gracza 1: ")
player2 = input("Podaj nazwę gracza 2: ")
move = ("kamien", "papier", "nozyce")

while True:

    player1_move = input("Gracz 1 podaj ruch: kamien, papier, nozyce: ")
    player2_move = input("Gracz 2 podaj ruch: kamien, papier, nozyce: ")

    if player1_move == player2_move:
        print(player1_move, "VS", player2_move)
        print("Remis!")

    elif player1_move == "kamien":
        if player2_move == "papier":
            print(player1_move, "VS", player2_move)
            print("Wygrywa", player2)
        else:
            print(player1_move, "VS", player2_move)
            print("Wygrywa", player1)

    elif player1_move == "papier":
        if player2_move == "nozyce":
            print(player1_move, "VS", player2_move)
            print("Wygrywa", player2)
        else:
            print(player1_move, "VS", player2_move)
            print("Wygrywa", player1)

    elif player1_move == "nozyce":
        if player2_move == "kamien":
            print(player1_move, "VS", player2_move)
            print("Wygrywa", player2)
        else:
            print(player1_move, "VS", player2_move)
            print("Wygrywa", player1)

    elif (player1_move != move) or (player2_move != move):
        print("Nie ma takiego ruchu")

    if (input("Czy chcesz zagrać ponownie? tak/nie: ") == "tak"):
        continue
    else:
        print("Koniec gry!")
        break
