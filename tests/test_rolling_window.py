#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shlex
import subprocess
from unittest import TestCase

import pandas
import numpy as np
import tstoolbox.tsutils as tsutils
from pandas.testing import assert_frame_equal
from tstoolbox import tstoolbox

from . import capture


class TestRollingWindow(TestCase):
    def setUp(self):
        dr = pandas.date_range("2000-01-01", periods=2, freq="D")
        ts = pandas.Series([np.nan, 9.1], index=dr)
        self.compare_rolling_window_sum = pandas.DataFrame(
            ts, columns=["Value::rolling.2.sum"]
        )
        self.compare_rolling_window_sum.index.name = "Datetime"

        dr = pandas.date_range("2000-01-01", periods=2, freq="D")
        ts = pandas.Series([np.nan, 4.55], index=dr)
        self.compare_rolling_window_mean = pandas.DataFrame(
            ts, columns=["Value::rolling.2.mean"]
        )
        self.compare_rolling_window_mean.index.name = "Datetime"

        self.compare_rolling_window_sum_cli = capture.capture(
            tsutils._printiso, self.compare_rolling_window_sum
        )

        self.compare_rolling_window_mean_cli = capture.capture(
            tsutils._printiso, self.compare_rolling_window_mean
        )

    def test_rolling_window_sum(self):
        """API: Rolling window sum for data_simple.csv is 9.1."""
        out = tstoolbox.rolling_window(
            statistic="sum", input_ts="tests/data_simple.csv"
        )
        assert_frame_equal(out, self.compare_rolling_window_sum)

    def test_rolling_window_mean(self):
        """API: Rolling window mean for data_simple.csv is 4.55."""
        out = tstoolbox.rolling_window(
            statistic="mean", input_ts="tests/data_simple.csv"
        )
        assert_frame_equal(out, self.compare_rolling_window_mean)

    def test_rolling_window_sum_cli(self):
        """CLI: Rolling window mean for data_simple.csv is 9.1."""
        args = 'tstoolbox rolling_window sum --input_ts="tests/data_simple.csv"'
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()
        self.assertEqual(out[0], self.compare_rolling_window_sum_cli)

    def test_rolling_window_mean_cli(self):
        """CLI: Rolling window sum for data_simple.csv is 4.55."""
        args = 'tstoolbox rolling_window mean --input_ts="tests/data_simple.csv"'
        args = shlex.split(args)
        out = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()
        self.assertEqual(out[0], self.compare_rolling_window_mean_cli)
