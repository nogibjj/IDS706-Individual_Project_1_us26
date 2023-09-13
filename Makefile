install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	py.test --nbval *.ipynb

format:
	black_nbconvert *.ipynb

lint:
	nbqa ruff *.ipynb

all: install lint format test
