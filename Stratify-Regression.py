# Sturge's Rule:
# No. of bins = 1 + log2(N)
# where N is the number of samples

num_bins = int(np.floor(1 + np.log2(len(data))))
data['bins'] = pd.cut(data[target], bins=num_bins, labels=False)
# this column can be used to stratify the data