#!/usr/bin/env python3

import json

VAR_FILE = "var.json"
BODY_FILE = "body"
ROOT_NODE = "variable"
ITEM_NODE = "item"
VERBOSE = False


def verbose_print(msg):
    if VERBOSE:
        print(msg)


"""
convert the key, value data to python dict
"""


def toDict(data):
    res = {}
    for item in data:
        if "key" in item and "value" in item:
            res[item["key"]] = item["value"]
        else:
            verbose_print("not valid item{}".format(item))
    return res


"""
load variable data from postman collection export
"""


def load(file=VAR_FILE):
    if file == "":
        file = VAR_FILE
    with open(file, "r") as f:
        data = json.load(f)
    if ROOT_NODE in data:
        return toDict(data[ROOT_NODE])
    return []



def read_body(file=BODY_FILE, name=""):
    if file == "":
        file = BODY_FILE
    with open(file, "r") as f:
        body = f.read()
    # direct read body data from template    
    if not file.endswith("json"):
        return body    
    # read body data from postman collection export json
    if name == "":
        raise Exception("request name must set")
    body_json = json.loads(body)
    if not ITEM_NODE in body_json:
        raise Exception("not expected format json")

    for item in body_json[ITEM_NODE]:
        if item['name'] == name:
            body = item['request']['body']
            break
    # we are now only support raw body
    mode = body['mode']
    if mode != "raw":
        raise Exception("not supported body mode")
    return body['raw']