PACKAGE_NAME=actions

.PHONY: tests install

install:
	pip install -r requirements.txt

tests:
	pytest tests/$(PACKAGE_NAME)

lint:
	black $(PACKAGE_NAME)
	black tests
