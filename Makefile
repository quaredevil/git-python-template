CWD=$(shell pwd)
PKG=app

clean:
	find ./$(PKG) -name "*.pyc" -exec rm -rfv {} \;

test:
	tox -r

.PHONY: test clean
