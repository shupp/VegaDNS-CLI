# VegaDNS CLI

VegaDNS CLI is a command line interface for the [VegaDNS 2 API](https://github.com/shupp/VegaDNS/tree/python-api) written in python.  It is comprised of a thin REST wrapper with [OAuth2 section 4.4](https://tools.ietf.org/html/rfc6749#section-4.4) support, vegadns_client, and a [Click](http://click.pocoo.org/5/) based cli wrapper vegadns_cli.

## Installation and upgrades

Installation should through [pip](https://pip.pypa.io/en/stable/).  For a first time global installation, you can do the following:

```
sudo pip install https://github.com/shupp/VegaDNS/archive/vegadns-cli.zip
```

For subsequent updates, you can use the builtin _upgrade_ command:

```
sudo vdns upgrade
```

## Configuring

To connect to your VegaDNS2 API, you'll need to set the host url, your api key, and api secret.

### From a brand new api install
For a brand new installation, you can start with the seeded account information and change it later when you create accounts:

```
vdns config set --host <your_api_url> \
    --key 6d145840921dabcc85907bff35e607289abdad04b7900196ee45f5a4e12ac369 \
    --secret b1163b6387318dbfebaca5740ddb024ad61fa18831bb887ea085036f8df9c180
```

### From email/password
If you need to first create api keys from a given email/password, you can currently use curl and basic auth to generate the keys:

```
curl -X POST -u <email>:<password> <api_host>/1.0/apikeys
```
In the response JSON response you'll see a _key_ and _secret_.  Use those values and follow the _config set_ example above.

## Using the _vdns_ cli tool

The vdns tool should be pretty self explanatory.  Too see the list of commands available, you can call it without any arguments:

```
$ vdns
Usage: vdns [OPTIONS] COMMAND [ARGS]...

  A command line interface for managing VegaDNS

Options:
  -e, --environment TEXT  Which environment config to use, default is
                          'default'
  -d, --debug             Enables HTTP debug logs
  --help                  Show this message and exit.

Commands:
  accounts         Manage accounts
  apikeys          Manage account api keys
  config           Manage the config for the current environment
  default_records  Manage default records
  domaingroupmaps  Manage domain to group mappings/permissions
  domains          Manage domains
  export           Export active domains in tinydns data format
  groupmembers     Manage group members
  groups           Manage groups
  records          Manage a domain's records
  update_data      Update tinydns data (local to VegaDNS only)
  upgrade          Upgrade VegaDNS CLI client
  ```
As you can see, if you work with multiple VegaDNS2 installations, you can use _-e <environment>_ as a global argument to all commands specify which api to talk to.  The default is _default_.

Note that you can always use _--help_ with any command to see its usage:

```
$ vdns records --help
Usage: vdns records [OPTIONS] COMMAND [ARGS]...

  Manage a domain's records

Options:
  --help  Show this message and exit.

Commands:
  create_a        Create A record
  create_aaaa     Create a AAAA record
  create_aaaaptr  Create a AAAA+PTR record
  create_aptr     Create A+PTR record
  create_cname    Create a CNAME record
  create_mx       Create an MX record
  create_ns       Create an NS record
  create_ptr      Create a PTR record
  create_soa      Create an SOA record (limit one per domain)
  create_spf      Create an SPF record
  create_srv      Create an SRV record
  create_txt      Create a TXT record
  delete          Delete a record
  edit_a          Edit an A record
  edit_aaaa       Edit a AAAA record
  edit_aaaaptr    Edit a AAAA+PTR record
  edit_aptr       Edit an A+PTR record
  edit_cname      Edit a CNAME record
  edit_mx         Edit an MX record
  edit_ns         Edit an NS record
  edit_ptr        Edit a PTR record
  edit_soa        Edit an SOA record
  edit_spf        Edit an SPF record
  edit_srv        Edit an SRV record
  edit_txt        Edit a TXT record
  list            List all records for a domain
```

```
$ vdns accounts --help
Usage: vdns accounts [OPTIONS] COMMAND [ARGS]...

  Manage accounts

Options:
  --help  Show this message and exit.

Commands:
  create        Create an account
  delete        Delete an account
  edit          Edit an account
  get           Get a single account
  list          List all accounts
  set_password  Set the password for an account
```

While some argumens can be omitted resulting in a prompt for their values, you'll likely find the most success by knowing the arguments you need, and being explicit.

## Support
For support or feedback, please use [GitHub issues](https://github.com/shupp/VegaDNS/issues)
