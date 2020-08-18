
.PHONY: build test upload upload-test

PACKAGE_FORMATS=gztar

dist-build:
	rm -f dist/*
	python3 setup.py sdist --formats $(PACKAGE_FORMATS) bdist_wheel

upload:
	python3 -m twine upload --repository pypi dist/*

upload-test:
	python3 -m twine upload --repository testpypi dist/*

test:
	trial src/tests/test_githubapi.py
