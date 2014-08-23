# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from .exceptions import TransactionValidationError

AVAIABLE_PAYMENT_METHOD = ['credit_card', 'boleto']


def validate_transaction(attrs):
    if len(attrs) <= 0:
        raise TransactionValidationError('Need a valid attr dict')

    errors = []

    if 'amount' not in attrs or attrs['amount'] <= 0:
        errors.append('Need to define an amount')

    if 'payment_method' not in attrs:
        errors.append('Need to define an valid payment_method')

    if 'payment_method' in attrs:
        if not attrs['payment_method'] in AVAIABLE_PAYMENT_METHOD:
            errors.append(
                "invalid payment_method need be boleto or credit_card")

    if len(errors) > 0:
        raise TransactionValidationError(', '.join(errors))


class Transaction():
    def __init__(self, requester):
        self.requester = requester
        self.attributes = {}

    def get_transactions(self, page=1):
        return self.requester.commit('/transactions', {'page': page}, 'GET')

    def build_transaction(self, transaction_attributes):
        if not isinstance(transaction_attributes, dict):
            raise TransactionValidationError(
                'Transaction attributes need be an dict')

        self.attributes.update(transaction_attributes)

    def charge(self):
        self.validate_attrs

    def validate_attrs(self):
        validate_transaction(self.attributes)


