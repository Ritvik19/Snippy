from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia_obj = SentimentIntensityAnalyzer()


def sentiment_scores(sentence):
    sentiment_dict = sia_obj.polarity_scores(sentence)
    if sentiment_dict["compound"] >= 0.05:
        return 1
    elif sentiment_dict["compound"] <= -0.05:
        return -1
    else:
        return 0
