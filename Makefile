install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py test_files/test_*.py preprocess_SQL_files/*.py

lint:
	ruff check *.py test_files/test_*.py preprocess_SQL_files/*.py
	
test:
	python -m pytest -vv *.py test_files/test_*.py preprocess_SQL_files/*.py

check:
	python main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "test"; \
	git push; \


all: install lint format test 
