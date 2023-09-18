install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:	
	py.test --nbval  \jupyter_notebook/*.ipynb
	python -m pytest \python_script/*.py 
	python -m pytest \src/*.py
	python -m pytest -vv --cov=lib

format:
	nbqa black  \jupyter_notebook/*.ipynb &&\
		black \python_script/*.py &&\
			black *.py

lint:
	nbqa ruff \jupyter_notebook/*.ipynb &&\
		ruff check \python_script/*.py &&\
			ruff check *.py

all: install test format lint
