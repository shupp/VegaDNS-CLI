from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import audit_logs


logger = logging.getLogger(__name__)


@audit_logs.command()
@click.option(
    "--order",
    default="asc",
    help="Optionally order results asc or desc"
)
@click.option(
    "--sort",
    default=None,
    help="Optionally sort results by domain_id, log_id, or time"
)
@click.option(
    "--search",
    type=str,
    prompt=False,
    help=("Optional search string for log entry")
)
@click.option(
    "--domain-ids",
    type=str,
    prompt=False,
    help=("Optional comma delimited list of domain ids to filter logs by, "
          "defaults to all domains.")
)
@click.pass_context
def list(ctx, domain_ids=None, search=None, sort=None, order=None):
    """List audit logs"""
    try:
        collection = ctx.obj['client'].audit_logs(
            domain_ids=domain_ids, sort=sort, order=order, search=search
        )

        audit_logs = []
        for audit_log in collection:
            audit_logs.append(audit_log.values)
        click.echo(json.dumps(audit_logs, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
