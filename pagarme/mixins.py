# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import requests


class PagarMeRequest():
    def __init__(self, api_key):
        self.endpoint = "https://api.pagar.me/1{}"
        self.payload = {'api_key': api_key}

    def commit(self, path, params, method='GET'):
        url = self.endpoint.format(path)
        self.payload.update(params)

        if method == 'GET':
            request = requests.get(url, params=self.payload)

        return request
