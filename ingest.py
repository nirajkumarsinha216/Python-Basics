from embedings import get_embeddings, read_text_file
from vector_store import add_data_to_vector_store
from convert_doc_to_text import convert_docx_to_text
import os



def create_chunks_from_text(text):
    """
    Create chunks of text from the input text.

    Args:
        text (str): The input text.

    Returns:
        list: A list of text chunks.
    """
    lines = text.strip().splitlines()
    chunks = []
    for chunk in range(0, len(lines), 5):
        chunk_text = '\n'.join(lines[chunk:chunk+5])
        chunks.append(chunk_text)
    return chunks

def create_embeddings_for_chunks(chunks):
    """
    Create embeddings for each chunk of text.

    Args:
        chunks (list): A list of text chunks.
    Returns:
        list: A list of embeddings corresponding to each chunk.
    """
    embeddings = []
    try:
        for chunk in chunks:
            embedding = get_embeddings(chunk)
            embeddings.append(embedding)
        print("Embeddings created successfully.")
    except Exception as e:
        print(f"Error occurred while creating embeddings: {e}")
    return embeddings

if __name__ == "__main__":
    docx_path = "/Users/niraj/Documents On Mac/Projects/Python Basics/llm/company_document.docx"
    text_file_path = "/Users/niraj/Documents On Mac/Projects/Python Basics/llm/company_document.txt"

    # Convert .docx to text
    convert_docx_to_text(docx_path)

    # Read the text file
    sample_text = read_text_file(text_file_path)

    # Create chunks from the text
    chunks = create_chunks_from_text(sample_text)
    print(f"Total chunks created: {len(chunks)}")
    # Create embeddings for each chunk
    embeddings = create_embeddings_for_chunks(chunks)

    # Add data to vector store
    add_data_to_vector_store(chunks, embeddings)