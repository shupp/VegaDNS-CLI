from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import default_records


logger = logging.getLogger(__name__)


@default_records.command()
@click.pass_context
def list(ctx):
    """List default records"""
    try:
        collection = ctx.obj['client'].default_records()
        default_records = []
        for default_record in collection:
            default_records.append(default_record.values)
        click.echo(json.dumps(default_records, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv4 address of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_a(ctx, record_id, name, ip, ttl=3600):
    """Edit a default A record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv4 address of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_a(ctx, name, ip, ttl=3600):
    """Create a default A record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv6 address of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_aaaa(ctx, record_id, name, ip, ttl=3600):
    """Edit default AAAA record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv6 address of the default record to create, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record to create, required"
)
@click.pass_context
def create_aaaa(ctx, name, ip, ttl=3600):
    """Create default AAAA record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_cname(ctx, record_id, name, value, ttl=3600):
    """Edit default CNAME record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record to create, required"
)
@click.pass_context
def create_cname(ctx, name, value, ttl=3600):
    """Create default CNAME record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_ns(ctx, record_id, name, value, ttl=3600):
    """Edit default NS record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record to create, required"
)
@click.pass_context
def create_ns(ctx, name, value, ttl=3600):
    """Create default NS record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_txt(ctx, record_id, name, value, ttl=3600):
    """Edit default TXT record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_txt(ctx, name, value, ttl=3600):
    """Create default TXT record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
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
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_srv(ctx, record_id, name, value, weight, port, distance=0, ttl=3600):
    """Edit default SRV record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
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
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_srv(ctx, name, value, weight, port, distance=0, ttl=3600):
    """Create default SRV record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_spf(ctx, record_id, name, value, ttl=3600):
    """Edit default SPF record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the default record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_spf(ctx, name, value, ttl=3600):
    """Create default SPF record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
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
    type=str,
    prompt=True,
    help="Authority name server, i.e. ns1.example.com, required"
)
@click.option(
    "--email",
    type=str,
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
def edit_soa(ctx, record_id, email, nameserver, refresh=16374, retry=2048,
             expire=1048576, minimum=2560, serial=None, ttl=86400):
    """Edit default SOA record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
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
    type=str,
    prompt=True,
    help="Authority name server, i.e. ns1.example.com, required"
)
@click.option(
    "--email",
    type=str,
    prompt=True,
    help="Domain contact, i.e. hostmaster.example.com, required"
)
@click.pass_context
def create_soa(ctx, email, nameserver, refresh=16374, retry=2048,
               expire=1048576, minimum=2560, serial=None, ttl=86400):
    """Create default SOA record (limited to one)"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
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
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
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
def edit_mx(ctx, record_id, name, value, distance=0, ttl=3600):
    """Edit default MX record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
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
    type=str,
    prompt=True,
    help="Value of the default record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the default record, required"
)
@click.pass_context
def create_mx(ctx, name, value, distance=0, ttl=3600):
    """Create default MX record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@default_records.command()
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="Record id"
)
@click.pass_context
def delete(ctx, record_id):
    """Delete a default record"""
    try:
        r = ctx.obj['client'].default_record(record_id)
        r.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
