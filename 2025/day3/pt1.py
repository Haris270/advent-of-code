
def findVoltage(digits):
    l = 0
    n = len(digits)
    maxVal = '0'
    for r in range(1,n):
        curr = digits[l] + digits[r]
        maxVal = max(curr, maxVal)

        if digits[r] > digits[l]:
            l = r
    return int(maxVal)
            


# res = findVoltage(['2','3','4','2','3','4','2','3','4','2','3','4','2','7','8'])
# print(res)



total_voltage = 0
with open("inputd3.txt", 'r') as file:
    for line in file:
        single_line = list(line.strip())
        total_voltage += findVoltage(single_line)

print(total_voltage)
