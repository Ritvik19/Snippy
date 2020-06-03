df = pd.DataFrame({'sandwich':  ['PB&J', 'BLT', 'cheese'],
                   'ingredients':[['peanut butter', 'jelly'],
                    ['bacon', 'lettuce', 'tomato'],
                    ['swiss cheese']]})
df
#     sandwich    ingredients
# 0   PB&J        [peanut butter, jelly]
# 1   BLT         [bacon, lettuce, tomato]
# 2   cheese      [swiss cheese]
df.explode('ingredients')
#     sandwich    ingredients
# 0   PB&J        peanut butter
# 0   PB&J        jelly
# 1   BLT         bacon
# 1   BLT         lettuce
# 1   BLT         tomato
# 2   cheese      swiss cheese