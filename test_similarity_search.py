import pytest
import chromadb
from chromadb.utils import embedding_functions
from similarity_search import main, add_documents, get_all_items, perform_similarity_search, texts, ids, collection_name

def test_main():
    collection = main()
    assert collection is not None
    assert collection.name == collection_name

def test_add_documents():
    client = chromadb.Client()
    try:
        collection = client.get_collection(collection_name)
    except:
        collection = main()
    add_documents(collection)
    # Check if documents are added
    all_items = collection.get()
    assert len(all_items['documents']) == len(texts)

def test_get_all_items():
    client = chromadb.Client()
    try:
        collection = client.get_collection(collection_name)
    except:
        collection = main()
        add_documents(collection)
    all_items = get_all_items(collection)
    assert 'documents' in all_items
    assert len(all_items['documents']) == len(texts)

def test_perform_similarity_search():
    client = chromadb.Client()
    try:
        collection = client.get_collection(collection_name)
    except:
        collection = main()
        add_documents(collection)
    results = perform_similarity_search(collection, "programming")
    assert results is not None
    assert 'documents' in results
    assert len(results['documents'][0]) > 0