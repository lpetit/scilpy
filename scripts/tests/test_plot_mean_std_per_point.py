#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_help_option(script_runner):
    ret = script_runner.run('scil_plot_mean_std_per_point.py', '--help')
    assert ret.success
