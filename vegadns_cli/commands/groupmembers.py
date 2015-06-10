import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.option(
    "--group-id",
    prompt=True,
    help="ID of the group to list members for, required"
)
@click.pass_context
def list_groupmembers(ctx, group_id):
    try:
        collection = ctx.obj['client'].groupmembers(group_id)
        members = []
        for member in collection:
            members.append(member.values)
        click.echo(json.dumps(members, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--is-admin",
    prompt=False,
    default=0,
    help="Whether this use has admin privileges on the group.  1 = yes, 0 = no"
)
@click.option(
    "--account-id",
    prompt=True,
    help="ID of the account to add the group, required"
)
@click.option(
    "--group-id",
    prompt=True,
    help="ID of the group to list members for, required"
)
@click.pass_context
def add_groupmember(ctx, group_id, account_id, is_admin):
    try:
        g = ctx.obj['client'].groupmembers.create(
            group_id, account_id, is_admin
        )
        click.echo(json.dumps(g.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--groupmember-id",
    prompt=True,
    help="ID of the group member to delete, required"
)
@click.pass_context
def delete_groupmember(ctx, groupmember_id):
    try:
        g = ctx.obj['client'].groupmember(groupmember_id)
        g.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--is-admin",
    prompt=False,
    default=0,
    help="Whether this use has admin privileges on the group.  1 = yes, 0 = no"
)
@click.option(
    "--groupmember-id",
    prompt=True,
    help="ID of the group member to delete, required"
)
@click.pass_context
def edit_groupmember(ctx, groupmember_id, is_admin):
    try:
        g = ctx.obj['client'].groupmember(groupmember_id)
        g.edit(is_admin)
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
