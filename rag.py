from embedings import get_embeddings
from vector_store import collection
from ollama import chat
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import os
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
print(f"Using model: {MODEL_NAME}")

env = Environment(
    loader=FileSystemLoader("promtps")
)

template = env.get_template("rag_prompt.jinja2")

def retrieve_relevant_documents(question):
    try:
        # Get embeddings fot the question
        question_embeddings = get_embeddings(question)
        results = collection.query(
            query_embeddings=question_embeddings,
            n_results=3  # Number of relevant documents to retrieve
        )
        return results['documents'][0]
    except Exception as e:
        print(f"Error occurred while retrieving relevant documents: {e}")
        return []

def ask_rag(question):
    try:
        # Retrieve relevant documents based on the question
        relevant_docs = retrieve_relevant_documents(question)
        context = "\n".join(relevant_docs) 

        prompt = template.render(
    context=context,
    question=question
)
        response = chat(model=MODEL_NAME,
                        messages=[
                            {"role": "system", "content": '''You are a helpful assistant for Lala Company. Answer the user's question using ONLY the information provided in the context. If the answer cannot be found in the context, say that the information is not available in the company document.'''},
                            {"role": "user", "content": prompt}
                        ],
                        think=False,
                        options={
                            "temperature": 0.2,
                            "top_k": 40,
                            "num_predict": 10000
                        })
        return response.message.content
    
    except Exception as e:
        print(f"Error occurred while retrieving documents: {e}")
        return "Sorry, I couldn't retrieve relevant documents at the moment."

if __name__ == "__main__":
    user_question = input("Enter your question: ")
    answer = ask_rag(user_question)
    print(f"Answer: {answer}")
