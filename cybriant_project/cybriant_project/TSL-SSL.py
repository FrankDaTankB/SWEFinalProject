import json
import tornado  # @UnresolvedImport
from tornado.httpclient import HTTPClient  # @NoMove @UnresolvedImport


response = HTTPClient().fetch("https://www.google.com").body.decode()
data = json.loads(response)
tls_version = data["tls_version"]

print("tls_version")
