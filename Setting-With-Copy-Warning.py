# instead of 
df[df['gender'] == 'F']['gender'] = 'Female'
# do
df.loc[df['gender'] == 'F', 'gender'] = 'Female'