#!/usr/bin/env python3

from env import load
from env import read_body
import myhttp

ENV_FILE = "metric.postman_collection2.json"
REQ_NAME = "TestGroupN"

vars = load(ENV_FILE)
metricGroups = "metricGroup{}"
critical_vars = ["metricReportN", "maxGroup"]
for i in range(1, 6):
    critical_vars.append(metricGroups.format(i))

# check vars we need for create request
for c in critical_vars:
    if not c in vars:
        print("Cannot find critical parameter: " + c)
        exit(1)

body = read_body(ENV_FILE, REQ_NAME)
if len(body) < 10:
    print("body file get some trouble")
    exit(1)

base_url = "192.168.56.168"
url = "https://{}/redfish/v1/TelemetryService/MetricReportDefinitions/".format(base_url)
metricReportN = int(vars["metricReportN"])
metricGrouptN = int(vars["maxGroup"])
metricData = vars["metricGroup1"]
# myhttp.verbose()
for i in range(1, metricGrouptN):
    metricData = vars[metricGroups.format(i)]
    for k in range(metricReportN):
        body_data = (
            body.replace("{{metricData}}", metricData)
            .replace("{{testGroupIdx}}", str(i))
            .replace("{{testReportIdx}}", str(k))
        )
        res = myhttp.post(url, body_data)
        print("i:{}, k:{}, res: {}".format(i, k,res.status_code))
    
