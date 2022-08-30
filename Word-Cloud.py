import numpy as np
import pandas as pd

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def buildWordCloud(text):
    wordcloud = WordCloud(
        width=W, height=H, background_color=BGC, min_font_size=10, max_words=mw
    ).generate(text)
    plt.figure(figsize=(W // 100, H // 100), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
