from unittest import TestCase

import pytest

import pandas as pd
from pandas.testing import assert_frame_equal
from tstoolbox import tstoolbox, tsutils


class TestRead(TestCase):
    def setUp(self):
        base = pd.read_csv(
            "tests/data_missing.csv",
            index_col=[0],
            parse_dates=True,
            skipinitialspace=True,
        ).astype("float64")
        base.index.name = "Datetime"
        self.cumsum = base.cumsum()
        self.cumsum.columns = [tsutils.renamer(i, "sum") for i in self.cumsum.columns]

    def test_cumsum(self):
        """Test cumsum."""
        out = tstoolbox.accumulate(input_ts="tests/data_missing.csv", dropna="any")
        assert_frame_equal(out, self.cumsum)


def test_stats():
    """Test stat names."""
    with pytest.raises(ValueError):
        _ = tstoolbox.accumulate(
            input_ts="tests/data_missing.csv", dropna="any", statistic="camel"
        )
