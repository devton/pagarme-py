# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class PagarMeError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)
