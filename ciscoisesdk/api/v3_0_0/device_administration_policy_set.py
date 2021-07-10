# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine Device Administration - Policy Set API wrapper.

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

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
    get_next_page,
)
import urllib.parse


class DeviceAdministrationPolicySet(object):
    """Identity Services Engine Device Administration - Policy Set API (version: 3.0.0).

    Wraps the Identity Services Engine Device Administration - Policy Set
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceAdministrationPolicySet
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceAdministrationPolicySet, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_device_admin_policy_set_list(self,
                                         headers=None,
                                         **query_parameters):
        """Device Admin List of policy sets.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/policy/device-admin/policy-set')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed5920513e92b1728b824771cc_v3_0_0', _api_response)

    def get_all(self,
                headers=None,
                **query_parameters):
        """Alias for `get_device_admin_policy_set_list <#ciscoisesdk.
        api.v3_0_0.device_administration_policy_set.
        DeviceAdministrationPolicySet.get_device_admin_policy_set_list>`_
        """
        return self.get_device_admin_policy_set_list(
            headers=headers,
            **query_parameters
        )

    def create_device_admin_policy_set(self,
                                       condition=None,
                                       default=None,
                                       description=None,
                                       hit_counts=None,
                                       id=None,
                                       is_proxy=None,
                                       link=None,
                                       name=None,
                                       rank=None,
                                       service_name=None,
                                       state=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **query_parameters):
        """Device Admin Create a new policy set.

        Args:
            condition(object): condition, property of the request
                body.
            default(boolean): Flag which indicates if this policy
                set is the default one, property of the
                request body.
            description(string): The description for the policy set,
                property of the request body.
            hit_counts(integer): The amount of times the policy was
                matched, property of the request body.
            id(string): Identifier for the policy set, property of
                the request body.
            is_proxy(boolean): Flag which indicates if the policy
                set service is of type 'Proxy Sequence'
                or 'Allowed Protocols', property of the
                request body.
            link(object): link, property of the request body.
            name(string): Given name for the policy set, [Valid
                characters are alphanumerics,
                underscore, hyphen, space, period,
                parentheses], property of the request
                body.
            rank(integer): The rank(priority) in relation to other
                policy set. Lower rank is higher
                priority., property of the request body.
            service_name(string): Policy set service identifier
                Allowed Protocols,Server Sequence..,
                property of the request body.
            state(string): The state that the policy set is in. A
                disabled policy set cannot be matched.,
                property of the request body. Available
                values are 'enabled', 'disabled' and
                'monitor'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'condition':
                    condition,
                'default':
                    default,
                'description':
                    description,
                'hitCounts':
                    hit_counts,
                'id':
                    id,
                'isProxy':
                    is_proxy,
                'link':
                    link,
                'name':
                    name,
                'rank':
                    rank,
                'serviceName':
                    service_name,
                'state':
                    state,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_ac3ccf225801ad8ba0bb1ad9de0b_v3_0_0')\
                .validate(_payload)

        e_url = ('/v1/policy/device-admin/policy-set')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_ac3ccf225801ad8ba0bb1ad9de0b_v3_0_0', _api_response)

    def create(self,
               condition=None,
               default=None,
               description=None,
               hit_counts=None,
               id=None,
               is_proxy=None,
               link=None,
               name=None,
               rank=None,
               service_name=None,
               state=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_device_admin_policy_set <#ciscoisesdk.
        api.v3_0_0.device_administration_policy_set.
        DeviceAdministrationPolicySet.create_device_admin_policy_set>`_
        """
        return self.create_device_admin_policy_set(
            condition=condition,
            default=default,
            description=description,
            hit_counts=hit_counts,
            id=id,
            is_proxy=is_proxy,
            link=link,
            name=name,
            rank=rank,
            service_name=service_name,
            state=state,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def reset_hit_counts_device_admin_policy_sets(self,
                                                  headers=None,
                                                  **query_parameters):
        """Device Admin Reset HitCount for PolicySets.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/v1/policy/device-admin/policy-set/reset-hitcount')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed47964d442d52dca1f7da967f37b3e2_v3_0_0', _api_response)

    def reset_hit_counts(self,
                         headers=None,
                         **query_parameters):
        """Alias for `reset_hit_counts_device_admin_policy_sets <#ciscoisesdk.
        api.v3_0_0.device_administration_policy_set.
        DeviceAdministrationPolicySet.reset_hit_counts_device_admin_policy_sets>`_
        """
        return self.reset_hit_counts_device_admin_policy_sets(
            headers=headers,
            **query_parameters
        )

    def get_device_admin_policy_set_by_id(self,
                                          policy_id,
                                          headers=None,
                                          **query_parameters):
        """Device Admin Get policy set attributes.

        Args:
            policy_id(basestring): policyId path parameter. Policy
                id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(policy_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
        }

        e_url = ('/v1/policy/device-admin/policy-set/{policyId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f36918d98a546ab6ca2618d1844984_v3_0_0', _api_response)

    def get_by_id(self,
                  policy_id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_device_admin_policy_set_by_id <#ciscoisesdk.
        api.v3_0_0.device_administration_policy_set.
        DeviceAdministrationPolicySet.get_device_admin_policy_set_by_id>`_
        """
        return self.get_device_admin_policy_set_by_id(
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )

    def update_device_admin_policy_set_by_id(self,
                                             policy_id,
                                             condition=None,
                                             default=None,
                                             description=None,
                                             hit_counts=None,
                                             id=None,
                                             is_proxy=None,
                                             link=None,
                                             name=None,
                                             rank=None,
                                             service_name=None,
                                             state=None,
                                             headers=None,
                                             payload=None,
                                             active_validation=True,
                                             **query_parameters):
        """Device Admin Update a policy set.

        Args:
            condition(object): condition, property of the request
                body.
            default(boolean): Flag which indicates if this policy
                set is the default one, property of the
                request body.
            description(string): The description for the policy set,
                property of the request body.
            hit_counts(integer): The amount of times the policy was
                matched, property of the request body.
            id(string): Identifier for the policy set, property of
                the request body.
            is_proxy(boolean): Flag which indicates if the policy
                set service is of type 'Proxy Sequence'
                or 'Allowed Protocols', property of the
                request body.
            link(object): link, property of the request body.
            name(string): Given name for the policy set, [Valid
                characters are alphanumerics,
                underscore, hyphen, space, period,
                parentheses], property of the request
                body.
            rank(integer): The rank(priority) in relation to other
                policy set. Lower rank is higher
                priority., property of the request body.
            service_name(string): Policy set service identifier
                Allowed Protocols,Server Sequence..,
                property of the request body.
            state(string): The state that the policy set is in. A
                disabled policy set cannot be matched.,
                property of the request body. Available
                values are 'enabled', 'disabled' and
                'monitor'.
            policy_id(basestring): policyId path parameter. Policy
                id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(policy_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _payload = {
                'condition':
                    condition,
                'default':
                    default,
                'description':
                    description,
                'hitCounts':
                    hit_counts,
                'id':
                    id,
                'isProxy':
                    is_proxy,
                'link':
                    link,
                'name':
                    name,
                'rank':
                    rank,
                'serviceName':
                    service_name,
                'state':
                    state,
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b6cc40e0f4b45e8da5908776d124ed5a_v3_0_0')\
                .validate(_payload)

        e_url = ('/v1/policy/device-admin/policy-set/{policyId}')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b6cc40e0f4b45e8da5908776d124ed5a_v3_0_0', _api_response)

    def update_by_id(self,
                     policy_id,
                     condition=None,
                     default=None,
                     description=None,
                     hit_counts=None,
                     id=None,
                     is_proxy=None,
                     link=None,
                     name=None,
                     rank=None,
                     service_name=None,
                     state=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """Alias for `update_device_admin_policy_set_by_id <#ciscoisesdk.
        api.v3_0_0.device_administration_policy_set.
        DeviceAdministrationPolicySet.update_device_admin_policy_set_by_id>`_
        """
        return self.update_device_admin_policy_set_by_id(
            policy_id=policy_id,
            condition=condition,
            default=default,
            description=description,
            hit_counts=hit_counts,
            id=id,
            is_proxy=is_proxy,
            link=link,
            name=name,
            rank=rank,
            service_name=service_name,
            state=state,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def delete_device_admin_policy_set_by_id(self,
                                             policy_id,
                                             headers=None,
                                             **query_parameters):
        """Device Admin Delete a policy set.

        Args:
            policy_id(basestring): policyId path parameter. Policy
                id.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'X-Request-ID' in headers:
                check_type(headers.get('X-Request-ID'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(policy_id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'policyId': policy_id,
        }

        e_url = ('/v1/policy/device-admin/policy-set/{policyId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f602e2f88378502a8d8bca6dff274afe_v3_0_0', _api_response)

    def delete_by_id(self,
                     policy_id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_device_admin_policy_set_by_id <#ciscoisesdk.
        api.v3_0_0.device_administration_policy_set.
        DeviceAdministrationPolicySet.delete_device_admin_policy_set_by_id>`_
        """
        return self.delete_device_admin_policy_set_by_id(
            policy_id=policy_id,
            headers=headers,
            **query_parameters
        )
