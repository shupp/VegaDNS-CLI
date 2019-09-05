from builtins import str
import click
import dns
import dns.resolver
import logging
from subprocess import call

from vegadns_cli.common import cli


@cli.command()
def upgrade():
    """Upgrade VegaDNS CLI client"""

    resolver = dns.resolver.Resolver()
    result = resolver.query("cli_upgrade_url.vegadns.org", "txt", tcp=False)
    url = str(result[0]).replace('"', "")
    call(["pip", "install", "--upgrade", url])
