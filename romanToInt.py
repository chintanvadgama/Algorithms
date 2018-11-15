def roman_to_integer(string):
    lookup = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    numeric = 0
    for i in range(len(string) - 1):
        if lookup[string[i]] < lookup[string[i+1]]:
            numeric -= 1
        else:
            numeric += 1
    return numeric + lookup[string[-1]]
