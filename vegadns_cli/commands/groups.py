import click
import json
import logging
import requests

from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.option(
    "--group-id",
    prompt=True,
    help="Group id"
)
@click.pass_context
def get_group(ctx, group_id):
    r = ctx.obj['client'].get("/groups/" + group_id)
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return

    decoded = r.json()

    click.echo(json.dumps(decoded["group"], indent=4))


@cli.command()
@click.pass_context
def list_groups(ctx):
    r = ctx.obj['client'].get("/groups")
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return

    decoded = r.json()

    out = []
    for group in decoded['groups']:
        out.append(group)

    click.echo(json.dumps(out, indent=4))


@cli.command()
@click.option(
    "--group-name",
    prompt=True,
    help="Group name to use, must be unique"
)
@click.pass_context
def create_group(ctx, group_name):
    print group_name
    r = ctx.obj['client'].post("/groups", {"name": group_name})
    if r.status_code != 201:
        click.echo("Error: " + str(r.status_code))
        click.echo("Response: " + str(r.content))
        return

    decoded = r.json()

    click.echo(json.dumps(decoded["group"], indent=4))
