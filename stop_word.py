import nltk
from nltk.corpus import stopwords

texto = "Só sei que nada sei"

palavras = nltk.word_tokenize(texto.lower())
stop_words = set(stopwords.words('portuguese')) #pegando as stop words no idioma portugues

palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_words]

print("palavras sem stop words: ", palavras_filtradas)