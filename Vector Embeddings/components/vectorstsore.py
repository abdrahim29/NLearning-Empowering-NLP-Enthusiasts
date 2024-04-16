from langchain_community.vectorstores import FAISS
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
import os
from dotenv import load_dotenv
load_dotenv()

class vectorStore:
    def __init__(self, is_load, index_name):
        self.is_load = is_load
        self.index_name = index_name
        self.qdrant_url = os.getenv("qdrant_url")
        self.qdrant_api_key = os.getenv("qdrant_api")

    def vectorstore_faiss(self,embedding_model, chunks):
        try:
            if not self.is_load:
                db = FAISS.from_documents(chunks, embedding_model)
                db.save_local(self.index_name)
            else:
                db = FAISS.load_local(self.index_name, embedding_model)
            return db

        except Exception as e:
            print(f"Error: {e}")    

    def create_vectorstore_qdrant(self, embedding_model, chunks, index_name ):
        try:
            if not self.is_load:
                vector_db = Qdrant.from_documents(
                    documents = chunks,
                    embedding = embedding_model,
                    url=self.qdrant_url,
                    # prefer_grpc=True,
                    api_key=self.qdrant_api_key,
                    collection_name=index_name,
                )
            else:
                qdrant_client = QdrantClient(
                    url=self.qdrant_url, 
                    # prefer_grpc=True,
                    api_key=self.qdrant_api_key,
                )
                vector_db= Qdrant(qdrant_client, index_name, embedding_model)
            return vector_db
        except Exception as ex:
            raise Exception({"Error": str(ex)})
