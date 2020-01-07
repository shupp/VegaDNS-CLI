from builtins import str
import click
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def export(ctx):
    """Export active domains in tinydns data format"""
    try:
        datafile = ctx.obj['client'].export(format="tinydns")
        click.echo(datafile)
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
