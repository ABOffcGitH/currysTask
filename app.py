from fastapi import FastAPI
from pydantic import BaseModel
from esg_chain import get_esg_chain

app = FastAPI()
chain = get_esg_chain()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_esg(query: Query):
    
    result = chain({"question": query.question})
    return {
        "answer": result["answer"],
        "source_documents": [doc.metadata for doc in result["source_documents"]]
    }
