.PHONY: mypy
mypy:
	poetry run mypy src

.PHONY: flake8
flake8:
	poetry run flake8 src tests

.PHONY: test
test:
	poetry run python -m unittest

.PHONY: test-all
test-all:
	$(MAKE) mypy
	$(MAKE) flake8
	$(MAKE) test
