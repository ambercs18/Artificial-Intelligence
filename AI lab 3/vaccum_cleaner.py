def clean(ar, i, j):
    ar[i][j] = 0
    return ar


def show(ar, a, b):
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if i == a and j == b:
                print("-> {}".format(ar[i][j]), end="\t")
            else:
                print(ar[i][j], end="\t")
        print()


print("Enter row and columns")
n, m = map(int, input().split())
print("Enter the current state")
ar = []
for i in range(n):
    a = []
    ar.append(input().split())

for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print("Move - Right")
            if ar[i][j] == "1":
                print("Sense - Dirty")
                ar = clean(ar, i, j)
                show(ar, i, j)
                print("*" * 20)
            else:
                print("Sense - Clean")
                print("*" * 20)

    else:
        for j in range(m - 1, -1, -1):
            print("Move - Left")
            if ar[i][j] == "1":
                print("Sense - Dirty")
                clean(ar, i, j)
                show(ar,i,j)
                print("*" * 20)
            else:
                print("Sense - Clean")
                print("*" * 20)

    print("Move - Down")
