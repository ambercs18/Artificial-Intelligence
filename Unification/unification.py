count = 0
arguCount = [None for i in range(10)]
preds = [None for i in range(10)]
args = [[None for i in range(10)] for i in range(10)]


def main():
    global count
    char = 'y'
    while (char == 'y'):
        count = int(input("Enter Number of Predicates: "))
        for i in range(count):
            print("Enter the predicate ", (i + 1), " :")
            preds[i] = input()
            print("Enter No.of Arguments for thePredicate ", preds[i], " :")
            arguCount[i] = int(input())

            for j in range(arguCount[i]):
                print("Enter argument ", j + 1, " :")
                args[i][j] = input()

        printAns()
        predCheck()
        char = input("Do you want to continue(y/n):   ")


def printAns():
    print("The given Predicates are")
    for i in range(count):
        print(preds[i], "(", end="")
        for j in range(arguCount[i]):
            print(args[i][j], end="")
            if (j != arguCount[i] - 1):
                print(",", end="")
        print(")")


def unify():
    flag = 0
    for i in range(count - 1):
        for j in range(arguCount[i]):
            if (args[i][j] != args[i + 1][j]):
                flag = 0
                if (flag == 0):
                    print("The substitution is : ", end="")
                    print(args[i + 1][j], "/", args[i][j])
                    flag += 1

        if (flag == 0):
            print("Arguments are Identical, so no substitution")
            flag += 1


def predCheck():
    flag1 = 0
    flag2 = 0

    for i in range(count - 1):
        if (preds[i] != preds[i + 1]):
            print("Not same, Unification cannot be done")
            flag1 = 1
            break

    if (flag1 != 1):
        ind = 0
        key = arguCount[ind]
        length = len(arguCount)
        for i in range(0, key - 1):
            if i >= key:
                continue
            if ind != length - 1:
                ind += 1
                key = arguCount[ind]
            if (arguCount[i] != arguCount[i + 1]):
                print("Number of arguments are not same")
                argflag = 1
                break

        if (flag2 == 0 and flag1 != 1):
            unify()


main()
