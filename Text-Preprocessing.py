import re, nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


def expand_contractions(text):
    text = re.sub(r"can't", "can not", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"'s", " ", text)
    text = re.sub(r"'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"'re", " are ", text)
    text = re.sub(r"'d", " would ", text)
    text = re.sub(r"'ll", " will ", text)
    return text


def remove_url(text):
    return re.sub(r"""((http[s]?://)[^ <>'"{}|\^`[\]]*)""", r" ", text)


def remove_handles(text):
    return re.sub(r"@\S+", r" ", text)


def remove_incomplete_last_word(text):
    return re.sub(r"\S+…", r" ", text)


remove_punc = lambda x: re.sub(r"\W", " ", x)

remove_num = lambda x: re.sub(r"\d", " ", x)

remove_css = lambda x: re.sub(r"<style.*>[\s\S]+</style>", " ", x)

remove_js = lambda x: re.sub(r"<script.*>[\s\S]*</script>", " ", x)

remove_html = lambda x: re.sub(
    r"<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});", " ", x
)

remove_extra_spaces = lambda x: re.sub(r"\s+", " ", x)

remove_shortwords = lambda x: " ".join(word for word in x.split() if len(word) > 2)

remove_unusualwords = lambda x: " ".join(word for word in x.split() if len(word) < 16)

lower_case = lambda x: x.lower()

stop_words = set(nltk.corpus.stopwords.words("english"))
remove_stopwords = lambda x: " ".join(
    word for word in x.split() if word not in stop_words
)

ps = PorterStemmer()
ps_stem = lambda x: " ".join(ps.stem(word) for word in x.split())

wnl = WordNetLemmatizer()
wnl_lemmatize = lambda x: " ".join(wnl.lemmatize(word) for word in x.split())


def tag_pos(x):
    tag_list = nltk.pos_tag(nltk.word_tokenize(x))
    pos = ""
    for t in tag_list:
        pos += t[0] + "(" + t[1] + ")" + " "
    return pos


def cleanText(x, rsw, stm, lem, tgps):
    x = str(x)
    x = remove_url(x)
    x = remove_css(x)
    x = remove_js(x)
    x = remove_html(x)
    x = lower_case(x)
    x = expand_contractions(x)
    x = remove_punc(x)
    x = remove_num(x)
    x = remove_extra_spaces(x)
    x = remove_shortwords(x)
    x = remove_unusualwords(x)
    x = remove_incomplete_last_word(x)
    if rsw:
        x = remove_stopwords(x)
    if stm:
        x = ps_stem(x)
    if lem:
        x = wnl_lemmatize(x)
    if tgps:
        x = tag_pos(x)
    return x
