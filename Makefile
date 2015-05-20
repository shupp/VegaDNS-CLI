# You'll need to source venv/bin/activate before running this file

default: check

# Only check code we've written
check:
	pep8 vdns.py vegadns_cli vegadns_client
