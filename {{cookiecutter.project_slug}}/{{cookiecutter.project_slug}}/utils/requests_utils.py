import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client


def enable_requests_log():
    http_client.HTTPConnection.debuglevel = 1
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
