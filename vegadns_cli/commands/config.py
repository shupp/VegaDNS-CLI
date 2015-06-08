import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli, configfile


@cli.command()
@click.pass_context
def get_config(ctx):
    environment = ctx.obj['environment']
    key = ctx.obj['config'].get(ctx.obj['environment'], 'key')
    secret = ctx.obj['config'].get(ctx.obj['environment'], 'secret')
    host = ctx.obj['config'].get(ctx.obj['environment'], 'host')

    click.echo("[" + environment + "]")
    click.echo("key=" + key)
    click.echo("secret=" + secret)
    click.echo("host=" + host)


@cli.command()
@click.option(
    "--key",
    prompt=True,
    help="API key, required"
)
@click.option(
    "--secret",
    prompt=True,
    help="API secret, required"
)
@click.option(
    "--host",
    prompt=True,
    help="API host URL, required"
)
@click.pass_context
def set_config(ctx, key, secret, host):
    environment = ctx.obj['environment']

    c = ctx.obj['config']
    c.set(ctx.obj['environment'], 'key', key)
    c.set(ctx.obj['environment'], 'secret', secret)
    c.set(ctx.obj['environment'], 'host', host)
    f = open(configfile, 'w')
    c.write(f)

    click.echo("[" + environment + "]")
    click.echo("key = " + key)
    click.echo("secret = " + secret)
    click.echo("host = " + host)
