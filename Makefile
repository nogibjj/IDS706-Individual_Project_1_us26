install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:	
	python -m py.test --nbval Codes/jupyter_notebook/test_*.ipynb 
	python -m py.test -vv --cov=python_script Codes/python_script/*.py
	python -m py.test -vv --cov=lib

format:
	nbqa black  Codes/jupyter_notebook/*.ipynb &&\
		black Codes/python_script/*.py &&\
			black Codes/src/*.py

lint:
	nbqa ruff Codes/jupyter_notebook/*.ipynb &&\
		ruff check Codes/python_script/*.py &&\
			ruff check Codes/src/*.py

all: install test format lint
