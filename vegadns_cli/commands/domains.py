import click
import json
import logging
import requests

from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def list_domains(ctx):
    r = ctx.obj['client'].get("/domains")
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return
    decoded = r.json()
    click.echo(json.dumps(decoded['domains'], indent=4))
