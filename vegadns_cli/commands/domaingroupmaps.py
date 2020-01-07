from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import domaingroupmaps


logger = logging.getLogger(__name__)


@domaingroupmaps.command()
@click.option(
    "--group-id",
    type=int,
    prompt=False,
    help="ID of the group to list domain maps for"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=False,
    help="ID of the domain to list group maps for"
)
@click.pass_context
def list(ctx, domain_id, group_id):
    """List maps for a domain group"""
    if domain_id is None and group_id is None:
        click.echo(
            "Error: you must provide either --domain-id or --group-id"
        )
        ctx.exit(1)

    try:
        collection = ctx.obj['client'].domaingroupmaps(domain_id, group_id)
        maps = []
        for map in collection:
            maps.append(map.values)
        click.echo(json.dumps(maps, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@domaingroupmaps.command()
@click.option(
    "--can-delete",
    prompt=False,
    type=int,
    default=1,
    help="Whether this group can delete the domain. 1 = yes, 0 = no"
)
@click.option(
    "--can-write",
    prompt=False,
    type=int,
    default=1,
    help="Whether this group can modify records. 1 = yes, 0 = no"
)
@click.option(
    "--can-read",
    prompt=False,
    type=int,
    default=1,
    help="Whether this group can read records. 1 = yes, 0 = no"
)
@click.option(
    "--group-id",
    type=int,
    prompt=True,
    help="ID of the group to add, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to add a group to, required"
)
@click.pass_context
def add(ctx, domain_id, group_id, can_read, can_write, can_delete):
    """Add a domain group map"""
    try:
        m = ctx.obj['client'].domaingroupmaps.create(
            domain_id, group_id, can_read, can_write, can_delete
        )
        click.echo(json.dumps(m.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@domaingroupmaps.command()
@click.option(
    "--map-id",
    type=int,
    prompt=True,
    help="ID of the domain group map, required"
)
@click.pass_context
def get(ctx, map_id):
    """Get a single domain group map"""
    try:
        m = ctx.obj['client'].domaingroupmap(map_id)
        click.echo(json.dumps(m.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@domaingroupmaps.command()
@click.option(
    "--map-id",
    type=int,
    prompt=True,
    help="ID of the domain group map to delete, required"
)
@click.pass_context
def delete(ctx, map_id):
    """Delete a domain group map"""
    try:
        m = ctx.obj['client'].domaingroupmap(map_id)
        m.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@domaingroupmaps.command()
@click.option(
    "--can-delete",
    type=int,
    prompt=False,
    default=1,
    help="Whether this group can delete the domain. 1 = yes, 0 = no"
)
@click.option(
    "--can-write",
    prompt=False,
    type=int,
    default=1,
    help="Whether this group can modify records. 1 = yes, 0 = no"
)
@click.option(
    "--can-read",
    prompt=False,
    type=int,
    default=1,
    help="Whether this group can read records. 1 = yes, 0 = no"
)
@click.option(
    "--map-id",
    prompt=True,
    type=int,
    help="ID of the domain group map to edit, required"
)
@click.pass_context
def edit(ctx, map_id, can_read, can_write, can_delete):
    """Edit a domain group map"""
    try:
        m = ctx.obj['client'].domaingroupmap(map_id)
        m.edit(can_read, can_write, can_delete)
        click.echo(json.dumps(m.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
