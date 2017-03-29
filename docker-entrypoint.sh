#!/usr/local/bin/dumb-init /bin/bash
set -e

cd /opt/vegadns-cli && nosetests integration_tests
