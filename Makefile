install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv  test_*.ipynb

format:
	black_nbconvert *.ipynb

lint:
	ruff check  *.ipynb

all: install lint format test
