documents={
    1: "apple banana orange",
    2: "apple banana",
    3: "banana orange",
    4: "apple",
    5: "apple banana"
}

def create_inverted_index(documents):
  inverted_index={}
  for doc_id, doc_text in documents.items():
    for term in doc_text.split():
      term=term.lower() 
      inverted_index.setdefault(term,set()).add(doc_id)
  return inverted_index

#create the inverted index
inverted_index = create_inverted_index(documents)

def boolean_and(operands, index):
  result = set(index.get(operands[0],set()))
  for term in operands[1:]:
    result = result.intersection(index.get(term, set()))
  return list(result)

def boolean_or(operands,index):
  result=set()
  for term in operands:
    result.update(index.get(term,set()))
  return list(result)

def boolean_not(term, index, num_documents):
  all_docs=set(range(1,num_documents + 1)) 
  return list(all_docs - index.get(term,set())) 

# Example queries
query1 = ["apple", "banana"]
query2 = ["apple", "orange"]
# Performing Boolean Model queries
result1 = boolean_and(query1, inverted_index)
result2 = boolean_or(query2, inverted_index)
result3 = boolean_not("orange", inverted_index, len (documents))
print(inverted_index)
# Printing results
print("Documents containing 'apple' and 'banana':", result1)
print("Documents containing 'apple' op 'orange':", result2)
print("Documents not containing 'orange':", result3)

import nltk
nltk.download("stopwords")

# Code
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import numpy as np

train_set = ["The sky is blue.", "The sun is bright."]
test_set = ["The sun in the sky is bright."]
stopWords = stopwords.words('english')
vectorizer = TfidfVectorizer(stop_words=stopWords)
train_matrix = vectorizer.fit_transform(train_set)
test_matrix = vectorizer.transform(test_set)
print(train_matrix)
print(test_matrix)

# Calculate cosine similarity for each document 
for test_vector in test_matrix.toarray():
  for train_vector in train_matrix.toarray():
    cosine_similarity = np.dot(test_vector, train_vector) / (np.linalg.norm(test_vector) * np.linalg.norm(train_vector))
print(f"Cosine similarity between test document and train document: {cosine_similarity:.3f}")


