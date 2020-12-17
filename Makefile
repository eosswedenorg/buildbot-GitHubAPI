
.PHONY: build test install install-test upgrade-pip upload upload-test

VENV_PY_VERSION ?= python3
VENV_NAME := .venv$(VENV_PY_VERSION)

PYTHON := python
TRIAL := trial
PIP=pip3
PACKAGE_FORMATS=gztar

$(VENV_NAME) :
	virtualenv -p $(VENV_PY_VERSION) $@

virtualenv: $(VENV_NAME)
	@echo . $(VENV_NAME)/bin/activate

dist-build:
	rm -f dist/*
	$(PYTHON) setup.py sdist --formats $(PACKAGE_FORMATS) bdist_wheel

upgrade-pip:
	$(PYTHON) -m pip install --upgrade pip

install: upgrade-pip
	$(PIP) install -r requirements.txt

install-test: upgrade-pip
	$(PIP) install -r requirements-test.txt

upload:
	$(PYTHON) -m twine upload --repository pypi dist/*

upload-test:
	$(PYTHON) -m twine upload --repository testpypi dist/*

test:
	$(TRIAL) src/tests/test_githubapi.py
