.PHONY: install run test clean streamlit

install:
	pip install -r requirements.txt

run:
	python similarity_search.py

streamlit:
	python -m streamlit run app.py

test:
	pytest

clean:
	rm -rf __pycache__ .chroma