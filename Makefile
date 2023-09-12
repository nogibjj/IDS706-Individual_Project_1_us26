install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	python -m pytest -vv  test_*.ipynb

format:
	black *.ipynb

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?ipynb *.ipynb

all: install lint format test
