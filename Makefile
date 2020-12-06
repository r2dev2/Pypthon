py = python3

.PHONY: test

test:
	$(py) -m pytest tests/
