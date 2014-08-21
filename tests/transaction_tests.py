# -*- coding: utf-8 -*-
from unittest import TestCase

from pagarme.transaction import Transaction, TransactionValidator
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


class TransactionValidatorTest(TestCase):
    def test_validation(self):
        with self.assertRaises(PagarMeError):
            TransactionValidator({})

    def test_validation_of_amount(self):
        with self.assertRaises(PagarMeError):
            TransactionValidator({'payment_method': 'boleto'})

    def test_validation_of_payment_method(self):
        with self.assertRaises(PagarMeError):
            TransactionValidator({'amount': 1000})

    def test_validation_of_invalid_payment_method(self):
        with self.assertRaises(PagarMeError):
            TransactionValidator({'amount': 1000, 'payment_method': 'foo'})
