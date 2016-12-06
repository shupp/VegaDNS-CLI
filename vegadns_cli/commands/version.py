import click
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def version(ctx):
    """Display vdns and api versions"""
    try:
        api_version = ctx.obj['client'].release_version()
        click.echo("api version: " + api_version)
        click.echo("cli version: 2.0.0")
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
