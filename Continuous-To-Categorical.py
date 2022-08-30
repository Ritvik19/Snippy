df["age_groups"] = pd.cut(
    df.age, bins=[0, 18, 65, 99], labels=["child", "adult", "elderly"]
)

# 0 to 18 -> 'child'
# 18 to 65 -> 'adult'
# 65 to 99 -> 'elderly'
