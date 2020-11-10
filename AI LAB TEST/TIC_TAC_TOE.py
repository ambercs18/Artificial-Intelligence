def print_board(a):
    print("", a[1], " │", a[2], " │ ", a[3], " ")
    print("────┼────┼────")
    print("", a[4], " │", a[5], " │ ", a[6], " ")
    print("────┼────┼────")
    print("", a[7], " │", a[8], " │ ", a[9], " ")

def print_instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    print_board(pos)
    print()

    print("\n-------- Instructions ---------")
    print("->", players[0], "you will using X")
    print("->", players[1], "you will using 0")
    print("-> Turn starts from", players[0])
    print("-> Potisions are like :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    print("-> press S to start the game")
    flag = input()
    compfirst(flag)


def compfirst(flag):
    if flag == "S" or flag == "s":
        startcompfirst()
    else:
        print("Invalid Input!!")


def startcompfirst():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("Computer 1 is Playing!!")
            print()
            v = "x"
            if i == 0:
                p = 9
                pos[p] = v
                print_board(pos)
                turn = 1
                continue
            else:
                p = compwin(i)
                pos[p] = v
                print_board(pos)
                winner = checkwin(v)
                if winner == "nobody":
                    turn = 1
                    continue
                else:
                    print("\n\nHurray !!, Computer 1 you win ")
                    break
        else:
            print("Computer 2 is playing")
            print()
            p = logic("0")
            v = '0'
            pos[p] = v
            # print("*" * 20, "Player's Turn", "*" * 20)
            print_board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\n\nHurray !!, Computer 2 wins")
                break
    else:
        print("Game is Tied")


def compwin(i):
    if pos[5] == " " and i == 2:
        if pos[1] == " ":
            return 1
        elif pos[3] == " ":
            return 3
        elif pos[7] == " ":
            return 7
        elif pos[9] == " ":
            return 9

    if pos[5] != " " and i == 2:
        return 1

    for t in winning_conditions:
        if pos[t[0]] == "x" and pos[t[1]] == "x" and pos[t[2]] == " ":
            return t[2]
        if pos[t[0]] == " " and pos[t[1]] == "x" and pos[t[2]] == "x":
            return t[0]
        if pos[t[0]] == "x" and pos[t[1]] == " " and pos[t[2]] == "x":
            return t[1]

    for t in winning_conditions:
        if pos[t[0]] == "0" and pos[t[1]] == "0" and pos[t[2]] == " ":
            return t[2]
        if pos[t[0]] == " " and pos[t[1]] == "0" and pos[t[2]] == "0":
            return t[0]
        if pos[t[0]] == "0" and pos[t[1]] == " " and pos[t[2]] == "0":
            return t[1]

    if pos[7] == " " and pos[5] == " ":
        return 7
    else:
        return pos.index(" ")


def checkwin(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v, v, v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner


def logic(v):
    if "0" not in pos:
        if pos[5] == " ":
            return 5
        else:
            return 1
    else:
        for t in winning_conditions:
            c, awin = 0, 0
            if pos[t[0]] == "0" and pos[t[1]] == "0" and pos[t[2]] == " ":
                return t[2]
            elif pos[t[0]] == "0" and pos[t[1]] == " " and pos[t[2]] == "0":
                return t[1]
            elif pos[t[0]] == " " and pos[t[1]] == "0" and pos[t[2]] == "0":
                return t[0]

        for t in winning_conditions:
            if pos[t[0]] == "x" and pos[t[1]] == "x" and pos[t[2]] == " ":
                return t[2]
            elif pos[t[0]] == "x" and pos[t[1]] == " " and pos[t[2]] == "x":
                return t[1]
            elif pos[t[0]] == " " and pos[t[1]] == "x" and pos[t[2]] == "x":
                return t[0]

        if pos[3] == " ":
            return 3
        elif pos[6] == " ":
            return 6
        elif pos[9] == " ":
            return 9
        return pos.index(" ")


# main code
pos = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
players = ['Computer 1', 'Computer 2']
winning_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
print_instructions()



