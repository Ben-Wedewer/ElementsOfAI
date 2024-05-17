import math

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''

def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    # Sort vocabulary to ensure consistent ordering
    vocabulary.sort()

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequency of the word 'he' in the first document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # calculate tf-idf value
            tf_value = tf[word][doc_index]
            idf_value = math.log(N / df[word], 10)
            tfidf_value = tf_value * idf_value
            tfidf.append(tfidf_value)

        print(tfidf)

main(text)
