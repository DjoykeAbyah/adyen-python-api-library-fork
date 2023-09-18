from ..base import AdyenServiceBase


class TerminalsTerminalLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalsTerminalLevelApi, self).__init__(client=client)
        self.service = "management"
        self.baseUrl = "https://management-test.adyen.com/v1"

    def list_terminals(self, idempotency_key=None, **kwargs):
        """
        Get a list of terminals
        """
        endpoint = self.baseUrl + f"/terminals"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)
