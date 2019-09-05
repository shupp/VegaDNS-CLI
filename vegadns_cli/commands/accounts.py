from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import accounts


logger = logging.getLogger(__name__)


@accounts.command()
@click.option(
    "--account-id",
    type=int,
    prompt=True,
    help="ID of the account, required"
)
@click.pass_context
def delete(ctx, account_id):
    """Delete an account"""
    try:
        a = ctx.obj['client'].account(account_id)
        a.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@accounts.command()
@click.option(
    "--password",
    type=str,
    prompt=True,
    hide_input=True,
    help="Clear text password, required"
)
@click.option(
    "--account-id",
    type=int,
    prompt=True,
    help="Account ID, required"
)
@click.pass_context
def set_password(ctx, account_id, password):
    """Set the password for an account"""
    try:
        a = ctx.obj['client'].account(account_id)
        data = {
            'first_name': a.values["first_name"],
            'last_name': a.values["last_name"],
            'email': a.values["email"],
            'account_type': a.values["account_type"],
            'phone': a.values["phone"],
            'status': a.values["status"],
            'password': password
        }
        account = a.edit(data)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@accounts.command()
@click.option(
    "--status",
    type=str,
    prompt=False,
    help="Account status, defaults to 'active'"
)
@click.option(
    "--phone",
    type=str,
    prompt=False,
    help="Phone number, optional"
)
@click.option(
    "--account-type",
    type=str,
    prompt=True,
    help="Account type, one of 'senior_admin' or 'user', required"
)
@click.option(
    "--email",
    type=str,
    prompt=True,
    help="Email address, required"
)
@click.option(
    "--last-name",
    type=str,
    prompt=True,
    help="Last Name, required"
)
@click.option(
    "--first-name",
    type=str,
    prompt=True,
    help="First Name, required"
)
@click.option(
    "--account-id",
    type=int,
    prompt=True,
    help="Account ID, required"
)
@click.pass_context
def edit(ctx, account_id, first_name, last_name,
         email, account_type, phone, status='active'):
    """Edit an account"""
    try:
        a = ctx.obj['client'].account(account_id)
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'account_type': account_type,
            'phone': phone,
            'status': status
        }
        account = a.edit(data)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@accounts.command()
@click.option(
    "--phone",
    type=str,
    prompt=False,
    help="Phone number, optional"
)
@click.option(
    "--password",
    type=str,
    prompt=True,
    help="Clear text password, required"
)
@click.option(
    "--account-type",
    type=str,
    prompt=True,
    help="Account type, one of 'senior_admin' or 'user', required"
)
@click.option(
    "--email",
    type=str,
    prompt=True,
    help="Email address, required"
)
@click.option(
    "--last-name",
    type=str,
    prompt=True,
    help="Last Name, required"
)
@click.option(
    "--first-name",
    type=str,
    prompt=True,
    help="First Name, required"
)
@click.pass_context
def create(ctx, first_name, last_name, email,
           account_type, password, phone):
    """Create an account"""
    try:
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'account_type': account_type,
            'password': password,
            'phone': phone
        }
        a = ctx.obj['client'].accounts.create(data)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@accounts.command()
@click.option(
    "--account-id",
    type=int,
    prompt=True,
    help="ID of the account, required"
)
@click.pass_context
def get(ctx, account_id):
    """Get a single account"""
    try:
        a = ctx.obj['client'].account(account_id)
        click.echo(json.dumps(a.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@accounts.command()
@click.option(
    "--search",
    default=False,
    help="Optionally search accounts"
)
@click.pass_context
def list(ctx, search):
    """List all accounts"""
    try:
        collection = ctx.obj['client'].accounts(search)
        accounts = []
        for account in collection:
            accounts.append(account.values)
        click.echo(json.dumps(accounts, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
