columns_to_read = ['foo', 'bar']
df = pd.read_csv(file, usecols=columns_to_read)
columns_to_skip = ['foo','bar']
df = pd.read_csv(file, usecols=lambda x: x not in columns_to_skip)