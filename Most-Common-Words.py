pd.Series(" ".join(df["text"]).split()).value_counts()[:n]
