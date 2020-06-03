mapping = {'male':0, 'female':1}


cols = ['A', 'B', 'C']
df[cols] = df[cols].applymap(mapping.get())