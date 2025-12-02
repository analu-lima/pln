import nltk

# nltk.download("all")

texto = "Só sei que nada sei"

tokenizado = nltk.word_tokenize(texto.lower()) #tokenizacao e transformação do texto para minusculo

print(len(tokenizado)) #printar a quantidade de palavras
print(tokenizado)