from future import standard_library
standard_library.install_aliases()
import click
import http.client as http_client
import configparser
import logging
import os.path
import requests

from vegadns_client import client
from vegadns_client.store.file import AccessTokenStoreFile


logger = logging.getLogger(__name__)

# Use 'default' instead of 'DEFAULT'
configparser.DEFAULTSECT = 'default'

# Set config defaults, get config file
configfile = os.path.expanduser('~/.vegadns-cli-rc')
config_obj = configparser.SafeConfigParser(
    {"key": "", "secret": "", "host": "http://localhost:5000"}
)
config_obj.read(configfile)


@click.group()
@click.option(
    "--environment",
    "-e",
    default="default",
    help="Which environment config to use, default is 'default'"
)
@click.option("--debug", "-d", is_flag=True, help="Enables HTTP debug logs")
@click.pass_context
def cli(ctx, environment, debug=False):
    """A command line interface for managing VegaDNS"""
    if debug:
        http_client.HTTPConnection.debuglevel = 1

        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)

        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    # manage config
    if environment != 'default' and environment not in config_obj.sections():
        config_obj.add_section(environment)

    key = config_obj.get(environment, 'key')
    secret = config_obj.get(environment, 'secret')
    host = config_obj.get(environment, 'host')

    ctx.obj['config'] = config_obj
    ctx.obj['environment'] = environment

    local_commands = ['config', 'upgrade']
    if ctx.invoked_subcommand not in local_commands:
        store = AccessTokenStoreFile(
            key,
            secret,
            host,
            prefix=".vegadns-access-token-" + environment + "-"
        )
        ctx.obj['client'] = client(key, secret, host, store)


@click.group()
@click.pass_context
def domains(ctx):
    """Manage domains"""
    pass

cli.add_command(domains)


@click.group()
@click.pass_context
def records(ctx):
    """Manage a domain's records"""
    pass

cli.add_command(records)


@click.group()
@click.pass_context
def default_records(ctx):
    """Manage default records"""
    pass

cli.add_command(default_records)


@click.group()
@click.pass_context
def config(ctx):
    """Manage the config for the current environment"""
    pass

cli.add_command(config)


@click.group()
@click.pass_context
def accounts(ctx):
    """Manage accounts"""
    pass

cli.add_command(accounts)


@click.group()
@click.pass_context
def domaingroupmaps(ctx):
    """Manage domain to group mappings/permissions"""
    pass

cli.add_command(domaingroupmaps)


@click.group()
@click.pass_context
def groups(ctx):
    """Manage groups"""
    pass

cli.add_command(groups)


@click.group()
@click.pass_context
def groupmembers(ctx):
    """Manage group members"""
    pass

cli.add_command(groupmembers)


@click.group()
@click.pass_context
def apikeys(ctx):
    """Manage account api keys"""
    pass

cli.add_command(apikeys)


@click.group()
@click.pass_context
def locations(ctx):
    """Manage locations"""
    pass

cli.add_command(locations)


@click.group()
@click.pass_context
def location_prefixes(ctx):
    """Manage location network prefixes"""
    pass

cli.add_command(location_prefixes)


@click.group()
@click.pass_context
def audit_logs(ctx):
    """List audit logs"""
    pass

cli.add_command(audit_logs)
