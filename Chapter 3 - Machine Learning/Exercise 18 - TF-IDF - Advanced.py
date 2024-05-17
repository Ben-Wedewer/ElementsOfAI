import math
from itertools import combinations

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def tf_idf(docs, vocabulary):
    N = len(docs)
    df = {}
    tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])

    tf_idf_vectors = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            tf_value = tf[word][doc_index]
            idf_value = math.log(N / df[word], 10)
            tfidf_value = tf_value * idf_value
            tfidf.append(tfidf_value)
        tf_idf_vectors.append(tfidf)
    
    return tf_idf_vectors

def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(a ** 2 for a in vec2))
    if not magnitude1 or not magnitude2:
        return 0
    return dot_product / (magnitude1 * magnitude2)

def main(text):
    # Split text into lines and words, and lower case the words
    docs = [line.lower().split() for line in text.split('\n')]

    # Create the vocabulary of unique words
    vocabulary = list(set(word for doc in docs for word in doc))
    vocabulary.sort()  # Ensure consistent order

    # Calculate the TF-IDF vectors for each document
    tf_idf_vectors = tf_idf(docs, vocabulary)

    # Calculate the cosine similarity between each pair of documents
    max_similarity = -1
    most_similar_pair = None
    for (i, vec1), (j, vec2) in combinations(enumerate(tf_idf_vectors), 2):
        similarity = cosine_similarity(vec1, vec2)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_pair = (i, j)

    print(most_similar_pair)

main(text)
