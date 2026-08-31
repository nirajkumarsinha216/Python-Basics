import chromadb


client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection("lala_company")

def add_data_to_vector_store(chunks,embeddings):

    for i, (chunk,embeddings) in enumerate(zip(chunks,embeddings)):
        collection.add(
            ids =[f"chunk_{i}"],
            documents=[chunk],
            embeddings=[embeddings]
        )
    print("Data added to ChromaDB successfully.")