moves = 0
lifes = 3
direction = ""
correctCombination = "SSNWES"
a = 0;
while a < len(correctCombination):

    prompt = "Which way do you want to go? (N, S , W, E )"
    election = input(prompt)
    if election != "N" and election != "S" and election != "W" and election != "E":
        print("Invalid input, please type N, W, E or S")
        moves += 1

    elif election == "N" or election == "S" or election == "W" or election == "E":

        if election == correctCombination[a]:

            direction = direction + election
            print("Good choice, you are now one step closer!")
            moves += 1
            a += 1
            if direction == (correctCombination):
                print("You won")
                print("You did it in", moves, "moves.")
                print("You had", lifes, "lifes left.")
                break


        else:

            print("Incorrect, Try again")
            moves += 1
            a = 0

    if moves % 10 == 0:

        lifes -= 1
        print("You lost a life")
        if lifes == 0:
            print("Game Over, you lost all your lifes")
            break