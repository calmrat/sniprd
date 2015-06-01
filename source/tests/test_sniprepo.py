#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Chris Ward" <cward@redhat.com>

from __future__ import unicode_literals, absolute_import


def test_SnipRepo():
    # simple test that import works
    from sniprd.sniprepo import SnipRepo
    assert SnipRepo


def test_SnipRepoSQLAlchemy():
    # simple test that import works
    from sniprd.sniprepo import SnipRepoSQLAlchemy
    assert SnipRepoSQLAlchemy


def test_Snip():
    # simple test that import works
    from sniprd.sniprepo import Snip
    assert Snip
