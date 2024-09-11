from ciscoisesdk import IdentityServicesEngineAPI
from ciscoisesdk.exceptions import ApiError

# Create a IdentityServicesEngineAPI connection object;
# it uses ISE custom URL, username, and password, with ISE API version 3.3_patch_1
# and its API Gateway enabled,
# verify=True to verify the server's TLS certificate
# with debug logs disabled
# and without using the CSRF token
api = IdentityServicesEngineAPI(username='readonly',
                                password='ISEisC00L',
                                uses_api_gateway=True,
                                base_url='https://devnetsandboxise.cisco.com',
                                version='3.2_beta',
                                verify=True,
                                debug=False,
                                uses_csrf_token=False)
# NOTE: This collection assumes that the ERS APIs and OpenAPIs are enabled.

# Get allowed protocols (first page)
search_result = api.allowed_protocols.get_all().response.SearchResult
if search_result and search_result.resources:
  for resource in search_result.resources:
    resource_detail = api.allowed_protocols.get_by_id(
                        resource.id
                      ).response.AllowedProtocols
    print("Id {}\nName {}\nallowChap {}\n".format(resource_detail.id,
                                                  resource_detail.name,
                                                  resource_detail.allowChap))
print("----------")
