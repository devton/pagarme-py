# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from .exceptions import PagarMeError


class Transaction():
    def __init__(self, requester):
        self.requester = requester

    def get_transactions(self, page=1):
        return self.requester.commit('/transactions', {'page': page}, 'GET')

    def build_transaction(self, transaction_attributes):
        if not isinstance(transaction_attributes, dict):
            raise PagarMeError('Transaction attributes need be an dict')

