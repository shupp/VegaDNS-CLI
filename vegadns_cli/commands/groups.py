import click
import json
import logging
import requests

from vegadns_cli.common import cli
from vegadns_client.exceptions import ClientException


logger = logging.getLogger(__name__)


@cli.command()
@click.option(
    "--group-id",
    prompt=True,
    help="Group id"
)
@click.pass_context
def get_group(ctx, group_id):
    try:
        g = ctx.obj['client'].group(group_id)
        click.echo(json.dumps(g.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        return


@cli.command()
@click.pass_context
def list_groups(ctx):
    try:
        collection = ctx.obj['client'].groups()
        groups = []
        for group in collection:
            groups.append(group.values)
        click.echo(json.dumps(groups, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        return


@cli.command()
@click.option(
    "--group-name",
    prompt=True,
    help="Group name to use, must be unique"
)
@click.pass_context
def create_group(ctx, group_name):
    try:
        g = ctx.obj['client'].groups.create(group_name)
        click.echo(json.dumps(g.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        return


@cli.command()
@click.option(
    "--group-name",
    prompt=True,
    help="Group name to use, must be unique"
)
@click.option(
    "--group-id",
    prompt=True,
    help="Group id"
)
@click.pass_context
def edit_group(ctx, group_id, group_name):
    r = ctx.obj['client'].put("/groups/" + group_id, {"name": group_name})
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        click.echo("Response: " + str(r.content))
        return

    decoded = r.json()

    click.echo(json.dumps(decoded["group"], indent=4))


@cli.command()
@click.option(
    "--group-id",
    prompt=True,
    help="Group id"
)
@click.pass_context
def delete_group(ctx, group_id):
    try:
        g = ctx.obj['client'].group(group_id)
        g.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        return
