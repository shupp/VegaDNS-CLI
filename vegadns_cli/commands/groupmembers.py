from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import groupmembers


logger = logging.getLogger(__name__)


@groupmembers.command()
@click.option(
    "--group-id",
    type=int,
    prompt=True,
    help="ID of the group to list members for, required"
)
@click.pass_context
def list(ctx, group_id):
    """List members for a group"""
    try:
        collection = ctx.obj['client'].groupmembers(group_id)
        members = []
        for member in collection:
            members.append(member.values)
        click.echo(json.dumps(members, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@groupmembers.command()
@click.option(
    "--is-admin",
    type=int,
    prompt=False,
    default=0,
    help="Whether this user has admin privileges on the group. 1 = yes, 0 = no"
)
@click.option(
    "--account-id",
    type=int,
    prompt=True,
    help="ID of the account to add the group, required"
)
@click.option(
    "--group-id",
    type=int,
    prompt=True,
    help="ID of the group to list members for, required"
)
@click.pass_context
def add(ctx, group_id, account_id, is_admin):
    """Add a member to a group"""
    try:
        g = ctx.obj['client'].groupmembers.create(
            group_id, account_id, is_admin
        )
        click.echo(json.dumps(g.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@groupmembers.command()
@click.option(
    "--groupmember-id",
    type=int,
    prompt=True,
    help="ID of the group member to delete, required"
)
@click.pass_context
def delete(ctx, groupmember_id):
    """Delete a member from a group"""
    try:
        g = ctx.obj['client'].groupmember(groupmember_id)
        g.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@groupmembers.command()
@click.option(
    "--is-admin",
    type=int,
    prompt=False,
    default=0,
    help="Whether this use has admin privileges on the group.  1 = yes, 0 = no"
)
@click.option(
    "--groupmember-id",
    type=int,
    prompt=True,
    help="ID of the group member to delete, required"
)
@click.pass_context
def edit(ctx, groupmember_id, is_admin):
    """Edit a group member's admin status"""
    try:
        g = ctx.obj['client'].groupmember(groupmember_id)
        g.edit(is_admin)
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
