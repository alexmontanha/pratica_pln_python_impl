import re
import nltk
import spacy

from nltk.corpus import stopwords
from nltk import ngrams

corpus = """A Sra. Rosa plantou uma rosa no jardim. O céu estava azul e a brisa era suave. 
Ela pensou: 'Seria maravilhoso se todos os dias fossem assim, tão tranquilos quanto uma rosa em flor.'"""

tokens = re.findall(r'\w+', corpus.lower())  # Divide em palavras e transforma para minúsculas
print("Tokens:", tokens)

tokens_normalizados = [re.sub(r'[^\w\s]', '', token) for token in tokens]  # Remove pontuações
print("Tokens Normalizados:", tokens_normalizados)

nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))
tokens_filtrados = [word for word in tokens_normalizados if word not in stop_words]
print("Tokens Sem Stop Words:", tokens_filtrados)

# Unigramas
unigramas = list(ngrams(tokens_filtrados, 1))
print("Unigramas:", unigramas)

# Bigramas
bigramas = list(ngrams(tokens_filtrados, 2))
print("Bigramas:", bigramas)

# Trigramas
trigramas = list(ngrams(tokens_filtrados, 3))
print("Trigramas:", trigramas)

nlp = spacy.load('pt_core_news_sm')
doc = nlp(" ".join(tokens_filtrados))
tokens_lematizados = [token.lemma_ for token in doc]
print("Tokens Lematizados:", tokens_lematizados)

