.PHONY: help linter mypy test validate

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  help       to show this help"
	@echo "  test       to make tests running"
	@echo "  mypy       to make static type checking"
	@echo "  validate   to make source code validation"

linter:
	tox -e linter

mypy:
	tox -e mypy

test:
	@echo "Will be added after some refactoring"

validate:
	tox -e pre-commit
