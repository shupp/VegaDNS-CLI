import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def list_accounts(ctx):
    try:
        collection = ctx.obj['client'].accounts()
        accounts = []
        for account in collection:
            accounts.append(account.values)
        click.echo(json.dumps(accounts, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
