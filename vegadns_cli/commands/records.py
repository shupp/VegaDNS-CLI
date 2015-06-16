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
