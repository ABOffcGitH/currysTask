# Currys Task 

Create a multi-turn chat agent that answers real-world questions using an ESG policy document (note that not all questions will refer to the document).

The agent should be user-friendly and accessible to a non-technical audience, consistently providing relevant answers.

The backend code should be written in Python and remain concise and readable. Include a separate file outlining the application's limitations, potential issues, and areas for future improvement.

It's recommended to consider evaluation strategies for the application, including appropriate metrics to track and methods for measuring them.




### 1. Install dependencies

- pip install -r requirements.txt


### 2. Prepare the vector store

- python index_document.py

### 3. Start the FastAPI server

- uvicorn app:app --reload

### 4. Ask a question

- Send a POST request to http://127.0.0.1:8000/ask:

  {
      "question": "What ESG risks should my business prioritize?"
  }

  {
  "answer": "You should prioritize climate risks, stakeholder engagement, and governance structure......",
  "source_documents": [
  
    {"source": "esg-brochure.pdf", "page": 5},
    {"source": "esg-brochure.pdf", "page": 12}

]
}

# Evaluation




# Tech Stack
- Python 3.10+
- LangChain
- OpenAI GPT-3.5 / GPT-4
- ChromaDB
- FastAPI
- PDF Parsing (PyMuPDF / PyPDF)


# License
MIT License
