import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('BAAI/bge-base-en-v1.5')

def embed_chunks(chunks):
    vectors = model.encode(chunks)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)
    return index, vectors