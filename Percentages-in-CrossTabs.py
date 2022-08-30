pd.crosstab(df.A, df.B).apply(lambda r: r / r.sum(), axis=1)
