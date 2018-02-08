.PHONY: help
help:
	@echo Targets: test

.PHONY: start
start:
	@python -m magus_kalkulator

.PHONY: test
test: test2 test3

.PHONY: test2
test2:
	python -m pytest

.PHONY: test3
test3:
	python3 -m pytest

.PHONY: lint
lint:
	python3 -m pylint magus_kalkulator/*.py --disable=too-many-ancestors
	python3 -m pycodestyle magus_kalkulator/*.py
	python3 -m pylint tests/*.py --disable=too-many-ancestors
	python3 -m pycodestyle tests/*.py