#!/usr/bin/env python
"""Collection of functions for the manipulation of time series."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings

import mando
from mando.rst_text_formatter import RSTHelpFormatter

import pandas as pd

from .. import tsutils

warnings.filterwarnings('ignore')


@mando.command(formatter_class=RSTHelpFormatter, doctype='numpy')
@tsutils.doc(tsutils.docstrings)
def add_trend(start_offset,
              end_offset,
              input_ts='-',
              columns=None,
              clean=False,
              start_date=None,
              end_date=None,
              dropna='no',
              round_index=None,
              print_input=False):
    """Add a trend.

    Parameters
    ----------
    start_offset : float
        The starting value for the applied trend.
    end_offset : float
        The ending value for the applied trend.
    {input_ts}
    {columns}
    {start_date}
    {end_date}
    {dropna}
    {clean}
    {print_input}
    {round_index}

    """
    tsd = tsutils.common_kwds(tsutils.read_iso_ts(input_ts),
                              start_date=start_date,
                              end_date=end_date,
                              pick=columns,
                              round_index=round_index,
                              dropna=dropna,
                              clean=clean)
    # Need it to be float since will be using pd.np.nan
    ntsd = tsd.copy().astype('float64')

    ntsd.ix[:, :] = pd.np.nan
    ntsd.ix[0, :] = float(start_offset)
    ntsd.ix[-1, :] = float(end_offset)
    ntsd = ntsd.interpolate(method='values')

    ntsd = ntsd + tsd

    ntsd = tsutils.memory_optimize(ntsd)
    return tsutils.print_input(print_input,
                               tsd,
                               ntsd,
                               '_trend')