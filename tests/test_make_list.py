#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase

from tstoolbox import tsutils


class TestMakeList(TestCase):
    def test_make_list(self):
        assert tsutils.make_list(None) == None
        assert tsutils.make_list(1) == [1]
        assert tsutils.make_list(1.2) == [1.2]
        assert tsutils.make_list("") == None
        assert tsutils.make_list("1,2") == [1, 2]
        assert tsutils.make_list("2,") == [2, None]
        assert tsutils.make_list([1, 2, 3]) == [1, 2, 3]
        assert tsutils.make_list(["1", 2, "3"]) == [1, 2, 3]
        assert tsutils.make_list([1, "er", 3]) == [1, "er", 3]
        assert tsutils.make_list([1, "er", 3.3]) == [1, "er", 3.3]
        assert tsutils.make_list(["1", "er", "3"]) == [1, "er", 3]
        assert tsutils.make_list(["1", "", "5.6"]) == [1, None, 5.6]
        assert tsutils.make_list(["1", "None", "5.6"]) == [1, None, 5.6]
        assert tsutils.make_list("None") == None
        assert tsutils.make_list("") == None
        assert tsutils.make_list("1.1,2.2,") == [1.1, 2.2, None]
