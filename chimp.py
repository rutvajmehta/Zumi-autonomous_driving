a = input()
legLengths = input().split()
pantLengths = input().split()
for i in range(0, len(legLengths)):
    legLengths[i] = int(legLengths[i])
for i in range(0, len(pantLengths)):
    pantLengths[i] = int(pantLengths[i])
discValue = 0
for i in range(0, len(legLengths)):
    discValue += abs(legLengths[i] - pantLengths[i])

print(discValue)
