from sklearn.feature_extraction.text import CountVectorizer


def get_top_n_gram(corpus, ngram_range, n=None):
    vec = CountVectorizer(ngram_range=ngram_range, stop_words="english").fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


top_n_gram = get_top_n_gram(data["text_clean"], (i, j), 20)

df = (
    pd.DataFrame(top_n_gram, columns=["Text", "count"])
    .groupby("Text")
    .sum()["count"]
    .sort_values(ascending=False)
)
sns.barplot(df.values, df.index, color="b", ax=ax[i][0])
