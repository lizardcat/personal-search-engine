import os 
import string

DATA_DIR = "data" # the directory containing the samples

def load_documents(data_dir):
    documents = {} # creates an empty dictionary
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as f: 
                documents[filename] = f.read()
    return documents

def tokenize(text):
    translator = str.maketrans("", "", string.punctuation) # building a translation table without any punctuation
    return text.lower().translate(translator).split() # Formats the text; lowercases it and removes whitespace

def build_inverted_index(documents):
    index = {} # creating an empty index dictionary
    for doc_id, text in documents.items():
        for word in tokenize(text):
            if word not in index: 
                index[word] = set()
            index[word].add(doc_id)
    return index

def search(index, query): 
    query = query.lower()
    return index.get(query, set())