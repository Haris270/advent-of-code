
# res = findVoltage(['2','3','4','2','3','4','2','3','4','2','3','4','2','7','8'])

# res = findVoltage(['2','7','4','2','3','4','2','3','1', '1', '1', '1', '2','3','4','2','7','8'])

# def findVoltage(digits):
#     e1 = len(digits) - 11

#     max1 = max(digits[:e1+1])

#     i1 = digits.index(max1)

#     for  i in range(i1+1, len(digits)):


def findVoltage(digits):
    stack = []
    n = len(digits)
    drop = n - 12
    maxVal = ""
    for num in digits:
        while drop > 0 and stack and stack[-1] < num:
            stack.pop()
            drop -= 1
        stack.append(num)

    for digit in stack[:12]:
        maxVal += digit

    return int(maxVal)
    #print(int(maxVal))
    #print(stack)


#findVoltage(['2','7','4','2','3','4','2','3','1', '1', '1', '1', '2','3','4','2','7','8'])
#findVoltage(list("2223223335223234342422322225224113422423142441542233322124236224232234222242262232142124444266221211"))

total_voltage = 0
with open("inputd3.txt", 'r') as file:
    for line in file:
        single_line = list(line.strip())
        total_voltage += findVoltage(single_line)

print(total_voltage)
    

