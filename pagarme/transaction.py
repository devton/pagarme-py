# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import re

from .exceptions import PagarMeError


class Transaction():
    def __init__(self, requester):
        self.requester = requester
        self.attributes = {}

    def get_transactions(self, page=1):
        return self.requester.commit('/transactions', {'page': page}, 'GET')

    def build_transaction(self, transaction_attributes):
        if not isinstance(transaction_attributes, dict):
            raise PagarMeError('Transaction attributes need be an dict')

        self.attributes.update(transaction_attributes)

    def charge(self):
        self.validate_attrs

    def validate_attrs(self):
        TransactionValidator(self.attributes)


class TransactionValidator():
    def __init__(self, attrs):
        if len(attrs) <= 0:
            raise PagarMeError('Need a valid attr dict')

        self.regex_pattern = re.compile(r"(boleto|credit_card)")
        self.attrs = attrs
        self.start_validate()

    def start_validate(self):
        errors = []

        if 'amount' not in self.attrs or self.attrs['amount'] <= 0:
            errors.append('Need to define an amount')

        if 'payment_method' not in self.attrs:
            errors.append('Need to define an valid payment_method')

        if 'payment_method' in self.attrs:
            if not re.match(self.regex_pattern, self.attrs['payment_method']):
                errors.append(
                    "invalid payment_method need be boleto or credit_card")

        if len(errors) > 0:
            raise PagarMeError(', '.join(errors))
