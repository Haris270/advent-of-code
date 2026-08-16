

currNum = 50

zeroCount = 0
DialAtZero = False
with open("input.txt", "r") as file:
    for line in file:

        sign = line[0]

        zeroCount += int(line[1:]) // 100

        val = int(line[1:]) % 100

        prevNum = currNum

        if (sign == 'L'):
            currNum = currNum - val

        else:
            currNum = currNum + val

        
        if currNum < 0:
            if prevNum != 0:
                zeroCount += 1
            currNum = 100 + currNum

        elif currNum == 100:
            zeroCount += 1
            currNum -= 100
            continue

        elif currNum > 100:
    
            zeroCount += 1
            currNum = currNum - 100
            
            
        if currNum == 0:
            zeroCount += 1
            

        
print(zeroCount)

