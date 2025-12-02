#bigrama

import nltk
from nltk.util import ngrams
from collections import Counter

texto = "Só sei que nada sei"

tokenizado = nltk.word_tokenize(texto.lower())
bigrama = list(ngrams(tokenizado, 2))
frequenciaPalavra = Counter(bigrama)

print(frequenciaPalavra)
print(bigrama)
