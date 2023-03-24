from ..base import AdyenServiceBase


class PaymentInstrumentGroupsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(PaymentInstrumentGroupsApi, self).__init__(client=client)
        self.service = "balancePlatform"

    def get_payment_instrument_group(self, id, idempotency_key=None, **kwargs):
        """
        Get a payment instrument group
        """
        endpoint = f"/paymentInstrumentGroups/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_all_transaction_rules_for_payment_instrument_group(self, id, idempotency_key=None, **kwargs):
        """
        Get all transaction rules for a payment instrument group
        """
        endpoint = f"/paymentInstrumentGroups/{id}/transactionRules"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_payment_instrument_group(self, request, idempotency_key=None, **kwargs):
        """
        Create a payment instrument group
        """
        endpoint = f"/paymentInstrumentGroups"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

