df['Change'] = df.col.diff()
df['Percent Change'] = df.col.pct_change()*100
df.style.format({'Percent Change':'{:.2f}%'})