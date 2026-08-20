import re

def mergeRange(original):
    
    i = 0
    while i< len(original)-1:
        curr = original[i]
        next = original[i+1]

        if curr[0] <= next[0] <= curr[1]:
            curr[1] = max(next[1], curr[1])
            original.pop(i+1)

        else:
            i+=1
    

def countRange(original):
    total = 0

    for curr in original:
        curr_sum = curr[1]-curr[0] + 1
        total += curr_sum

    return total
        



with open("d5input.txt", 'r') as file:
    all_range = []
    for line in file:
        if not line.strip():
            break
        single_line = line.strip()

        # get index of dash in the line
        dash = re.search(r"-", single_line).start()

        # get start & end of range and append as list to all_range
        r_start = int(single_line[:dash])
        r_end = int(single_line[dash+1:])
        all_range.append([r_start, r_end])

    all_range.sort()
    mergeRange(all_range)
    print(f"Merged Range: {all_range}")
    print( countRange(all_range))

    

