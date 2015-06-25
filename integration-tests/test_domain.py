import unittest
import os
import socket
import dns
import dns.exception
import dns.resolver
import dns.reversename
import socket

import vegadns_client


class TestDomain(unittest.TestCase):
    def setUp(self):
        k = "6d145840921dabcc85907bff35e607289abdad04b7900196ee45f5a4e12ac369"
        s = "b1163b6387318dbfebaca5740ddb024ad61fa18831bb887ea085036f8df9c180"
        h = "http://vegadns.docker:80"
        self.ns_server = "vegadns.docker"

        self.client = vegadns_client.client(k, s, h)
        self.remove_token_file()

    def tearDown(self):
        self.remove_token_file()

    def remove_token_file(self):
        # remove oauth access token storage file so it doesn't carry over
        # between runs
        try:
            os.remove(self.client._store.token_file)
        except OSError:
            # might not exist
            pass

    def test_create_domain(self):
        domain = self.client.domains.create("example.com")
        self.assertEquals("example.com", domain.values["domain"])

        # add soa manually for now
        data = {
            "record_type": "SOA",
            "domain_id": domain.values["domain_id"],
            "email": "hostmaster.example.com",
            "nameserver": "ns1.example.com",
            "refresh": 16374,
            "retry": 2048,
            "expire": 1048576,
            "minimum": 2560,
            "serial": None,
            "ttl": 86400
        }
        soa = self.client.records.create(data)
        self.assertEquals("hostmaster.example.com", soa.values["email"])

        # add ns records manually for now
        data = {
            "record_type": "NS",
            "domain_id": domain.values["domain_id"],
            "name": "example.com",
            "value": "ns1.example.com",
            "ttl": 3600
        }
        ns1 = self.client.records.create(data)
        self.assertEquals("ns1.example.com", ns1.values["value"])

        data = {
            "record_type": "NS",
            "domain_id": domain.values["domain_id"],
            "name": "example.com",
            "value": "ns2.example.com",
            "ttl": 3600
        }
        ns2 = self.client.records.create(data)
        self.assertEquals("ns2.example.com", ns2.values["value"])

        data = {
            "record_type": "A",
            "domain_id": domain.values["domain_id"],
            "name": "www.example.com",
            "value": "1.2.3.4",
            "ttl": 3600
        }
        www = self.client.records.create(data)
        self.assertEquals("www.example.com", www.values["name"])
        self.assertEquals("1.2.3.4", www.values["value"])

        # force tinydns update
        self.client.updatedata()

        # check DNS
        dnsclient = DNS()

        response = dnsclient.exec_query("www.example.com", "a", self.ns_server)
        records = []

        for record in response:
            records.append(record.to_text())

        self.assertEquals("1.2.3.4", records[0])


class DNS(object):
    DNS_CACHE_LIFE_SECONDS = 240.0
    DNS_TIMEOUT_SECONDS = 2.0         # timeout per DNS server
    DNS_LIFETIME_TIMEOUT_SECONDS = 1  # total timeout per DNS request
    PTR_CACHE_LEN = 512

    def is_ipv4(self, ipv4_address):
        try:
            socket.inet_aton(ipv4_address)
        except socket.error:
            return False
        return ipv4_address.count('.') == 3

    def get_resolver(self, direct=False):
        if direct:
            resolver = dns.resolver.Resolver(filename=None)
        else:
            resolver = dns.resolver.Resolver()

        resolver.timeout = self.DNS_TIMEOUT_SECONDS
        resolver.lifetime = self.DNS_LIFETIME_TIMEOUT_SECONDS

        return resolver

    def exec_query(self, hostname, record_type, ns_server=None):
        try:
            # if nameserver specified then try it first
            if ns_server:
                if not self.is_ipv4(ns_server):
                    ns_server = socket.gethostbyname(ns_server)
                resolver = self.get_resolver(direct=True)
                resolver.nameservers = [ns_server]
                try:
                    return resolver.query(hostname, record_type, tcp=False)
                except dns.exception.Timeout:
                    pass

            # if it's not specified or timed out then use default nameserver
            return get_resolver().query(hostname, record_type, tcp=False)

        # in case of timeouts and socket errors return []
        except dns.exception.Timeout:
            return []

        except socket.error:
            return []
