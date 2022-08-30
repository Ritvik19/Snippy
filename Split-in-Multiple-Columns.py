df[["fisrt", "middle", "last"]] = df.name.str.split(" ", expand=True)
