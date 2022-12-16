"""
    Management API

    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to version 1 of the `/companies/{companyId}/webhooks` endpoint, use:  ```text https://management-test.adyen.com/v1/companies/{companyId}/webhooks ```  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  ```text https://management-live.adyen.com/v1 ```  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""

from ..base import AdyenServiceBase


class TerminalSettingsStoreLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalSettingsStoreLevelApi, self).__init__(client=client)
        self.service = "management"

    def get_merchants_merchant_id_stores_reference_terminal_logos(self, merchantId, reference, idempotency_key=None, **kwargs):
        """
        Get the terminal logo
        """
        endpoint = f"/merchants/{merchantId}/stores/{reference}/terminalLogos"
        endpoint = endpoint.replace('/','',1)
        method = "GET"
        return self.client.call_management_api(None, method, endpoint, idempotency_key, **kwargs)

    def get_merchants_merchant_id_stores_reference_terminal_settings(self, merchantId, reference, idempotency_key=None, **kwargs):
        """
        Get terminal settings
        """
        endpoint = f"/merchants/{merchantId}/stores/{reference}/terminalSettings"
        endpoint = endpoint.replace('/','',1)
        method = "GET"
        return self.client.call_management_api(None, method, endpoint, idempotency_key, **kwargs)

    def get_stores_store_id_terminal_logos(self, storeId, idempotency_key=None, **kwargs):
        """
        Get the terminal logo
        """
        endpoint = f"/stores/{storeId}/terminalLogos"
        endpoint = endpoint.replace('/','',1)
        method = "GET"
        return self.client.call_management_api(None, method, endpoint, idempotency_key, **kwargs)

    def get_stores_store_id_terminal_settings(self, storeId, idempotency_key=None, **kwargs):
        """
        Get terminal settings
        """
        endpoint = f"/stores/{storeId}/terminalSettings"
        endpoint = endpoint.replace('/','',1)
        method = "GET"
        return self.client.call_management_api(None, method, endpoint, idempotency_key, **kwargs)

    def patch_merchants_merchant_id_stores_reference_terminal_logos(self, request, merchantId, reference, idempotency_key=None, **kwargs):
        """
        Update the terminal logo
        """
        endpoint = f"/merchants/{merchantId}/stores/{reference}/terminalLogos"
        endpoint = endpoint.replace('/','',1)
        method = "PATCH"
        return self.client.call_management_api(request, method, endpoint, idempotency_key, **kwargs)

    def patch_merchants_merchant_id_stores_reference_terminal_settings(self, request, merchantId, reference, idempotency_key=None, **kwargs):
        """
        Update terminal settings
        """
        endpoint = f"/merchants/{merchantId}/stores/{reference}/terminalSettings"
        endpoint = endpoint.replace('/','',1)
        method = "PATCH"
        return self.client.call_management_api(request, method, endpoint, idempotency_key, **kwargs)

    def patch_stores_store_id_terminal_logos(self, request, storeId, idempotency_key=None, **kwargs):
        """
        Update the terminal logo
        """
        endpoint = f"/stores/{storeId}/terminalLogos"
        endpoint = endpoint.replace('/','',1)
        method = "PATCH"
        return self.client.call_management_api(request, method, endpoint, idempotency_key, **kwargs)

    def patch_stores_store_id_terminal_settings(self, request, storeId, idempotency_key=None, **kwargs):
        """
        Update terminal settings
        """
        endpoint = f"/stores/{storeId}/terminalSettings"
        endpoint = endpoint.replace('/','',1)
        method = "PATCH"
        return self.client.call_management_api(request, method, endpoint, idempotency_key, **kwargs)



