df
# A B C D E F
# 1 2 3 4 5 6
# 4 5 6 7 8 9

df.insert(3, 'C2', df['C']*2)

df
# A B C C2 D E F
# 1 2 3 6  4 5 6
# 4 5 6 12 7 8 9