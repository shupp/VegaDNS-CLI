from builtins import str
import click
import json
import logging

from vegadns_client.exceptions import ClientException
from vegadns_cli.common import records


logger = logging.getLogger(__name__)


@records.command()
@click.option(
    "--search-value",
    default=False,
    help="Optionally search by record values"
)
@click.option(
    "--search-name",
    default=False,
    help="Optionally search by record names"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def list(ctx, domain_id, search_name, search_value):
    """List all records for a domain"""
    try:
        collection = ctx.obj['client'].records(
            domain_id, search_name, search_value
        )
        records = []
        for record in collection:
            records.append(record.values)
        click.echo(json.dumps(records, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv4 address of the record to edit, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record to edit, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record to edit, required"
)
@click.pass_context
def edit_aptr(ctx, record_id, name, ip, ttl=3600):
    """Edit an A+PTR record"""
    try:
        data = {
            "record_type": "A+PTR",
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].record(record_id)
        r = record.edit(data)
        click.echo(json.dumps(r.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv4 address of the record to edit, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record to edit, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record to edit, required"
)
@click.pass_context
def edit_a(ctx, record_id, name, ip, ttl=3600):
    """Edit an A record"""
    try:
        data = {
            "record_type": "A",
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].record(record_id)
        r = record.edit(data)
        click.echo(json.dumps(r.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv4 address of the record to create, required"
)
@click.option(
    "--name",
    type=str,
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
def create_aptr(ctx, domain_id, name, ip, ttl=3600):
    """Create A+PTR record"""
    try:
        data = {
            "record_type": "A+PTR",
            "domain_id": domain_id,
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv4 address of the record to create, required"
)
@click.option(
    "--name",
    type=str,
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
def create_a(ctx, domain_id, name, ip, ttl=3600):
    """Create A record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
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
    help="IPv6 address, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="Record ID to edit, required"
)
@click.pass_context
def edit_aaaa(ctx, record_id, name, ip, ttl=3600):
    """Edit a AAAA record"""
    try:
        data = {
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv6 address of the record to create, required"
)
@click.option(
    "--name",
    type=str,
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
def create_aaaa(ctx, domain_id, name, ip, ttl=3600):
    """Create a AAAA record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
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
    help="IPv6 address, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="Record ID to edit, required"
)
@click.pass_context
def edit_aaaaptr(ctx, record_id, name, ip, ttl=3600):
    """Edit a AAAA+PTR record"""
    try:
        data = {
            "name": name,
            "value": ip,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--ip",
    type=str,
    prompt=True,
    help="IPv6 address of the record to create, required"
)
@click.option(
    "--name",
    type=str,
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
def create_aaaaptr(ctx, domain_id, name, ip, ttl=3600):
    """Create a AAAA+PTR record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the CNAME record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record to edit, required"
)
@click.pass_context
def edit_cname(ctx, record_id, name, value, ttl=3600):
    """Edit a CNAME record"""
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the CNAME record, required"
)
@click.option(
    "--name",
    type=str,
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
def create_cname(ctx, domain_id, name, value, ttl=3600):
    """Create a CNAME record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record, required"
)
@click.pass_context
def edit_ns(ctx, record_id, name, value, ttl=3600):
    """Edit an NS record"""
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
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
def create_ns(ctx, domain_id, name, value, ttl=3600):
    """Create an NS record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record, required"
)
@click.pass_context
def edit_txt(ctx, record_id, name, value, ttl=3600):
    """Edit a TXT record"""
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
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
def create_txt(ctx, domain_id, name, value, ttl=3600):
    """Create a TXT record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the record, defaults to 0"
)
@click.option(
    "--port",
    type=int,
    prompt=True,
    help="Port of the record, required"
)
@click.option(
    "--weight",
    type=int,
    prompt=True,
    help="Weight of the record, required"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record to create, required"
)
@click.pass_context
def edit_srv(ctx, record_id, name, value, weight, port, distance=0, ttl=3600):
    """Edit an SRV record"""
    try:
        data = {
            "name": name,
            "value": value,
            "weight": weight,
            "port": port,
            "distance": distance,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
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
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
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
def create_srv(ctx, domain_id, name, value, weight, port, distance=0,
               ttl=3600):
    """Create an SRV record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record, required"
)
@click.pass_context
def edit_spf(ctx, record_id, name, value, ttl=3600):
    """Edit an SPF record"""
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
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
def create_spf(ctx, domain_id, name, value, ttl=3600):
    """Create an SPF record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record, required"
)
@click.pass_context
def edit_ptr(ctx, record_id, name, value, ttl=3600):
    """Edit a PTR record"""
    try:
        data = {
            "name": name,
            "value": value,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record to create, defaults to 3600"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
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
def create_ptr(ctx, domain_id, name, value, ttl=3600):
    """Create a PTR record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
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
    """Edit an SOA record"""
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
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
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
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_soa(ctx, domain_id, email, nameserver, refresh=16374, retry=2048,
               expire=1048576, minimum=2560, serial=None, ttl=86400):
    """Create an SOA record (limit one per domain)"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--distance",
    type=int,
    prompt=False,
    help="Distance of the record, defaults to 0"
)
@click.option(
    "--value",
    type=str,
    prompt=True,
    help="Value of the record, required"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record, required"
)
@click.pass_context
def edit_mx(ctx, record_id, name, value, distance=0, ttl=3600):
    """Edit an MX record"""
    try:
        data = {
            "name": name,
            "value": value,
            "distance": distance,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
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
    type=str,
    prompt=True,
    help="Value of the record to create, required"
)
@click.option(
    "--name",
    type=str,
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
def create_mx(ctx, domain_id, name, value, distance=0, ttl=3600):
    """Create an MX record"""
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
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--flag",
    type=int,
    prompt=False,
    help="CAA Flag, defaults to 0"
)
@click.option(
    "--tag",
    type=click.Choice(['issue', 'issuewild', 'iodef']),
    prompt=True,
    help="Type of CAA tag: issue, issuewild, iodef"
)
@click.option(
    "--tag-value",
    type=str,
    prompt=True,
    help="Value of the CAA tag"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="ID of the record, required"
)
@click.pass_context
def edit_caa(ctx, record_id, name, tag, tag_value, flag=0, ttl=3600):
    """Edit a CAA record"""
    try:
        data = {
            "name": name,
            "tag": tag,
            "tagval": tag_value,
            "flag": flag,
            "ttl": ttl
        }
        r = ctx.obj['client'].record(record_id)
        record = r.edit(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--ttl",
    type=int,
    prompt=False,
    help="TTL of the record, defaults to 3600"
)
@click.option(
    "--flag",
    type=int,
    prompt=False,
    help="CAA Flag, defaults to 0"
)
@click.option(
    "--tag",
    type=click.Choice(['issue', 'issuewild', 'iodef']),
    prompt=True,
    help="Type of CAA tag: issue, issuewild, iodef"
)
@click.option(
    "--tag-value",
    type=str,
    prompt=True,
    help="Value of the CAA tag"
)
@click.option(
    "--name",
    type=str,
    prompt=True,
    help="Hostname of the record, required"
)
@click.option(
    "--domain-id",
    type=int,
    prompt=True,
    help="ID of the domain to list records for, required"
)
@click.pass_context
def create_caa(ctx, domain_id, name, tag, tag_value, flag=0, ttl=3600):
    """Create a CAA record"""
    try:
        data = {
            "record_type": "CAA",
            "domain_id": domain_id,
            "name": name,
            "tag": tag,
            "tagval": tag_value,
            "flag": flag,
            "ttl": ttl
        }
        record = ctx.obj['client'].records.create(data)
        click.echo(json.dumps(record.values, indent=4))
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)


@records.command()
@click.option(
    "--record-id",
    type=int,
    prompt=True,
    help="Record id"
)
@click.pass_context
def delete(ctx, record_id):
    """Delete a record"""
    try:
        r = ctx.obj['client'].record(record_id)
        r.delete()
    except ClientException as e:
        click.echo("Error: " + str(e.code))
        click.echo("Response: " + str(e.message))
        ctx.exit(1)
