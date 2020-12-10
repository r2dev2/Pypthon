py = python3

.PHONY: test

test:
	$(py) -m pytest tests/

install:
	$(py) setup.py install --user
