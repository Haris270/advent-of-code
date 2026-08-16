def read_ranges(filename):
    """
    Reads a file containing comma-separated ranges of the form:
    start-end,start-end,...
    Returns a list of (start, end) integer tuples.
    """
    ranges = []
    with open(filename, "r") as file:
        content = file.read().strip()
        for part in content.split(","):
            start, end = map(int, part.split("-"))
            ranges.append((start, end))
    return ranges


#print(read_ranges("example.txt"))


def generate_invalid_ids_for_digits(digits):
    """
    Generates all invalid IDs with exactly `digits` digits.
    An invalid ID is a number formed by repeating a digit sequence twice.
    """
    half = digits // 2
    start = 10 ** (half - 1)
    end = 10 ** half

    for x in range(start, end):
        yield int(str(x) + str(x))


def sum_invalid_ids_in_range(start, end):
    """
    Returns the sum of all invalid IDs that lie within [start, end].
    """
    total = 0

    min_digits = len(str(start))
    max_digits = len(str(end))

    for digits in range(min_digits, max_digits + 1):
        if digits % 2 != 0:
            continue  # must be even

        for invalid_id in generate_invalid_ids_for_digits(digits):
            if invalid_id > end:
                break
            if invalid_id >= start:
                total += invalid_id

    return total


def solution(filename="example.txt"):
    """
    Main driver function.
    """
    ranges = read_ranges(filename)
    final_sum = 0

    for start, end in ranges:
        final_sum += sum_invalid_ids_in_range(start, end)

    print(final_sum)


solution("code.txt")