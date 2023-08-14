from gensim import models
from keybert import KeyBERT

# KeyBERT model to extract important words/phrases and block stop words from query sentence
kw_model = KeyBERT()

# Word2vec model to generate like terms
model = models.Word2Vec.load('app/model/display.model')

# Extract keywords and keyphrases from query


def extract_phrases(query):
    extraction = kw_model.extract_keywords(
        query, keyphrase_ngram_range=(1, 2), stop_words='english')
    keywords = [entry[0].replace(
        " ", "-") if " " in entry[0] else entry[0] for entry in extraction]
    return keywords

# Find related terms for each word


def retrieve_related_terms(text):
    # Check if token(term) is in the vocab
    # If so generate related terms
    # Otherwise return null to prevent errors/crashing
    if text in model.wv.key_to_index:
        # Generate related terms
        pre_formatted_tokens = model.wv.most_similar(text, topn=5)

        # Format related terms as an array of terms.
        # Only return keys that don't match the query text (ie. don't return cola for coca-cola)
        related_terms = [
            token[0] for token in pre_formatted_tokens]
        return related_terms
    else:
        return []

# Extract keywords, find their related terms and return a set of unique values


def generate_like_terms(query):
    keywords = extract_phrases(query)

    final_terms = []
    for word in keywords:
        related_terms = retrieve_related_terms(word)
        final_terms.extend(related_terms)
    return list(set(final_terms))
