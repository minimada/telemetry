# telemetry
This repository is the test scripts for [Openbmc telemetry service](https://github.com/openbmc/docs/blob/master/designs/telemetry.md).
The original script is developed by Postman, but Postman free plan have test run limitation.
After I try the postman alternatives, all of them get cost which have test script function.
So I deside move to python script, some of the alternative like HTTPie or Postcode can convert requests to python code easily.
This repo shows move test scripts from Postman to Python is not hard thing.

## Files
* metric.postman_collection2.json, the collection export data from Postman
* env.py, the utils for read data from collection export data. Include variables and request item.
* myhttp.py, the python request helper for Openbmc. Disable SSL certificate verify fail as default.
* test.py, unit test script for env module.
* add_metric_report.py, test script for add metric report definition via redfish API.
* del_metric_report.py, test script for delete metric report definition via redfish API.

## Environment setup
You need an Arbel EVB and run Openbmc on it. And configure DUT IP address to 192.168.56.168 or change the IP address via set url in script.

## Usage
```bash
python3 add_metric_report.py
python3 del_metric_report.py
```
Note. Set the metricReportN value in json file to change the add report number.
