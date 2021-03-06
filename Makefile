TAG := latest

help:
	@echo Available targets:
	@echo
	@grep '^\S\+:' Makefile \
		| grep -v .PHONY | \
		awk -F: '{ print $$1 }'

venv:
	(python3 -m venv venv \
		&& source venv/bin/activate \
		&& pip3 install -U pip \
		&& pip3 install -r requirements.txt)

build-image:
	docker build --no-cache -t vegadns/cli:${TAG} .

# Only check code we've written
check:
	pycodestyle vdns vegadns_cli vegadns_client integration_tests
clean: clean-python
	rm -rf venv
clean-python:
	find vegadns_client vegadns_cli -name "*.pyc" -exec rm -f {} \;
test-integration:
	nosetests integration_tests

upgrade-pip-packages: venv
	pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U
