# Practice Python Ex 8 Rock Scissors Paper
# Make two-player Rock-Scissors Paper game.

while True:
    p1 = input("Player 1, Type r(rock) s(scissors) or p(paper): ")
    p2 = input("Player 2, Type r(rock) s(scissors) or p(paper): ")
    if p1 == p2: print("It's a tie!")
    elif p1 == "r":
        if p2 == "s": print("Rock bashes scissors. Player 1 wins!")
        elif p2 == "p": print("Paper covers rock. Player 2 wins!")
    elif p1 == "s":    
        if p2 == "r": print("Rock bashes scissors. Player 2 wins!")
        elif p2 == "p": print("Scissors cuts paper. Player 1 wins!")
    elif p1 == "p":    
        if p2 == "r": print("Paper covers rock. Player 1 wins!")
        elif p2 == "s": print("Scissors cuts paper. Player 2 wins!")
    x = input("Type 'Y' to play again: ")
    if x != 'Y': exit()
    