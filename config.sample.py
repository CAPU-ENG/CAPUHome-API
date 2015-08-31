#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: config.sample.py
Author: huxuan <i(at)huxuan.org>
Description: Configuration file for app.
"""

# Debug or not
DEBUG = True

# Make jsonfiy encode in utf-8.
JSON_AS_ASCII = False

# Secret key.
SECRET_KEY = 'CAPUHOME_Secret_Key'

# Database & sqlalchemy.
DB_USERNAME = 'username'
DB_PASSWORD = 'password'
DB_SERVER = 'localhost'
DB_NAME = 'dbname'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(
    DB_USERNAME, DB_PASSWORD, DB_SERVER, DB_NAME)
