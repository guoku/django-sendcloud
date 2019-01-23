from requests import exceptions


class SendCloudAPIError(Exception):
    pass


class SendCloudConnectionError(exceptions.ConnectionError):
    pass


