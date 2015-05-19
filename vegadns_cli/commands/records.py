import click
import json
import requests

from vegadns_cli.common import cli


@cli.command()
@click.option(
    "--domain_id",
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def list_records(ctx, domain_id):
    r = ctx.obj['client'].get("/records?domain_id=" + domain_id)
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return

    decoded = r.json()

    out = []
    for record in decoded['records']:
        if record['record_type'] != 'SOA':
            out.append(record)

    click.echo(json.dumps(out, indent=4))
