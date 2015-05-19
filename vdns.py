import click
import requests
import json

from vegadns_cli.common import config, AccessToken, ApiClient, cli
from vegadns_cli.commands.domains import list_domains
from vegadns_cli.commands.records import list_records


if __name__ == "__main__":
    cli(obj={})
