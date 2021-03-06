from social.backends.oauth import BaseOAuth2
from django.utils.http import urlencode
import json

class LifelongeduOAuth2(BaseOAuth2):
    """Lifelongedu OAuth authentication backend"""
    name = 'lifelongedu'
    AUTHORIZATION_URL = 'http://121.78.115.125:8080/o/authorize'
    ACCESS_TOKEN_URL = 'http://121.78.115.125:8080/o/token/'
    SCOPE_SEPARATOR = ','
#   STATE_PARAMETER = 'random_state_string'
    STATE_PARAMETER = False
    REDIRECT_STATE = False
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires'),
    ]

    def get_user_details(self, response):
        """Return user details from Github account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name'),
                'provider': response.get('provider'),
                'uid': response.get('id') }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'http://121.78.115.125:8080/api/hello?' + urlencode({
            'access_token': access_token
        })
#        url = 'https://121.78.115.125:8080/api/hello?' + {
#            'access_token': access_token
#        }
        try:
            return self.get_json(url)
        except ValueError:
            return None
