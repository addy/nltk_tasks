import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Stem all of the words that aren't stop words.
def stemWords(words):
	stemmer = SnowballStemmer("english")
	stemmedWords = []

	for word in words:
		stemmedWords.append(stemmer.stem(word))

	return stemmedWords

# Lemmatize our stemmed words.
def lemmatizeWords(words):
	lemmatizedWords = []
	lemmatizer = WordNetLemmatizer()

	for word in words:
		lemmatizedWords.append(lemmatizer.lemmatize(word))

	return lemmatizedWords

# Setup tokenizer and open wiki article.
tokenizer = RegexpTokenizer(r'\w+')
file = open('testosterone.txt')
raw = file.read()

# Read in all of the text.
words_with_stops = tokenizer.tokenize(raw)

# Remove stop words.
stop_words = stopwords.words('english')
words = []

for word in words_with_stops:
	if word not in stop_words:
		words.append(word)

# Print stemmed words and lemmatized words respectively.
print(stemWords(words))
print(lemmatizeWords(words))