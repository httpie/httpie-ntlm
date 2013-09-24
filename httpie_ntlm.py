"""
NTLM auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin


__version__ = '1.0.2'
__author__ = 'Jakub Roztocil'
__licence__ = 'BSD'


class NTLMAuthPlugin(AuthPlugin):

    name = 'NTLM auth'
    auth_type = 'ntlm'
    description = ''

    def get_auth(self, username, password):
        from requests_ntlm import HttpNtlmAuth
        return HttpNtlmAuth(username, password)
