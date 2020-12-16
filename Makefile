
.PHONY: build test install install-test upload upload-test

VENV_PY_VERSION ?= python3
VENV_NAME := .venv$(VENV_PY_VERSION)

PIP=pip3
PACKAGE_FORMATS=gztar

$(VENV_NAME) :
	virtualenv -p $(VENV_PY_VERSION) $@

virtualenv: $(VENV_NAME)
	@echo . $(VENV_NAME)/bin/activate

dist-build:
	rm -f dist/*
	python3 setup.py sdist --formats $(PACKAGE_FORMATS) bdist_wheel

install:
	$(VENV_PY_VERSION) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

install-test: install
	$(PIP) install -r testrequirements.txt

upload:
	python3 -m twine upload --repository pypi dist/*

upload-test:
	python3 -m twine upload --repository testpypi dist/*

test:
	trial src/tests/test_githubapi.py
