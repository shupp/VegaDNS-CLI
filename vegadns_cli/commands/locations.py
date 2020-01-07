from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import locations


logger = logging.getLogger(__name__)


@locations.command()
@click.option(
    "--location-id",
    type=int,
    prompt=True,
    help="ID location, required"
)
@click.pass_context
def delete(ctx, location_id):
    """Delete a location and its related network prefixes"""
    try:
        lo = ctx.obj['client'].location(location_id)
        lo.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@locations.command()
@click.option(
    "--location-description",
    type=str,
    help="Description"
)
@click.option(
    "--location",
    type=str,
    prompt=True,
    help="Two character location name, required"
)
@click.option(
    "--location-id",
    type=int,
    prompt=True,
    help="Account ID, required"
)
@click.pass_context
def edit(ctx, location_id, location, location_description=None):
    """Edit a location"""
    try:
        lo = ctx.obj['client'].location(location_id)
        data = {
            'location_description': location_description,
            'location': location
        }
        location = lo.edit(data)
        click.echo(json.dumps(location.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@locations.command()
@click.option(
    "--location",
    type=str,
    prompt=True,
    help="Two character location name, required"
)
@click.option(
    "--location-description",
    type=str,
    help="Description, optional"
)
@click.pass_context
def create(ctx, location, location_description=None):
    """Create a location"""
    try:
        data = {
            'location': location,
            'location_description': location_description,
        }
        lo = ctx.obj['client'].locations.create(data)
        click.echo(json.dumps(lo.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@locations.command()
@click.option(
    "--location-id",
    type=int,
    prompt=True,
    help="ID of the location, required"
)
@click.pass_context
def get(ctx, location_id):
    """Get a single location by id"""
    try:
        lo = ctx.obj['client'].location(location_id)
        click.echo(json.dumps(lo.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@locations.command()
@click.pass_context
def list(ctx):
    """List locations"""
    try:
        collection = ctx.obj['client'].locations()

        locations = []
        for location in collection:
            locations.append(location.values)
        click.echo(json.dumps(locations, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
