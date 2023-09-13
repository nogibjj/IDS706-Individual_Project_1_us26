install:
	pip install --upgrade pip &&\
		pip install --prefer-binary -r requirements.txt

test:
	py.test --nbval *.ipynb

format:
	nbqa black *.ipynb

lint:
	nbqa ruff --fix *.ipynb

all: install lint format test
