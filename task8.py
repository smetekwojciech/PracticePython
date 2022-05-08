# Make a two-player Rock-Paper-Scissors game.

player1=input("Player 1 please enter yout name : ")
player2=input("Player 2 please enter yout name : ")

next_turn=0
while next_turn!=1:
    player1_hand=input(player1+" please write Rock/Paper/Scissors\n")
    player2_hand=input(player2+" please write Rock/Paper/Scissors\n")

    if((player1_hand=="Rock"and player2_hand=="Rock")or(player1_hand=="Paper"and player2_hand=="Paper")or(player1_hand=="Scissors"and player2_hand=="Scissors")):
        print("It's a draw!")
    elif((player1_hand=="Rock"and player2_hand=="Scissors")or(player1_hand=="Paper"and player2_hand=="Rock")or(player1_hand=="Scissors"and player2_hand=="Paper")):
        print(player1 +" wins!")
        next_turn=1
    elif((player2_hand=="Rock"and player1_hand=="Scissors")or(player2_hand=="Paper"and player1_hand=="Rock")or(player2_hand=="Scissors"and player1_hand=="Paper")):
        print(player2 +" wins!")
        next_turn=1