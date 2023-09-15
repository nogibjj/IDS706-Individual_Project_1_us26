install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	py.test --nbval *.ipynb

format:
	nbqa black *.ipynb
	black *.py

lint:
	nbqa ruff *.ipynb
	ruff check *.py

all: install lint format test
