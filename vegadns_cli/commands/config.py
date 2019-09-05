import click
import json
import logging
import os
import stat

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli, config, configfile


@config.command()
@click.pass_context
def list(ctx):
    """List the config sections that can be used as environments"""
    environments = ctx.obj['config'].sections()
    environments.insert(0, 'default')

    for e in environments:
        key = ctx.obj['config'].get(e, 'key')
        secret = ctx.obj['config'].get(e, 'secret')
        host = ctx.obj['config'].get(e, 'host')

        click.echo("[" + e + "]")
        click.echo("key=" + key)
        click.echo("secret=" + secret)
        click.echo("host=" + host)
        click.echo("")


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
    """Check existing file permissions"""
    if os.path.exists(configfile):
        s = os.stat(configfile)
        if bool(s.st_mode & stat.S_IROTH):
            """Need to update permissions"""
            os.chmod(configfile, 0o600)

    with os.fdopen(
        os.open(configfile, os.O_WRONLY | os.O_CREAT, 0o600),
        'w'
    ) as f:
        c.write(f)

    click.echo("[" + environment + "]")
    click.echo("key = " + key)
    click.echo("secret = " + secret)
    click.echo("host = " + host)
