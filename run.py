#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Entry point for 'balls' game"""
from system.bootstrap import bootstrap
from system.application import Application

settings = bootstrap()

if settings:
    app = Application(settings)
    app.run()
else:
    print "Settings file not found"
