# Importing the necessary modules from the chromadb package:
# chromadb is used to interact with the Chroma DB database,
# embedding_functions is used to define the embedding model
import chromadb
from chromadb.utils import embedding_functions

# Define the embedding function using SentenceTransformers
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Create a new instance of ChromaClient to interact with the Chroma DB
client = chromadb.Client()

# Define the name for the collection to be created or retrieved
collection_name = "tech_collection"

# Define the main function to interact with the Chroma DB
def main():
    try:
        # Create a collection in the Chroma database with a specified name, 
        # distance metric, and embedding function. In this case, we are using 
        # cosine distance
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing tech-related data"},
            configuration={
                "hnsw": {"space": "cosine"},
                "embedding_function": ef
            }
        )
        print(f"Collection created: {collection.name}")
        return collection
    except Exception as error:  # Catch any errors and log them to the console
        print(f"Error: {error}")
        return None

# Array of tech-related text items
texts = [
    'Python programming language',
    'JavaScript for web development',
    'Machine learning with TensorFlow',
    'React framework for UI',
    'Docker containerization',
    'Git version control',
    'SQL databases',
    'RESTful APIs',
    'Cloud computing with AWS',
    'Cybersecurity best practices',
    'Data science with Pandas',
    'Node.js runtime',
    'Kubernetes orchestration',
    'Blockchain technology'
]

# Create a list of unique IDs for each text item in the 'texts' array
 # Each ID follows the format 'tech_<index>', where <index> starts from 1
ids = [f"tech_{index + 1}" for index, _ in enumerate(texts)]

def add_documents(collection):
    # Add documents and their corresponding IDs to the collection
    # The `add` method inserts the data into the collection
    # The documents are the actual text items, and the IDs are unique identifiers
    # ChromaDB will automatically generate embeddings using the configured embedding function
    collection.add(
        documents=texts,
        metadatas=[{"source": "tech", "category": "technology"} for _ in texts],
        ids=ids
    )

def get_all_items(collection):
    # Retrieve all the items (documents) stored in the collection
    # The `get` method fetches all data from the collection
    all_items = collection.get()
    # Log the retrieved items to the console for inspection
    # This will print out all the documents, IDs, and metadata stored in the collection
    print("Collection contents:")
    print(f"Number of documents: {len(all_items['documents'])}")
    return all_items

# Function to perform a similarity search in the collection
def perform_similarity_search(collection, query_term, n_results=3):
    try:
        # Perform a query to search for the most similar documents to the 'query_term'
        results = collection.query(
            query_texts=[query_term],
            n_results=n_results  # Retrieve top n results
        )
        print(f"\nQuery: '{query_term}'")
        print("Top similar results:")
        for i, doc in enumerate(results['documents'][0]):
            print(f"{i+1}. {doc}")
        return results
    except Exception as error:
        print(f"Error in similarity search: {error}")
        return None

# Function to perform a similarity search in the collection
def search_in_document(document_text, query_term, n_results=3):
    # Create a temporary collection for the document
    temp_collection_name = "temp_doc_collection"
    try:
        client.delete_collection(temp_collection_name)
    except:
        pass
    temp_collection = client.create_collection(
        name=temp_collection_name,
        metadata={"description": "Temporary collection for document search"},
        configuration={
            "hnsw": {"space": "cosine"},
            "embedding_function": ef
        }
    )
    # Split document into sentences (simple split by period)
    sentences = [s.strip() for s in document_text.split('.') if s.strip()]
    ids = [f"sent_{i+1}" for i in range(len(sentences))]
    temp_collection.add(
        documents=sentences,
        ids=ids
    )
    # Query
    results = temp_collection.query(
        query_texts=[query_term],
        n_results=n_results
    )
    print(f"\nSearching in document for '{query_term}':")
    print("Top similar sentences:")
    for i, doc in enumerate(results['documents'][0]):
        print(f"{i+1}. {doc}")
    return results

if __name__ == "__main__":
    collection = main()
    if collection:
        add_documents(collection)
        all_items = get_all_items(collection)
        query = input("Enter a topic to search for: ")
        perform_similarity_search(collection, query)