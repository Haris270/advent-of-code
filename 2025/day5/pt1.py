import re


def getRange(single_line):
    match = re.search(r"-", single_line)
    start = int(single_line[:match.start()])
    end = int(single_line[match.start()+1:])
    return [start, end]

def binary_search(all_ranges, val):
    l = 0
    r = len(all_ranges)-1


    while l<r:
        mid = (l+r)//2
        lower_bound = all_ranges[mid][0]
        upper_bound = all_ranges[mid][1]


        if lower_bound <= val <= upper_bound:
            return True 
        
        elif val < lower_bound:
            r = mid 
        
        else:
            # if val <= all_ranges[mid][1]:
            #     return True
            l = mid+1

    if all_ranges[l][0] <= val <= all_ranges[l][1]:
        return True 
    
    return False

def merge_range(range_arr):
    i = 0
    while i<len(range_arr)-1:
        current = range_arr[i]
        next = range_arr[i+1]

        if current[0] <= next[0] <= current[1]:
            current[1] =  max(next[1], current[1])

            range_arr.pop(i+1)

        else:
            i += 1


    
#10,35


with open("d5input.txt", 'r') as file:
    all_ranges = []
    res = 0
    
    for line in file:
        if not line.strip():
            break

        single_line = line.strip()
        curr_range = getRange(single_line)
        all_ranges.append(curr_range)
    
    all_ranges.sort()
    merge_range(all_ranges)
    # print("---------Merged Range------------")
    # print(all_ranges)
    for ingredient in file:
        if binary_search(all_ranges, int(ingredient)):
            res += 1
        # print(single_line)

print("--------------Blank Line Reached---------------")
print(res)

