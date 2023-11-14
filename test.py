#!/usr/bin/env python3

import unittest
from env import load
from env import read_body


class TestEnvLoad(unittest.TestCase):
    def test_env_load(self):
        data = load()
        length = len(data)
        self.assertGreater(length, 0)
        self.assertIsInstance(data, dict)
        self.assertTrue("testReportIdx" in data)

    def test_env_load_other(self):
        data = load("metric.postman_collection2.json")
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data, dict)
        self.assertTrue("testReportIdx" in data)
        self.assertTrue("metricGroup5" in data)
        # print("{}".format(data["metricReportN"]))

    def test_env_load_empty(self):
        data = load("")
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data, dict)

    def test_read_body(self):
        data = read_body()
        self.assertGreater(len(data), 10)

    def test_read_body_json(self):
        try:
            data = read_body("metric.postman_collection2.json", "TestGroupN")
            self.assertGreater(len(data), 10)
            # print(data)
        except Exception:
            self.fail("No expection expected")

    def test_read_body_json_no_name(self):
        with self.assertRaises(Exception):
            read_body("metric.postman_collection2.json")



if __name__ == '__main__':
    unittest.main()