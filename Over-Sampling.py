q, r = divmod((data[col].value_counts().max() / data[col].value_counts())[1], 1)

data_over = pd.concat(
    [data[data[col] == 1]]*int(q) + 
    [data[data[col] == 1].sample(frac=r), data[data[col] == 0]]
).sample(frac=1.00)[[col] + feats]