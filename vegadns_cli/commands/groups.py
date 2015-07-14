import click
import json
import logging
import requests

from vegadns_cli.common import groups
from vegadns_client.exceptions import ClientException


logger = logging.getLogger(__name__)


@groups.command()
@click.option(
    "--group-id",
    type=int,
    prompt=True,
    help="Group id"
)
@click.pass_context
def get(ctx, group_id):
    """Get a group"""
    try:
        g = ctx.obj['client'].group(group_id)
        click.echo(json.dumps(g.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@groups.command()
@click.pass_context
def list(ctx):
    """List groups"""
    try:
        collection = ctx.obj['client'].groups()
        groups = []
        for group in collection:
            groups.append(group.values)
        click.echo(json.dumps(groups, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@groups.command()
@click.option(
    "--group-name",
    type=unicode,
    prompt=True,
    help="Group name to use, must be unique"
)
@click.pass_context
def create(ctx, group_name):
    """Create a group"""
    try:
        g = ctx.obj['client'].groups.create(group_name)
        click.echo(json.dumps(g.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@groups.command()
@click.option(
    "--group-name",
    prompt=True,
    help="Group name to use, must be unique"
)
@click.option(
    "--group-id",
    type=int,
    prompt=True,
    help="Group id"
)
@click.pass_context
def edit(ctx, group_id, group_name):
    """Edit a group's name, which must be unique"""
    r = ctx.obj['client'].put("/groups/" + group_id, {"name": group_name})
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        click.echo("Response: " + str(r.content))
        ctx.exit(1)

    decoded = r.json()

    click.echo(json.dumps(decoded["group"], indent=4))


@groups.command()
@click.option(
    "--group-id",
    type=int,
    prompt=True,
    help="Group id"
)
@click.pass_context
def delete(ctx, group_id):
    """Delete a group"""
    try:
        g = ctx.obj['client'].group(group_id)
        g.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
