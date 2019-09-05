from builtins import object
import dns
import dns.exception
import dns.resolver
import dns.reversename
import socket


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
        # if nameserver specified then try it first
        if ns_server:
            if not self.is_ipv4(ns_server):
                ns_server = socket.gethostbyname(ns_server)
            resolver = self.get_resolver(direct=True)
            resolver.nameservers = [ns_server]
            return resolver.query(hostname, record_type, tcp=False)
        else:
            # if it's not specified then use default nameserver
            return self.get_resolver().query(hostname, record_type, tcp=False)
