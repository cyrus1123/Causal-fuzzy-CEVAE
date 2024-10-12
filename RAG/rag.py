
import json
from typing import List

class RAGModel:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def retrieve_documents(self, query: str) -> List[str]:
        return [doc for doc in self.knowledge_base if query in doc]

    def generate_response(self, query: str):
        relevant_docs = self.retrieve_documents(query)
        return " ".join(relevant_docs)
