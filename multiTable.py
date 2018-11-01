def print_multiplication_table(max=1):
    i = 1
    print "-" * max * 5
    while i < max + 1:
        n = 1
        while n <= max:
            print "%4d" % (i * n)
            n += 1
        print ""
        i += 1
    print "-" * max * 5


print_multiplication_table(30)
