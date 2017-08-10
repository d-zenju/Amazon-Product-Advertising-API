# -*- coding: utf-8 -*-

import time
import datetime
import urllib2
import base64
import hmac
import hashlib

# Your AWS Access Key ID, as taken from the AWS Your Account page
AWS_ACCESS_KEY_ID = ""

# Your AWS Secret Key corresponding to the above ID, as taken from the AWS Your Account page
AWS_SECRET_KEY = ""

# The region you are interested in
ENDPOINT = "webservices.amazon.co.jp"

REQUEST_URI = "/onca/xml"

params = {
  "Service":"AWSECommerceService",
  "Operation":"BrowseNodeLookup",
  "AWSAccessKeyId":"",
  "AssociateTag":"",
  "BrowseNodeId":"",
  "ResponseGroup":"BrowseNodeInfo,TopSellers"
}

# Set current timestamp if not set
if (("Timestamp" in params) is False):
    params["Timestamp"] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# Sort the parameters by key
params = sorted(params.items())

pairs = []

for param in params:
    pairs.append(urllib2.quote(str(param[0])) + "=" + urllib2.quote(str(param[1])))

# Generate the canonical query
canonical_query_string = "&".join(pairs)

# Generate the string to be signed
string_to_sign = "GET\n" + str(ENDPOINT) + "\n" + str(REQUEST_URI) + "\n" + str(canonical_query_string)

# Generate the signature required by the Product Advertising API
signature = base64.b64encode(hmac.new(AWS_SECRET_KEY, string_to_sign, hashlib.sha256).digest())

request_url = 'http://' + str(ENDPOINT) + str(REQUEST_URI) + '?' + str(canonical_query_string) + '&Signature=' + urllib2.quote(signature)

# Generate the signed URL
print "Signed URL: \"" + str(request_url) + "\""