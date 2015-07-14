import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli, config, configfile


@config.command()
@click.pass_context
def get(ctx):
    """Get the current config values"""
    environment = ctx.obj['environment']
    key = ctx.obj['config'].get(ctx.obj['environment'], 'key')
    secret = ctx.obj['config'].get(ctx.obj['environment'], 'secret')
    host = ctx.obj['config'].get(ctx.obj['environment'], 'host')

    click.echo("[" + environment + "]")
    click.echo("key=" + key)
    click.echo("secret=" + secret)
    click.echo("host=" + host)


@config.command()
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
def set(ctx, key, secret, host):
    """Set current config values"""
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
