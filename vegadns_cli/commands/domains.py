import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def list_domains(ctx):
    try:
        collection = ctx.obj['client'].domains()
        domains = []
        for domain in collection:
            domains.append(domain.values)
        click.echo(json.dumps(domains, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain, required"
)
@click.pass_context
def get_domain(ctx, domain_id):
    try:
        d = ctx.obj['client'].domain(domain_id)
        click.echo(json.dumps(d.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--status",
    type=unicode,
    help="Domain status, can be 'active' or 'inactive'"
)
@click.option(
    "--owner-id",
    type=int,
    help="Account id of domain owner"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain, required"
)
@click.pass_context
def edit_domain(ctx, domain_id, owner_id, status):
    try:
        d = ctx.obj['client'].domain(domain_id)
        d.edit(owner_id, status)
        click.echo(json.dumps(d.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--domain",
    type=unicode,
    prompt=True,
    help="Domain name, required and must be unique"
)
@click.pass_context
def create_domain(ctx, domain):
    try:
        d = ctx.obj['client'].domains.create(domain)
        click.echo(json.dumps(d.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain, required"
)
@click.pass_context
def delete_domain(ctx, domain_id):
    try:
        d = ctx.obj['client'].domain(domain_id)
        d.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
