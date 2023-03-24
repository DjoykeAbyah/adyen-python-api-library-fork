from ..base import AdyenServiceBase


class BankAccountValidationApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(BankAccountValidationApi, self).__init__(client=client)
        self.service = "balancePlatform"

    def validate_bank_account_identification(self, request, idempotency_key=None, **kwargs):
        """
        Validate a bank account
        """
        endpoint = f"/validateBankAccountIdentification"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

