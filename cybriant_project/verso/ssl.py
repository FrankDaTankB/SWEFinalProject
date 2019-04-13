# Python 3.5.2-slim

import json
import re
import sys
import argparse
from ipwhois import IPWhois
from itertools import product
import socket
import signal
import os
import httplib2
import ssl
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from neomodel import config,db, clear_neo4j_database, StructuredNode, UniqueIdProperty, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom,Relationship



from backports.ssl_match_hostname import match_hostname


class CertValidatingHTTPSConnection(httplib2.HTTPConnection):
    default_port = httplib2.HTTPS_PORT

    def __init__(self, host, port=None, key_file=None, cert_file=None,
                             ca_certs=None, strict=None, **kwargs):
        httplib.HTTPConnection.__init__(self, host, port, strict, **kwargs)
        self.key_file = key_file
        self.cert_file = cert_file
        self.ca_certs = ca_certs
        if self.ca_certs:
            self.cert_reqs = ssl.CERT_REQUIRED
        else:
            self.cert_reqs = ssl.CERT_NONE

    def connect(self):
        httplib.HTTPConnection.connect(self)
        self.sock = ssl.wrap_socket(self.sock, keyfile=self.key_file,
                                    certfile=self.cert_file,
                                    cert_reqs=self.cert_reqs,
                                    ca_certs=self.ca_certs)
        if self.cert_reqs & ssl.CERT_REQUIRED:
            cert = self.sock.getpeercert()
            hostname = self.host.split(':', 0)[0]
            match_hostname(cert, hostname)


class VerifiedHTTPSHandler(urllib.HTTPSHandler):
    def __init__(self, **kwargs):
        urllib2.HTTPSHandler.__init__(self)
        self._connection_args = kwargs

    def https_open(self, req):
        def http_class_wrapper(host, **kwargs):
            full_kwargs = dict(self._connection_args)
            full_kwargs.update(kwargs)
            return CertValidatingHTTPSConnection(host, **full_kwargs)

        return self.do_open(http_class_wrapper, req)


if __name__ == "__main__":
    handler = VerifiedHTTPSHandler(ca_certs=certifi.where())
    # assuming proxy settings are in environment or set them with:
    # urllib2.ProxyHandler({'http_proxy': 'http://', 'https_proxy' = 'http://'})
    opener = urllib2.build_opener(handler, urllib2.ProxyHandler())
    opener.open('https://google.com').read()
    opener.open('https://kennesaw.edu').read()
