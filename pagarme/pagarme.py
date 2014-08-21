# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from .mixins import PagarMeRequest
from .transaction import Transaction


class PagarMe():
    def __init__(self, api_key):
        self.api_key = api_key
        self.requester = PagarMeRequest(self.api_key)
        self.transaction = Transaction(self.requester)

    def build_transaction(self, transaction_attributes):
        pass
