top_five = data.value_counts().n_largest(5).index
data_updated = data.where(data.isin(top_five), other="Other")
