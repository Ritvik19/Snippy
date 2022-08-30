df["c"] = df[["a", "b"]].apply(lambda row: row["a"] + row["b"], axis=1)
