import streamlit as st
import chromadb
from chromadb.utils import embedding_functions
from similarity_search import main, add_documents, perform_similarity_search, search_in_document

st.title("Tech Similarity Search")

# Initialize collection
if 'collection' not in st.session_state:
    st.session_state.collection = main()
    if st.session_state.collection:
        add_documents(st.session_state.collection)

# Slider for number of results
n_results = st.sidebar.slider("Number of results to show", min_value=1, max_value=10, value=3)

tab1, tab2, tab3 = st.tabs(["Tech Topics Search", "Document Search", "About"])

with tab1:
    st.header("Search in Tech Topics")
    query = st.text_input("Enter a topic to search for:", "programming language", key="tech_query")
    if st.button("Search Tech Topics"):
        if st.session_state.collection:
            results = perform_similarity_search(st.session_state.collection, query, n_results)
            if results:
                st.write(f"Top similar results for '{query}':")
                for i, doc in enumerate(results['documents'][0]):
                    st.write(f"{i+1}. {doc}")
        else:
            st.error("Failed to initialize collection.")

with tab2:
    st.header("Search in a Document")
    document = st.text_area("Paste your document text here:")
    doc_query = st.text_input("Enter a query to search in the document:", key="doc_query")
    if st.button("Search Document"):
        if document and doc_query:
            results = search_in_document(document, doc_query, n_results)
            if results:
                st.write(f"Top similar sentences for '{doc_query}':")
                for i, doc in enumerate(results['documents'][0]):
                    st.write(f"{i+1}. {doc}")
        else:
            st.error("Please provide both document text and query.")

with tab3:
    st.header("About")
    st.write("This app uses ChromaDB and Sentence Transformers for similarity search.")
    st.write("Model: all-MiniLM-L6-v2")
    st.write("Features: Search tech topics or custom documents.")
    st.write(f"Number of tech topics: {len(st.session_state.collection.get()['documents']) if st.session_state.collection else 0}")