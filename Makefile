.PHONY: setup train infer api test lint format check

setup:
	pip install -r requirements.txt

train:
	python app/train.py

infer:
	python app/infer.py

api:
	uvicorn app.api:app --reload

test:
	python -m pytest

lint:
	python -m ruff check .

format:
	python -m black app

check:
	python -m ruff check .
	python -m black --check app
	python -m pytest
