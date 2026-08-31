from ollama import embed
from dotenv import load_dotenv
from convert_doc_to_text import convert_docx_to_text
import os
load_dotenv()

EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME")

def get_embeddings(text):
    try:
        respone = embed(model=EMBEDDING_MODEL_NAME, input=text)
        return respone.embeddings[0]
    except Exception as e:
        print(f"Error occurred while getting embeddings: {e}")
        return None

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error occurred while reading the text file: {e}")
        return ""

# if __name__ == "__main__":
#     docx_path = "/Users/niraj/Documents On Mac/Projects/Python Basics/llm/company_document.docx"
#     text_file_path = "/Users/niraj/Documents On Mac/Projects/Python Basics/llm/company_document.txt"

#     convert_docx_to_text(docx_path)
#     sample_text = read_text_file(text_file_path)

#     lines = sample_text.strip().splitlines()

#     for chunk in range(0, len(lines), 5):
#           # Process 5 lines at a time
#         chunk_text = '\n'.join(lines[chunk:chunk+5])
#         embeddings = get_embeddings(chunk_text)

#         if embeddings is not None:
#             #print(f"Embeddings for '{lines[chunk]}': {embeddings}")
#             pass
#         else:
#             print(f"Failed to get embeddings for '{lines[chunk]}'.")
#     #embeddings = get_embeddings(sample_text)
#     #chunks = sample_text.strip().split()
#     #for chunk in chunks:
#         # embeddings = get_embeddings(chunk)
#         # if embeddings is not None:
#         #     print(f"Embeddings for '{chunk}': {embeddings}")
#         # else:
#         #     print(f"Failed to get embeddings for '{chunk}'.")