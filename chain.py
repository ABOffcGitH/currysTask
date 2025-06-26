from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings
from config import VECTOR_DB_DIR

def get_esg_chain() -> ConversationalRetrievalChain:  # Initializes ConversationalRetrievalChain with memory and retriever .
  
    vectordb = Chroma(persist_directory=VECTOR_DB_DIR, embedding_function=OpenAIEmbeddings())
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )
    return qa_chain
