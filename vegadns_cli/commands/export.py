import click
import json
import logging
import requests

from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def export(ctx):
    r = ctx.obj['client'].get("/export/tinydns")
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return
    click.echo(r.text)
