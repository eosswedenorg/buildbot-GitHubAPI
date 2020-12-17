
.PHONY: build install test dep-install dep-install-test upgrade-pip upload upload-test

VENV_PY_VERSION ?= python3
VENV_NAME := .venv$(VENV_PY_VERSION)

PYTHON := python
SETUPTOOLS := $(PYTHON) setup.py
TWINE := $(PYTHON) -m twine
TRIAL := trial
PIP=pip3
PACKAGE_FORMATS=gztar

$(VENV_NAME) :
	virtualenv -p $(VENV_PY_VERSION) $@

virtualenv: $(VENV_NAME)
	@echo . $(VENV_NAME)/bin/activate

build:
	$(SETUPTOOLS) build

install:
	$(SETUPTOOLS) install

dist-build:
	rm -f dist/*
	$(SETUPTOOLS) sdist --formats $(PACKAGE_FORMATS) bdist_wheel

upgrade-pip:
	$(PYTHON) -m pip install --upgrade pip

dep-install: upgrade-pip
	$(PIP) install -r requirements.txt

dep-install-test: upgrade-pip
	$(PIP) install -r requirements-test.txt

upload:
	$(TWINE) upload --repository pypi dist/*

upload-test:
	$(TWINE) upload --repository testpypi dist/*

test:
	$(SETUPTOOLS) install -f
	$(TRIAL) src/tests/test_githubapi.py
