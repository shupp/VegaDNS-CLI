import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import cli


logger = logging.getLogger(__name__)


@cli.command()
@click.pass_context
def list_default_records(ctx):
    try:
        collection = ctx.obj['client'].default_records()
        default_records = []
        for default_record in collection:
            default_records.append(default_record.values)
        click.echo(json.dumps(default_records, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv4 address of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record to edit, required"
)
@click.pass_context
def edit_default_a_record(ctx, record_id, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "A",
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_record(record_id)
        r = record.edit(data)
        click.echo(json.dumps(r.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)


@cli.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv4 address of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_default_a_record(ctx, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "A",
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv6 address of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record to edit, required"
)
@click.pass_context
def edit_default_aaaa_record(ctx, record_id, name, ip, ttl=3600):
    try:
        data = {
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=unicode,
    prompt=True,
    help="IPv6 address of the default record to create, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record to create, required"
)
@click.pass_context
def create_default_aaaa_record(ctx, name, ip, ttl=3600):
    try:
        data = {
            "record_type": "AAAA",
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record to edit, required"
)
@click.pass_context
def edit_default_cname_record(ctx, record_id, name, value, ttl=3600):
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record to create, required"
)
@click.pass_context
def create_default_cname_record(ctx, name, value, ttl=3600):
    try:
        data = {
            "record_type": "CNAME",
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record, required"
)
@click.pass_context
def edit_default_ns_record(ctx, record_id, name, value, ttl=3600):
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record to create, required"
)
@click.pass_context
def create_default_ns_record(ctx, name, value, ttl=3600):
    try:
        data = {
            "record_type": "NS",
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record to edit, required"
)
@click.pass_context
def edit_default_txt_record(ctx, record_id, name, value, ttl=3600):
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_default_txt_record(ctx, name, value, ttl=3600):
    try:
        data = {
            "record_type": "TXT",
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the default record, defaults to 0"
)
@click.option(
    "--port",
    type=int,
    prompt=True,
    help="Port of the default record, required"
)
@click.option(
    "--weight",
    type=int,
    prompt=True,
    help="Weight of the default record, required"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record, required"
)
@click.pass_context
def edit_default_srv_record(ctx, record_id, name, value, weight,
                            port, distance=0, ttl=3600):
    try:
        data = {
            "name": name,
            "value": value,
            "weight": weight,
            "port": port,
            "distance": distance,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the default record, defaults to 0"
)
@click.option(
    "--port",
    type=int,
    prompt=True,
    help="Port of the default record, required"
)
@click.option(
    "--weight",
    type=int,
    prompt=True,
    help="Weight of the default record, required"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_default_srv_record(ctx, name, value, weight, port,
                              distance=0, ttl=3600):
    try:
        data = {
            "record_type": "SRV",
            "name": name,
            "value": value,
            "weight": weight,
            "port": port,
            "distance": distance,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record, required"
)
@click.pass_context
def edit_default_spf_record(ctx, record_id, name, value, ttl=3600):
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_default_spf_record(ctx, name, value, ttl=3600):
    try:
        data = {
            "record_type": "SPF",
            "name": name,
            "value": value,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL, defaults to 86400"
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
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the SOA record to edit, required"
)
@click.pass_context
def edit_default_soa_record(ctx, record_id, email, nameserver, refresh=16374,
                            retry=2048, expire=1048576, minimum=2560,
                            serial=None, ttl=86400):

    try:
        data = {
            "email": email,
            "nameserver": nameserver,
            "refresh": refresh,
            "retry": retry,
            "expire": expire,
            "minimum": minimum,
            "serial": serial,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record to create, defaults to 86400"
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
@click.pass_context
def create_default_soa_record(ctx, email, nameserver, refresh=16374,
                              retry=2048, expire=1048576, minimum=2560,
                              serial=None, ttl=86400):

    try:
        data = {
            "record_type": "SOA",
            "email": email,
            "nameserver": nameserver,
            "refresh": refresh,
            "retry": retry,
            "expire": expire,
            "minimum": minimum,
            "serial": serial,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the default record, defaults to 0"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the default record, required"
)
@click.pass_context
def edit_default_mx_record(ctx, record_id, name, value, distance=0, ttl=3600):
    try:
        data = {
            "name": name,
            "value": value,
            "distance": distance,
            "ttl": ttl
        }
        r = ctx.obj['client'].default_record(record_id)
        record = r.edit(data)
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
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the default record, defaults to 0"
)
@click.option(
    "--value",
    type=unicode,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=unicode,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_default_mx_record(ctx, name, value, distance=0, ttl=3600):
    try:
        data = {
            "record_type": "MX",
            "name": name,
            "value": value,
            "distance": distance,
            "ttl": ttl
        }
        record = ctx.obj['client'].default_records.create(data)
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
def delete_default_record(ctx, record_id):
    try:
        r = ctx.obj['client'].default_record(record_id)
        r.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + e.message)
        ctx.exit(1)
