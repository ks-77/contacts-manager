class ImmediateHttpResponse(Exception):

    def __init__(self, response):
        self.response = response


class AccountExistError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = 'An account already exists with this e-mail address.'


class OAuth2Error(Exception):

    def __init__(self, message, *args, **kwargs):
        self.message = message
