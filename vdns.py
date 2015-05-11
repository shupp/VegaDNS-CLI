import click
import requests


@click.group()
@click.option(
    "--email",
    prompt=True,
    help="Email, required"
)
@click.password_option(
    "--password",
    confirmation_prompt=False,
    help="Password, required"
)
@click.option(
    "--host",
    default="http://localhost:5000",
    help="API Base URL, defaults to http://localhost:5000"
)
@click.pass_context
def cli(ctx, host, email, password):
    ctx.obj['host'] = host
    ctx.obj['email'] = email
    ctx.obj['password'] = password


@cli.command()
@click.pass_context
def list_domains(ctx):
    r = requests.get(
        ctx.obj['host'] + "/domains",
        auth=(ctx.obj['email'], ctx.obj['password'])
    )
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return

    decoded = r.json()
    for domain in decoded['domains']:
        click.echo(domain['domain'])


@cli.command()
@click.option(
    "--domain",
    prompt=True,
    help="Domain to list records for, required"
)
@click.pass_context
def list_records(ctx, domain):
    r = requests.get(
        ctx.obj['host'] + "/records?domain_id=" + domain,
        auth=(ctx.obj['email'], ctx.obj['password'])
    )
    if r.status_code != 200:
        click.echo("Error: " + str(r.status_code))
        return

    decoded = r.json()
    for record in decoded['records']:
        if record['record_type'] != 'SOA':
            click.echo(record['name'])

if __name__ == "__main__":
    cli(obj={})
