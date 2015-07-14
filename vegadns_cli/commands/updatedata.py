import click
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def update_data(ctx):
    """Update tinydns data (local to VegaDNS only)"""
    try:
        output = ctx.obj['client'].updatedata()
        click.echo(output)
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
