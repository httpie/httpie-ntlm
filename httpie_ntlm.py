"""
NTLM auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin
from requests_ntlm import HttpNtlmAuth


__version__ = '1.0.2'
__author__ = 'Jakub Roztocil'
__licence__ = 'BSD'


class NTLMAuthPlugin(AuthPlugin):

    name = 'NTLM auth'
    auth_type = 'ntlm'
    description = ''

    def get_auth(self, username, password):
        return HttpNtlmAuth(username, password)
