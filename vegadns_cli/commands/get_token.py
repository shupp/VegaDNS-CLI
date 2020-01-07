from __future__ import print_function
from __future__ import division
from builtins import str
from past.utils import old_div
import click
import json
import logging
import time
import math
import json as jsonlib

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.option(
    "--json",
    is_flag=True,
    help="Optional json formatting of output"
)
@click.pass_context
def get_token(ctx, json):
    """Gets the current oauth token and expiration time for use with swagger"""
    try:
        token = ctx.obj['client'].get_access_token()
        expires_at = ctx.obj['client'].get_access_token_expires_at()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)

    if json:
        values = {
            'token': token,
            'expires_at': expires_at
        }
        click.echo(jsonlib.dumps(values, indent=4))
    else:
        if expires_at is not None:
            # date = datetime.datetime.fromtimestamp(expires_at)
            now = int(time.time())
            seconds_left = expires_at - now
            minutes = int(math.floor(old_div(seconds_left, 60)))
            seconds = int(seconds_left - (minutes * 60))
            expires_at = (
                str(minutes) + " minutes and " + str(seconds) + " seconds"
            )

        print("Token:      " + token)
        print("Expires in: " + str(expires_at))
