T = int(input())
output = ''
while T != 0:
    ln = input()
    lnls = ln.split(' ')
    a = int(lnls[0])
    b = int(lnls[1])
    Ari = False

    while a > 0 and b > 0:
        if Ari:
            Ari = False
        else:
            Ari = True

        if a > b:
            a = a % b
        else:
            b = b % a

    if Ari:
        output = output + "Ari\n"
    else:
        output = output + "Rich\n"

    T = T - 1
print(output)