from ..base import AdyenServiceBase


class PayoutSettingsMerchantLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PayoutSettingsMerchantLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v3"

    def delete_payout_setting(self, merchantId, payoutSettingsId, idempotency_key=None, **kwargs):
        """
        Delete a payout setting
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def list_payout_settings(self, merchantId, idempotency_key=None, **kwargs):
        """
        Get a list of payout settings
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/payoutSettings"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_payout_setting(self, merchantId, payoutSettingsId, idempotency_key=None, **kwargs):
        """
        Get a payout setting
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_payout_setting(self, request, merchantId, payoutSettingsId, idempotency_key=None, **kwargs):
        """
        Update a payout setting
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/payoutSettings/{payoutSettingsId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def add_payout_setting(self, request, merchantId, idempotency_key=None, **kwargs):
        """
        Add a payout setting
        """
        endpoint = self.baseUrl + f"/merchants/{merchantId}/payoutSettings"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

