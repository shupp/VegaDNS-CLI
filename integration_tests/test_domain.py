import unittest
import os
import dns.reversename
import time

import vegadns_client
from integration_tests.dns_client import DNS


class TestDomain(unittest.TestCase):
    def setUp(self):
        dk = "6d145840921dabcc85907bff35e607289abdad04b7900196ee45f5a4e12ac369"
        ds = "b1163b6387318dbfebaca5740ddb024ad61fa18831bb887ea085036f8df9c180"
        dh = "http://localhost:80"
        dn = "localhost"

        k = os.getenv("KEY", default=dk)
        s = os.getenv("SECRET", default=ds)
        h = os.getenv("HOST", default=dh)
        n = os.getenv("NAMESERVER", default=dn)

        self.ns_server = n
        self.client = vegadns_client.client(k, s, h)
        self.remove_token_file()

        self.domain = self.client.domains.create("example.com")
        self.ptrdomain = self.client.domains.create("in-addr.arpa")
        self.ip6ptrdomain = self.client.domains.create("ip6.arpa")

    def tearDown(self):
        self.domain.delete()
        self.ptrdomain.delete()
        self.ip6ptrdomain.delete()

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
        self.assertEquals("example.com", self.domain.values["domain"])

        # add ns records manually for now
        ns1 = self.client.records.create({
            "record_type": "NS",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "value": "ns1.example.com",
            "ttl": 3600
        })
        self.assertEquals("ns1.example.com", ns1.values["value"])

        ns1ptr = self.client.records.create({
            "record_type": "NS",
            "domain_id": self.ptrdomain.values["domain_id"],
            "name": "in-addr.arpa",
            "value": "ns1.example.com",
            "ttl": 3600
        })
        self.assertEquals("ns1.example.com", ns1ptr.values["value"])

        ns1ip6ptr = self.client.records.create({
            "record_type": "NS",
            "domain_id": self.ip6ptrdomain.values["domain_id"],
            "name": "ip6.arpa",
            "value": "ns1.example.com",
            "ttl": 3600
        })
        self.assertEquals("ns1.example.com", ns1ip6ptr.values["value"])

        # generic record tests
        # A
        www = self.client.records.create({
            "record_type": "A",
            "domain_id": self.domain.values["domain_id"],
            "name": "www.example.com",
            "value": "1.2.3.4",
            "ttl": 3600
        })
        self.assertEquals("www.example.com", www.values["name"])
        self.assertEquals("1.2.3.4", www.values["value"])

        # AAAA
        ipv6 = self.client.records.create({
            "record_type": "AAAA",
            "domain_id": self.domain.values["domain_id"],
            "name": "ipv6.example.com",
            "value": "FE80:0000:0000:0000:0202:B3FF:FE1E:8329",
            "ttl": 3600
        })
        self.assertEquals("ipv6.example.com", ipv6.values["name"])
        self.assertEquals(
            "FE80:0000:0000:0000:0202:B3FF:FE1E:8329",
            ipv6.values["value"]
        )

        # AAAA+PTR
        ipv6ptr = self.client.records.create({
            "record_type": "AAAA+PTR",
            "domain_id": self.domain.values["domain_id"],
            "name": "ipv6ptr.example.com",
            "value": "FE80:0000:0000:0000:0202:B3FF:FE1E:8330",
            "ttl": 3600
        })
        self.assertEquals("ipv6ptr.example.com", ipv6ptr.values["name"])
        self.assertEquals(
            "FE80:0000:0000:0000:0202:B3FF:FE1E:8330",
            ipv6ptr.values["value"]
        )

        # CNAME
        cname = self.client.records.create({
            "record_type": "CNAME",
            "domain_id": self.domain.values["domain_id"],
            "name": "cname.example.com",
            "value": "www.example.com",
            "ttl": 3600
        })
        self.assertEquals("cname.example.com", cname.values["name"])
        self.assertEquals("www.example.com", cname.values["value"])

        # MX
        mx = self.client.records.create({
            "record_type": "MX",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "value": "mail.example.com",
            "distance": 8,
            "ttl": 3600
        })
        self.assertEquals("example.com", mx.values["name"])
        self.assertEquals("mail.example.com", mx.values["value"])
        self.assertEquals("8", mx.values["distance"])

        # PTR
        ptr = self.client.records.create({
            "record_type": "PTR",
            "domain_id": self.ptrdomain.values["domain_id"],
            "name": "4.3.2.1.in-addr.arpa",
            "value": "www.example.com",
            "ttl": 3600
        })
        self.assertEquals("4.3.2.1.in-addr.arpa", ptr.values["name"])
        self.assertEquals("www.example.com", ptr.values["value"])

        # SPF
        spf = self.client.records.create({
            "record_type": "SPF",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "value": "v=spf1 mx a ptr",
            "ttl": 3600
        })
        self.assertEquals("example.com", spf.values["name"])
        self.assertEquals("v=spf1 mx a ptr", spf.values["value"])

        # SRV
        srv = self.client.records.create({
            "record_type": "SRV",
            "domain_id": self.domain.values["domain_id"],
            "name": "_xmpp-client._tcp.example.com",
            "value": "server.office.example.com",
            "distance": 11,
            "weight": 110,
            "port": 5222,
            "ttl": 3600
        })
        self.assertEquals("_xmpp-client._tcp.example.com", srv.values["name"])
        self.assertEquals("server.office.example.com", srv.values["value"])
        self.assertEquals("11", srv.values["distance"])
        self.assertEquals("110", srv.values["weight"])
        self.assertEquals("5222", srv.values["port"])

        # TXT
        txt = self.client.records.create({
            "record_type": "TXT",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "value": "v=spf1 mx a ptr",
            "ttl": 3600
        })
        self.assertEquals("example.com", txt.values["name"])
        self.assertEquals("v=spf1 mx a ptr", txt.values["value"])

        # CAA issue
        caa = self.client.records.create({
            "record_type": "CAA",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "flag": 0,
            "tagval": "digicert.com",
            "tag": "issue"
        })
        self.assertEquals("example.com", caa.values["name"])
        self.assertEquals(0, caa.values["flag"])
        self.assertEquals("digicert.com", caa.values["tagval"])
        self.assertEquals("issue", caa.values["tag"])

        # CAA issuewild
        caa_wild = self.client.records.create({
            "record_type": "CAA",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "flag": 0,
            "tagval": ";",
            "tag": "issuewild"
        })
        self.assertEquals("example.com", caa_wild.values["name"])
        self.assertEquals(0, caa_wild.values["flag"])
        self.assertEquals(";", caa_wild.values["tagval"])
        self.assertEquals("issuewild", caa_wild.values["tag"])
        caa_wild.delete()

        # CAA iodef
        caa_iodef = self.client.records.create({
            "record_type": "CAA",
            "domain_id": self.domain.values["domain_id"],
            "name": "example.com",
            "flag": 0,
            "tagval": "mailto:test@example.com",
            "tag": "iodef"
        })
        self.assertEquals("example.com", caa_iodef.values["name"])
        self.assertEquals("0", caa_iodef.values["flag"])
        self.assertEquals("mailto:test@example.com", caa_iodef.values["tagval"])
        self.assertEquals("iodef", caa_iodef.values["tag"])
        caa_iodef.delete()

        # wait for tinydns update
        time.sleep(1)

        # check DNS
        dnsclient = DNS()

        # A check
        response = dnsclient.exec_query("www.example.com", "a", self.ns_server)
        self.assertEquals("1.2.3.4", str(response[0]))

        # AAAA check
        response = dnsclient.exec_query(
            "ipv6.example.com", "aaaa", self.ns_server
        )
        self.assertEquals("fe80::202:b3ff:fe1e:8329", str(response[0]))

        # AAAA+PTR check
        addr = dns.reversename.from_address(
            "FE80:0000:0000:0000:0202:B3FF:FE1E:8330"
        )
        response = dnsclient.exec_query(addr, "ptr", self.ns_server)
        self.assertEquals("ipv6ptr.example.com.", str(response[0]))

        # CNAME check
        response = dnsclient.exec_query(
            "cname.example.com", "cname", self.ns_server
        )
        self.assertEquals("www.example.com.", str(response[0]))

        # MX check
        response = dnsclient.exec_query("example.com", "mx", self.ns_server)
        self.assertEquals("mail.example.com.", str(response[0].exchange))
        self.assertEquals("8", str(response[0].preference))

        # PTR check
        addr = dns.reversename.from_address("1.2.3.4")
        response = dnsclient.exec_query(addr, "ptr", self.ns_server)
        self.assertEquals("www.example.com.", str(response[0]))

        # SPF check
        response = dnsclient.exec_query("example.com", "spf", self.ns_server)
        self.assertEquals('"v=spf1 mx a ptr"', str(response[0]))

        # SRV check
        response = dnsclient.exec_query(
            "_xmpp-client._tcp.example.com", "srv", self.ns_server
        )
        self.assertEquals(
            "server.office.example.com.", str(response[0].target)
        )
        self.assertEquals("11", str(response[0].priority))
        self.assertEquals("110", str(response[0].weight))
        self.assertEquals("5222", str(response[0].port))

        # TXT check
        response = dnsclient.exec_query("example.com", "txt", self.ns_server)
        self.assertEquals('"v=spf1 mx a ptr"', str(response[0]))

        # CAA check
        response = dnsclient.exec_query("example.com", "type257", self.ns_server)
        # dnspython doesn't support CAA yet so use the hex output
        # 00 flag
        # 05 length
        # 6973737565 = issue
        # 64696769636572742e636f6d = digicert.com
        self.assertEquals("\\# 19 0005697373756564696769636572742e 636f6d", str(response[0]))

        # Make changes to records

        # A edit
        www_e = self.client.record(www.values["record_id"])
        www_new = www_e.edit({
            "name": "www.example.com",
            "value": "2.3.4.5",
            "ttl": 3600
        })
        self.assertEquals("www.example.com", www_new.values["name"])
        self.assertEquals("2.3.4.5", www_new.values["value"])

        # AAAA edit
        ipv6_e = self.client.record(ipv6.values["record_id"])
        ipv6_new = ipv6_e.edit({
            "name": "ipv6.example.com",
            "value": "FE80:0000:0000:0000:0202:B3FF:FE1E:8328",
            "ttl": 3600
        })
        self.assertEquals("ipv6.example.com", ipv6_new.values["name"])
        self.assertEquals(
            "FE80:0000:0000:0000:0202:B3FF:FE1E:8328",
            ipv6_new.values["value"]
        )

        # AAAA+PTR edit
        ipv6ptr_e = self.client.record(ipv6ptr.values["record_id"])
        ipv6ptr_new = ipv6ptr_e.edit({
            "name": "ipv6ptr_edit.example.com",
            "value": "FE80:0000:0000:0000:0202:B3FF:FE1E:8331",
            "ttl": 3600
        })
        self.assertEquals(
            "ipv6ptr_edit.example.com",
            ipv6ptr_new.values["name"]
        )
        self.assertEquals(
            "FE80:0000:0000:0000:0202:B3FF:FE1E:8331",
            ipv6ptr_new.values["value"]
        )

        # CNAME edit
        cname_e = self.client.record(cname.values["record_id"])
        cname_new = cname_e.edit({
            "name": "www2.example.com",
            "value": "www.example.com",
            "ttl": 3600
        })
        self.assertEquals("www2.example.com", cname_new.values["name"])
        self.assertEquals("www.example.com", cname_new.values["value"])

        # MX edit
        mx_e = self.client.record(mx.values["record_id"])
        mx_new = mx_e.edit({
            "name": "example.com",
            "value": "exchange.example.com",
            "distance": 10,
            "ttl": 3600
        })
        self.assertEquals("example.com", mx_new.values["name"])
        self.assertEquals("exchange.example.com", mx_new.values["value"])
        self.assertEquals("10", mx_new.values["distance"])

        # PTR edit
        ptr_e = self.client.record(ptr.values["record_id"])
        ptr_new = ptr_e.edit({
            "name": "5.4.3.2.in-addr.arpa",
            "value": "www.example.com",
            "ttl": 3600
        })
        self.assertEquals("5.4.3.2.in-addr.arpa", ptr_new.values["name"])
        self.assertEquals("www.example.com", ptr_new.values["value"])

        # SPF edit
        spf_e = self.client.record(spf.values["record_id"])
        spf_new = spf_e.edit({
            "name": "example.com",
            "value": "v=spf1 mx ptr",
            "ttl": 3600
        })
        self.assertEquals("example.com", spf_new.values["name"])
        self.assertEquals("v=spf1 mx ptr", spf_new.values["value"])

        # SRV edit
        srv_e = self.client.record(srv.values["record_id"])
        srv_new = srv_e.edit({
            "name": "_xmpp-client._tcp.example.com",
            "value": "server2.office.example.com",
            "distance": 20,
            "weight": 220,
            "port": 5223,
            "ttl": 3600
        })
        self.assertEquals(
            "_xmpp-client._tcp.example.com", srv_new.values["name"]
        )
        self.assertEquals(
            "server2.office.example.com", srv_new.values["value"]
        )
        self.assertEquals("20", srv_new.values["distance"])
        self.assertEquals("220", srv_new.values["weight"])
        self.assertEquals("5223", srv_new.values["port"])

        # TXT
        txt_e = self.client.record(txt.values["record_id"])
        txt_new = txt_e.edit({
            "name": "example.com",
            "value": "v=spf1 mx ptr",
            "ttl": 3600
        })
        self.assertEquals("example.com", txt_new.values["name"])
        self.assertEquals("v=spf1 mx ptr", txt_new.values["value"])

        caa_e = self.client.record(caa.values["record_id"])
        caa_new = caa_e.edit({
            "name": "example.com",
            "flag": 0,
            "tagval": "letsencrypt.com",
            "tag": "issue"
        })

        # wait for tinydns update
        time.sleep(1)

        # A edit check
        response = dnsclient.exec_query("www.example.com", "a", self.ns_server)
        self.assertEquals("2.3.4.5", str(response[0]))

        # AAAA edit check
        response = dnsclient.exec_query(
            "ipv6.example.com", "aaaa", self.ns_server
        )
        self.assertEquals("fe80::202:b3ff:fe1e:8328", str(response[0]))

        # AAAA+PTR check
        addr = dns.reversename.from_address(
            "FE80:0000:0000:0000:0202:B3FF:FE1E:8331"
        )
        response = dnsclient.exec_query(addr, "ptr", self.ns_server)
        self.assertEquals("ipv6ptr_edit.example.com.", str(response[0]))

        # CNAME edit check
        response = dnsclient.exec_query(
            "www2.example.com", "cname", self.ns_server
        )
        self.assertEquals("www.example.com.", str(response[0]))

        # MX edit check
        response = dnsclient.exec_query(
            "example.com", "mx", self.ns_server
        )
        self.assertEquals("exchange.example.com.", str(response[0].exchange))
        self.assertEquals("10", str(response[0].preference))

        # PTR edit check
        addr = dns.reversename.from_address("2.3.4.5")
        response = dnsclient.exec_query(addr, "ptr", self.ns_server)
        self.assertEquals("www.example.com.", str(response[0]))

        # SPF edit check
        response = dnsclient.exec_query("example.com", "spf", self.ns_server)
        self.assertEquals('"v=spf1 mx ptr"', str(response[0]))

        # SRV edit check
        response = dnsclient.exec_query(
            "_xmpp-client._tcp.example.com", "srv", self.ns_server
        )
        self.assertEquals(
            "server2.office.example.com.", str(response[0].target)
        )
        self.assertEquals("20", str(response[0].priority))
        self.assertEquals("220", str(response[0].weight))
        self.assertEquals("5223", str(response[0].port))

        # TXT edit check
        response = dnsclient.exec_query("example.com", "txt", self.ns_server)
        self.assertEquals('"v=spf1 mx ptr"', str(response[0]))

        response = dnsclient.exec_query("example.com", "type257", self.ns_server)
        self.assertEquals('\\# 22 000569737375656c657473656e637279 70742e636f6d', str(response[0]))
