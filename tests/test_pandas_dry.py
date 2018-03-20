#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pandas_dry` package."""

import numpy as np
import pandas as pd
import unittest

from pandas_dry import pipes

class TestPipes(unittest.TestCase):
    def setUp(self):
        pass

    def test_null_counts(self):
        n = 27
        m = 41
        nulls = [np.nan] * n
        nonnulls = np.random.rand(m)
        data = np.concatenate((nulls, nonnulls))
        ser = pd.Series(data=data)
        null_counts = ser.pipe(pipes.null_counts)

        self.assertEqual(n, null_counts['Null'])
        self.assertEqual(m, null_counts['Not Null'])
