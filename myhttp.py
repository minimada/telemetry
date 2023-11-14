import requests
import urllib3
import logging
import sys

# disable SSL certificate verify fail warning
urllib3.disable_warnings()

# use Openbmc default user/passwd with basic authentication
headers = {
    "Authorization": "Basic cm9vdDowcGVuQm1j",
    "Content-Type": "application/json",
}

# handler log
logger = logging.getLogger("simple_example")
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def verbose(verb=True):
    if verb:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)


# default disable verbose
verbose(False)


# main functions
def get(url, headers=headers):
    logger.debug(url)
    return requests.request("GET", url, headers=headers, verify=False)


def delete(url, headers=headers):
    logger.debug(url)
    return requests.request("DELETE", url, headers=headers, verify=False)


def post(url, data, headers=headers):
    logger.debug(url)
    return requests.request("POST", url, headers=headers, data=data, verify=False)
