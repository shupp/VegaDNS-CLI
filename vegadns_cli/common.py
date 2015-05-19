import click
from ConfigParser import SafeConfigParser
import os.path

from vegadns_cli.client import ApiClient, AccessToken


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
@click.pass_context
def cli(ctx, environment):
    access_token = AccessToken(environment, config)

    ctx.obj['config'] = config
    ctx.obj['environment'] = environment
    ctx.obj['access_token'] = access_token.access_token
    ctx.obj['client'] = ApiClient(
        config.get(environment, 'host'),
        access_token.access_token
    )
