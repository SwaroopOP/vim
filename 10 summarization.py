import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')

def extractive_summarization_and_qa(text, question=None, num_sentences=3):
  def extractive_summarization(text, num_sentences):
    sentences = nltk.sent_tokenize(text)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    scores = similarity_matrix.sum(axis=1)
    ranked_sentences_indices = scores.argsort()[-num_sentences:][::-1]
    summary = [sentences [i] for i in sorted(ranked_sentences_indices)]
    return ' '.join(summary)

  def answer_question(question, text):
    sentences = nltk.sent_tokenize(text)
    sentences.insert(0, question)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    index = similarity_matrix.argsort()[0][-2]
    return sentences[index]

  if question:
    return answer_question(question, text)
  else:
    return extractive_summarization(text, num_sentences)

text = "Scientists recently discovered a new species of butterfly in the Amazon rainforest. The butterfly, named Morpho amadeus, has vibrant blue wings with intricate patterns. Researchers believe its discovery sheds light on the biodiversity of the region and underscores the importance of conservation efforts in preserving fragile ecosystems like the Amazon."
#question = "What was recently discovered in the Amazon rainforest?"
question = "What is the name of butterfly that has vibrant blue wings?"
result = extractive_summarization_and_qa(text, question)
print(result)
