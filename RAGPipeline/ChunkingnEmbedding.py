from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from typing import List, Any

from RAGPipeline.DocumentLoader import load_all_docs
    
import numpy as np
class ChunkEmbeddings:
    def __init__(self, model=None,model_name: str = "all-MiniLM-L6-v2", chunk_size: int = 1000, chunk_overlap: int = 200):
        self.model=model or SentenceTransformer(model_name)
        self.chunk_size=chunk_size
        self.chunk_overlap=chunk_overlap

        print(f"Loading the chunking model : {model_name}")

    def chunk_docs(self, documents : List[Any]) -> List[Any]:
        split=RecursiveCharacterTextSplitter(
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap,
            length_function = len,
            separators=["\n","\n\n"," ",""]
            )
        chunks=split.split_documents(documents)
        print(f"splitting {len(documents)} into {len(chunks)} chunks")
        return chunks
    
    def embed_docs(self, chunks: List[Any])->np.ndarray:
        text=[chunk.page_content for chunk in chunks]
        print(f"Embedding {len(chunks)} chunks into vectorformat")
        embedding=self.model.encode(text,show_progress_bar=True)
        print(f"Embeddings has {embedding.shape} dimension")
        return embedding
    
