# You'll need to source venv/bin/activate before running this file

default: check

venv:
	(virtualenv venv \
		&& source venv/bin/activate \
		&& pip install -r requirements.txt)

build-image:
	docker build --no-cache -t vegadns/cli .

# Only check code we've written
check:
	pep8 vdns vegadns_cli vegadns_client integration_tests
clean-python:
	find vegadns_client vegadns_cli -name "*.pyc" -exec rm {} \;
test-integration:
	nosetests integration_tests
