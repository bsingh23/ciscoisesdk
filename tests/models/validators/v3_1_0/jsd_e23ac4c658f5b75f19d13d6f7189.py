# -*- coding: utf-8 -*-
"""Identity Services Engine getNetworkAccessLocalExceptionRules data model.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
import json
from ciscoisesdk.exceptions import MalformedRequest

from builtins import *


class JSONSchemaValidatorE23AC4C658F5B75F19D13D6F7189(object):
    """getNetworkAccessLocalExceptionRules request schema definition."""
    def __init__(self):
        super(JSONSchemaValidatorE23AC4C658F5B75F19D13D6F7189, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "items": {
                "properties": {
                "link": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "enum": [
                "next",
                "previous",
                "self",
                "status"
                ],
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "required": [
                "href"
                ],
                "type": "object"
                },
                "profile": {
                "items": {
                "type": "string"
                },
                "type": "array"
                },
                "rule": {
                "properties": {
                "condition": {
                "properties": {
                "conditionType": {
                "enum": [
                "ConditionAndBlock",
                "ConditionAttributes",
                "ConditionOrBlock",
                "ConditionReference",
                "LibraryConditionAndBlock",
                "LibraryConditionAttributes",
                "LibraryConditionOrBlock",
                "TimeAndDateCondition"
                ],
                "type": "string"
                },
                "isNegate": {
                "type": "boolean"
                },
                "link": {
                "properties": {
                "href": {
                "type": "string"
                },
                "rel": {
                "enum": [
                "next",
                "previous",
                "self",
                "status"
                ],
                "type": "string"
                },
                "type": {
                "type": "string"
                }
                },
                "required": [
                "href"
                ],
                "type": "object"
                }
                },
                "required": [
                "conditionType"
                ],
                "type": "object"
                },
                "default": {
                "type": "boolean"
                },
                "hitCounts": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "name": {
                "type": "string"
                },
                "rank": {
                "type": "integer"
                },
                "state": {
                "enum": [
                "disabled",
                "enabled",
                "monitor"
                ],
                "type": "string"
                }
                },
                "required": [
                "name"
                ],
                "type": "object"
                },
                "securityGroup": {
                "type": "string"
                }
                },
                "required": [
                "rule"
                ],
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
                }
                },
                "required": [
                "response",
                "version"
                ],
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )
