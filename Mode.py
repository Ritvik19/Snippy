test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
mode = lambda x: (max(set(x), key = x.count))

mode(test)