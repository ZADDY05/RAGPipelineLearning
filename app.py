from RAGPipeline.DocumentLoader import load_all_docs
from RAGPipeline.VectorStore import FaissVectorStore

if __name__=='__main__':
    docs=load_all_docs("data")
    store=FaissVectorStore("faiss_store")
    store.build_from_documents(docs)