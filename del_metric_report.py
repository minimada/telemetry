#!/usr/bin/env python3

from env import load
import myhttp

ENV_FILE = "metric.postman_collection2.json"
vars = load(ENV_FILE)
if not "metricReportN" in vars or not "maxGroup" in vars:
    print("Cannot find critical parameter")
    exit(1)

metricReportN = int(vars["metricReportN"])
metricGrouptN = int(vars["maxGroup"])

base_url = "192.168.56.168"
reportName = "testGroup{}_{}"
url = "https://{}/redfish/v1/TelemetryService/MetricReportDefinitions/".format(base_url)

myhttp.verbose()
for i in range(1, metricGrouptN + 1):
    for k in range(metricReportN):
        myhttp.delete(url + reportName.format(i, k))
