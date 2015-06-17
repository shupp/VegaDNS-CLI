import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def list_records(ctx, domain_id):
    try:
        collection = ctx.obj['client'].records(domain_id)
        records = []
        for record in collection:
            records.append(record.values)
        click.echo(json.dumps(records, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv4 address of the record to create, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_a_record(ctx, domain_id, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "A",
            "domain_id": domain_id,
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="Record id"
)
@click.pass_context
def delete_record(ctx, record_id):
    try:
        r = ctx.obj['client'].record(record_id)
        r.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
