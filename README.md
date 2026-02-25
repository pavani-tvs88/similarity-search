# Similarity Search with ChromaDB

This project demonstrates similarity search using ChromaDB and Sentence Transformers. It allows users to search for similar tech-related topics from a predefined collection.

## Features

- Create and manage a ChromaDB collection with tech topics
- Perform similarity search on the collection
- Interactive query input
- Streamlit frontend for easy interaction

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pavani-tvs88/similarity-search.git
   cd similarity-search
   ```

2. Install dependencies:
   ```bash
   make install
   # or
   pip install -r requirements.txt
   ```

   Note: Installation may take time due to large ML models. For faster installs, consider using conda/mamba or a Docker image with pre-installed dependencies. You can also use `pip install --no-cache-dir` to avoid re-downloading.

## Usage

### Command Line

Run the script:
```bash
make run
# or
python similarity_search.py
```

Enter a query when prompted, e.g., "programming language".

#### Example Output
```
Enter a topic to search for: Python

Query: 'Python'
Top similar results:
1. Python programming language
2. Data science with Pandas
3. Machine learning with TensorFlow
```

### Streamlit App

Run the frontend:
```bash
make streamlit
# or
streamlit run app.py
```

Open the provided URL in your browser and enter queries. It has three tabs: Tech Topics Search, Document Search, and About. Use the sidebar slider to adjust the number of results (1-10).

#### Streamlit App Interface
- **Sidebar**: Slider for "Number of results to show" (default: 3)

- **Tech Topics Search Tab**:
  ```
  Enter a topic to search for: [programming language]
  [Search Tech Topics]
  
  Top similar results for 'programming language':
  1. Python programming language
  2. JavaScript for web development
  3. Data science with Pandas
  ```

- **Document Search Tab**:
  ```
  Paste your document text here: [Large text area for input]
  
  Enter a query to search in the document: [query here]
  [Search Document]
  
  Top similar sentences for 'query':
  1. Sentence matching the query.
  2. Another relevant sentence.
  ```

- **About Tab**:
  ```
  This app uses ChromaDB and Sentence Transformers for similarity search.
  Model: all-MiniLM-L6-v2
  Features: Search tech topics or custom documents.
  Number of tech topics: 14
  ```

Example: After entering "Python" in the Tech Topics tab and clicking search, you'll see results like the command-line example above.

### Testing

Run tests:
```bash
make test
# or
pytest
```

### Cleaning

Remove cache and data:
```bash
make clean
```

## Better Usage Ideas

- **Document Search**: Extend to search within uploaded documents or PDFs.
- **Q&A System**: Integrate with a knowledge base for question answering.
- **Recommendations**: Use for content recommendation based on user interests.
- **Multilingual Support**: Add support for multiple languages.

## Dependencies

- chromadb: Vector database
- sentence-transformers: For embeddings
- pytest: For testing
- streamlit: For frontend (optional)
