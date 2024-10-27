# Exercício: Processamento de Linguagem Natural - Tokenização e Normalização de Texto

## Objetivo

Proposta de solução para o exercício de processamento de linguagem natural, com foco em tokenização, normalização, remoção de stop words, geração de n-gramas e lematização de texto, presente em [Exercício: Processamento de Linguagem Natural - Tokenização e Normalização de Texto](https://github.com/alexmontanha/pratica_pln_python)

## 1. **Inicializando o Projeto**

Crie um ambiente virtual e instale as bibliotecas necessárias:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install nltk spacy
python -m spacy download pt_core_news_sm
```

## 2. **Importando o Corpus**

Defina o corpus textual fornecido:

```python
corpus = """A Sra. Rosa plantou uma rosa no jardim. O céu estava azul e a brisa era suave. 
Ela pensou: 'Seria maravilhoso se todos os dias fossem assim, tão tranquilos quanto uma rosa em flor.'"""
```

## 3. **Implementação**

### Passo 3.1: Tokenização

Neste passo, usamos a biblioteca `re` para dividir o texto em tokens:

```python
import re

tokens = re.findall(r'\w+', corpus.lower())  # Divide em palavras e transforma para minúsculas
print("Tokens:", tokens)
```

### Passo 3.2: Normalização

Remova pontuações e converta as palavras para minúsculas, caso ainda não tenha feito:

```python
tokens_normalizados = [re.sub(r'[^\w\s]', '', token) for token in tokens]  # Remove pontuações
print("Tokens Normalizados:", tokens_normalizados)
```

### Passo 3.3: Remoção de Stop Words

Utilize a lista de stop words em português do `nltk` para filtrar palavras irrelevantes:

```python
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('portuguese'))
tokens_filtrados = [word for word in tokens_normalizados if word not in stop_words]
print("Tokens Sem Stop Words:", tokens_filtrados)
```

### Passo 3.4: Geração de n-gramas

Gere unigramas, bigramas e trigramas usando `nltk`:

```python
from nltk import ngrams

# Unigramas
unigramas = list(ngrams(tokens_filtrados, 1))
print("Unigramas:", unigramas)

# Bigramas
bigramas = list(ngrams(tokens_filtrados, 2))
print("Bigramas:", bigramas)

# Trigramas
trigramas = list(ngrams(tokens_filtrados, 3))
print("Trigramas:", trigramas)
```

### Passo 3.5: Lematização

Utilize `spacy` para a lematização:

```python
import spacy

nlp = spacy.load('pt_core_news_sm')
doc = nlp(" ".join(tokens_filtrados))
tokens_lematizados = [token.lemma_ for token in doc]
print("Tokens Lematizados:", tokens_lematizados)
```

## 4. **Resultados Esperados**

Com o código acima, espera-se obter:

- **Tokens normalizados** e sem stop words.
- **N-gramas** para diferentes tamanhos.
- **Texto lematizado** para consolidar palavras com raízes semelhantes.

## 5. **Referências**

- [NLTK](https://www.nltk.org/)
- [spaCy](https://spacy.io/)
- [Exercício: Processamento de Linguagem Natural - Tokenização e Normalização de Texto](https://github.com/alexmontanha/pratica_pln_python)
