from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import apikeys


logger = logging.getLogger(__name__)


@apikeys.command()
@click.option(
    "--apikey-id",
    type=int,
    prompt=True,
    help="ID of the api key, required"
)
@click.pass_context
def delete(ctx, apikey_id):
    """Delete an api key"""
    try:
        a = ctx.obj['client'].apikey(apikey_id)
        a.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@apikeys.command()
@click.option(
    "--description",
    type=str,
    prompt=True,
    help="Description"
)
@click.option(
    "--apikey-id",
    type=int,
    prompt=True,
    help="Account ID, required"
)
@click.pass_context
def edit(ctx, apikey_id, description):
    """Edit an api key's description"""
    try:
        a = ctx.obj['client'].apikey(apikey_id)
        data = {'description': description}
        apikey = a.edit(data)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@apikeys.command()
@click.option(
    "--account-id",
    type=int,
    prompt=False,
    help="Account ID"
)
@click.option(
    "--description",
    type=str,
    prompt=True,
    help="Description, required"
)
@click.pass_context
def create(ctx, description, account_id=None):
    """Create an api key"""
    try:
        data = {'description': description}
        if account_id is not None:
            data["account_id"] = account_id
        a = ctx.obj['client'].apikeys.create(data)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@apikeys.command()
@click.option(
    "--apikey-id",
    type=int,
    prompt=True,
    help="ID of the api key, required"
)
@click.pass_context
def get(ctx, apikey_id):
    """Get a single api key"""
    try:
        a = ctx.obj['client'].apikey(apikey_id)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@apikeys.command()
@click.option(
    "--account-ids",
    type=str,
    prompt=False,
    help=("Optional comma delimited list of account IDs to limit keys by, "
          "defaults to your own keys.")
)
@click.pass_context
def list(ctx, account_ids=None):
    """List api keys"""
    try:
        if account_ids is not None:
            collection = ctx.obj['client'].apikeys(account_ids=account_ids)
        else:
            collection = ctx.obj['client'].apikeys()

        apikeys = []
        for apikey in collection:
            apikeys.append(apikey.values)
        click.echo(json.dumps(apikeys, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
