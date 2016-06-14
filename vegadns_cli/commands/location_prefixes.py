import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import location_prefixes


logger = logging.getLogger(__name__)


@location_prefixes.command()
@click.option(
    "--prefix-id",
    type=int,
    prompt=True,
    help="ID of the prefix to delete, required"
)
@click.pass_context
def delete(ctx, prefix_id):
    """Delete a location prefix"""
    try:
        l = ctx.obj['client'].location_prefix(prefix_id)
        l.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@location_prefixes.command()
@click.option(
    "--prefix-description",
    type=unicode,
    prompt=False,
    help="Preifx description, optional"
)
@click.option(
    "--prefix-type",
    type=unicode,
    prompt=False,
    default="ipv4",
    help="Prefix type, either 'ipv4' or 'ipv6', defaults to 'ipv4'"
)
@click.option(
    "--prefix",
    type=unicode,
    prompt=True,
    help="Prefix, e.g. '192.168.1', required"
)
@click.option(
    "--prefix-id",
    type=int,
    prompt=True,
    help="Location prefix ID, required"
)
@click.pass_context
def edit(ctx, prefix_id, prefix, prefix_type, prefix_description=None):
    """Edit a location prefix"""
    try:
        p = ctx.obj['client'].location_prefix(prefix_id)
        data = {
            'prefix': prefix,
            'prefix_type': prefix_type,
            'prefix_description': prefix_description
        }
        prefix = p.edit(data)
        click.echo(json.dumps(prefix.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@location_prefixes.command()
@click.option(
    "--prefix-description",
    type=unicode,
    prompt=False,
    help="Preifx description, optional"
)
@click.option(
    "--prefix-type",
    type=unicode,
    prompt=False,
    default="ipv4",
    help="Prefix type, either 'ipv4' or 'ipv6', required"
)
@click.option(
    "--prefix",
    type=unicode,
    prompt=True,
    help="Prefix, e.g. '192.168.1', required"
)
@click.option(
    "--location-id",
    type=int,
    prompt=True,
    help="Location ID, required"
)
@click.pass_context
def create(
    ctx, location_id, prefix, prefix_type="ipv4", prefix_description=None
):
    """Create a location network prefix"""
    try:
        data = {
            'location_id': location_id,
            'prefix': prefix,
            'prefix_type': prefix_type,
            'prefix_description': prefix_description
        }
        l = ctx.obj['client'].location_prefixes.create(data)
        click.echo(json.dumps(l.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@location_prefixes.command()
@click.option(
    "--prefix-id",
    type=int,
    prompt=True,
    help="ID of the prefix, required"
)
@click.pass_context
def get(ctx, prefix_id):
    """Get a single location prefix"""
    try:
        l = ctx.obj['client'].location_prefix(location_id)
        click.echo(json.dumps(l.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@location_prefixes.command()
@click.option(
    "--location-id",
    type=unicode,
    prompt=True,
    help=("Location id to list prefixes for, required")
)
@click.pass_context
def list(ctx, location_id=None):
    """List location prefixes for a location"""
    try:
        collection = ctx.obj['client'].location_prefixes(
            location_id=location_id
        )

        location_prefixes = []
        for prefix in collection:
            location_prefixes.append(prefix.values)
        click.echo(json.dumps(location_prefixes, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
