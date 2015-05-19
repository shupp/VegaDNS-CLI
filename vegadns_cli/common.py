import click
import httplib as http_client
from ConfigParser import SafeConfigParser
import logging
import os.path
import requests

from vegadns_cli.client import ApiClient, AccessToken


logger = logging.getLogger(__name__)

# Get config
configfile = os.path.expanduser('~/.vegadns-cli-rc')
config = SafeConfigParser()
config.read(configfile)


@click.group()
@click.option(
    "--environment",
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

    access_token = AccessToken(environment, config)

    ctx.obj['config'] = config
    ctx.obj['environment'] = environment
    ctx.obj['access_token'] = access_token.access_token
    ctx.obj['client'] = ApiClient(
        config.get(environment, 'host'),
        access_token.access_token
    )
