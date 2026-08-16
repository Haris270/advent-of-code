
currNum = 50
zeroCount = 0
with open("input.txt", "r") as file:
    for line in file:

        sign = line[0]
        val = int(line[1:]) % 100

        if (sign == 'L'):
            currNum = currNum - val

        else:
            currNum = currNum + val


        if currNum < 0:
            print(f"Negative Val: {currNum}")
            
            currNum = 100 + currNum

        elif currNum >= 100:
            currNum = currNum - 100

        if currNum == 0:
            zeroCount += 1

print(zeroCount)

