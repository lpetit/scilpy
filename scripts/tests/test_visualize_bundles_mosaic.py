#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_help_option(script_runner):
    ret = script_runner.run('scil_visualize_bundles_mosaic.py', '--help')
    assert ret.success
