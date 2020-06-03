with \
    open('a.txt') as a,\
    open('b.txt', 'w') as b:
    for line in a:
        b.write(line)