# -*- coding: utf-8 -*-
from unittest import TestCase

from pagarme.transaction import Transaction
from pagarme.exceptions import PagarMeError
from pagarme.mixins import PagarMeRequest


class TransactionTest(TestCase):
    def setUp(self):
        self.requester = PagarMeRequest(
            'ak_test_KGXIjQ4GicOa2BLGZrDRTR5qNQxDWo')
        self.transaction = Transaction(self.requester)

    def test_build_transaction_attributes_should_be_an_dict(self):
        with self.assertRaises(PagarMeError):
            self.transaction.build_transaction('invalid arg')

    def test_get_transactions(self):
        result = self.transaction.get_transactions()
        self.assertEqual(result.status_code, 200)
