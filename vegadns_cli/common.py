import click
import httplib as http_client
import ConfigParser
import logging
import os.path
import requests

from vegadns_client import client
from vegadns_client.store.file import AccessTokenStoreFile


logger = logging.getLogger(__name__)

# Use 'default' instead of 'DEFAULT'
ConfigParser.DEFAULTSECT = 'default'

# Set config defaults, get config file
configfile = os.path.expanduser('~/.vegadns-cli-rc')
config = ConfigParser.SafeConfigParser(
    {"key": "", "secret": "", "host": "http://localhost:5000"}
)
config.read(configfile)


@click.group()
@click.option(
    "--environment",
    "-e",
    default="default",
    help="Which environment config to use, default is 'default'"
)
@click.option("--debug", "-d", is_flag=True, help="Enables debug logs")
@click.pass_context
def cli(ctx, environment, debug=False):
    if debug:
        http_client.HTTPConnection.debuglevel = 1

        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)

        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    # manage config
    if environment != 'default' and environment not in config.sections():
        config.add_section(environment)

    key = config.get(environment, 'key')
    secret = config.get(environment, 'secret')
    host = config.get(environment, 'host')

    ctx.obj['config'] = config
    ctx.obj['environment'] = environment

    config_commands = ['set_config', 'get_config']
    if ctx.invoked_subcommand not in config_commands:
        store = AccessTokenStoreFile(
            key,
            secret,
            host,
            prefix=".vegadns-access-token-" + environment + "-"
        )
        ctx.obj['client'] = client(key, secret, host, store)
