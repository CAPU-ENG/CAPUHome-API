#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: run.py
Author: huxuan <i@huxuan.org>
Description: Run script for app.
"""
import os.path

from app import app

if os.path.isfile('config.py'):
    raise Exception('Please copy `config.sample.py` to `config.py` with proper'
                    'configuration to make it work.')


def main():
    """ Main function for run script. """
    app.run()

if __name__ == '__main__':
    main()
