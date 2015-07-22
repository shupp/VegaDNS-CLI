import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import domains


logger = logging.getLogger(__name__)


def get_all_domains(ctx):
    collection = ctx.obj['client'].domains()
    domains = []
    for domain in collection:
        domains.append(domain.values)
    return domains


@domains.command()
@click.pass_context
def list(ctx):
    """List domains"""
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


@domains.command()
@click.option(
    "--domain",
    type=unicode,
    help="domain name"
)
@click.option(
    "--domain-id",
    type=int,
    help="ID of the domain, takes precedence"
)
@click.pass_context
def get(ctx, domain_id=None, domain=None):
    """Get a single domain"""
    try:
        if domain_id is not None:
            d = ctx.obj['client'].domain(domain_id)
            click.echo(json.dumps(d.values, indent=4))
            ctx.exit(0)

        if domain is None:
            domain = click.prompt('Please enter the domain name')

        domains = get_all_domains(ctx)
        for d in domains:
            if d["domain"] == domain:
                click.echo(json.dumps(d, indent=4))
                ctx.exit(0)

        # not found
        click.echo("Error: domain not found: " + domain)
        ctx.exit(1)
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@domains.command()
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
def edit(ctx, domain_id, owner_id, status):
    """Edit a domain"""
    try:
        d = ctx.obj['client'].domain(domain_id)
        d.edit(owner_id, status)
        click.echo(json.dumps(d.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@domains.command()
@click.option(
    "--domain",
    type=unicode,
    prompt=True,
    help="Domain name, required and must be unique"
)
@click.pass_context
def create(ctx, domain):
    """Create a new domain"""
    try:
        d = ctx.obj['client'].domains.create(domain)
        click.echo(json.dumps(d.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@domains.command()
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain, required"
)
@click.pass_context
def delete(ctx, domain_id):
    """Delete a domain"""
    try:
        d = ctx.obj['client'].domain(domain_id)
        d.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
