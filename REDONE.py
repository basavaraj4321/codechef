T = int(input())
output = ''
while T != 0:
    N = int(input())
    sum1 = 0
    for i in range(1, N+1):
        sum1 = (sum1 * i) + (sum1 + i)
    output = output + str(sum1) + "\n"
    T = T - 1
print(output)
