#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_help_option(script_runner):
    ret = script_runner.run('scil_remove_outliers_ransac.py', '--help')
    assert ret.success
