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

# log handler
logger = logging.getLogger("simple_example")
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def verbose(verb=True):
    if verb:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)


def print_res(url, status):
    logger.debug("status: {}, url: {}".format(status, url))


# default disable verbose
verbose(False)


# main functions
def get(url, headers=headers):
    res = requests.request("GET", url, headers=headers, verify=False)
    print_res(url, res.status_code)
    return res


def delete(url, headers=headers):
    res = requests.request("DELETE", url, headers=headers, verify=False)
    print_res(url, res.status_code)
    return res


def post(url, data, headers=headers):
    res = requests.request("POST", url, headers=headers, data=data, verify=False)
    print_res(url, res.status_code)
    return res
