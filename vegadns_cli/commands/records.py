import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def list_records(ctx, domain_id):
    try:
        collection = ctx.obj['client'].records(domain_id)
        records = []
        for record in collection:
            records.append(record.values)
        click.echo(json.dumps(records, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv4 address of the record to create, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_a_record(ctx, domain_id, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "A",
            "domain_id": domain_id,
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv6 address of the record to create, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_aaaa_record(ctx, domain_id, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "AAAA",
            "domain_id": domain_id,
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv6 address of the record to create, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_aaaaptr_record(ctx, domain_id, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "AAAA+PTR",
            "domain_id": domain_id,
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the CNAME record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_cname_record(ctx, domain_id, name, value, ttl=3600):
    try:
        data = {
            "record_type": "CNAME",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_ns_record(ctx, domain_id, name, value, ttl=3600):
    try:
        data = {
            "record_type": "NS",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_txt_record(ctx, domain_id, name, value, ttl=3600):
    try:
        data = {
            "record_type": "TXT",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the record to create, defaults to 0"
)
@click.option(
    "--port",
    type=int,
    prompt=True,
    help="Port of the record to create, required"
)
@click.option(
    "--weight",
    type=int,
    prompt=True,
    help="Weight of the record to create, required"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to create the record for, required"
)
@click.pass_context
def create_srv_record(ctx, domain_id, name, value, weight, port, distance=0, ttl=3600):
    try:
        data = {
            "record_type": "SRV",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "weight": weight,
            "port": port,
            "distance": distance,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to create the record for, required"
)
@click.pass_context
def create_spf_record(ctx, domain_id, name, value, ttl=3600):
    try:
        data = {
            "record_type": "SPF",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_ptr_record(ctx, domain_id, name, value, ttl=3600):
    try:
        data = {
            "record_type": "PTR",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 86400"
)
@click.option(
    "--serial",
    type=int,
    prompt=False,
    help="Custom serial number, defaults to none (autogenerated)"
)
@click.option(
    "--minimum",
    type=int,
    prompt=False,
    help="Minimum ttl, defaults to 2560"
)
@click.option(
    "--expire",
    type=int,
    prompt=False,
    help="Expire time, defaults to 1048576"
)
@click.option(
    "--retry",
    type=int,
    prompt=False,
    help="Retry time, defaults to 2048"
)
@click.option(
    "--refresh",
    type=int,
    prompt=False,
    help="Refresh time, defaults to 16374"
)
@click.option(
    "--nameserver",
    type=unicode,
    prompt=True,
    help="Authority name server, i.e. ns1.example.com, required"
)
@click.option(
    "--email",
    type=unicode,
    prompt=True,
    help="Domain contact, i.e. hostmaster.example.com, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_soa_record(ctx, domain_id, email, nameserver, refresh=16374,
                      retry=2048, expire=1048576, minimum=2560, serial=None,
                      ttl=86400):

    try:
        data = {
            "record_type": "SOA",
            "domain_id": domain_id,
            "email": email,
            "nameserver": nameserver,
            "refresh": refresh,
            "retry": retry,
            "expire": expire,
            "minimum": minimum,
            "serial": serial,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the record to create, defaults to 0"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the record to create, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the record to create, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_mx_record(ctx, domain_id, name, value, distance=0, ttl=3600):
    try:
        data = {
            "record_type": "MX",
            "domain_id": domain_id,
            "name": name,
            "value": value,
            "distance": distance,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="Record id"
)
@click.pass_context
def delete_record(ctx, record_id):
    try:
        r = ctx.obj['client'].record(record_id)
        r.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
