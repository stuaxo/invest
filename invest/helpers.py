from urllib.parse import urljoin
from django.conf import settings
import requests


class IPStackAPIClient:
    session = requests.Session()
    api_key = settings.IPSTACK_API_KEY
    base_url = 'http://api.ipstack.com'
    auth = '?access_key=' + api_key

    @classmethod
    def get(cls, ip):
        url = urljoin(cls.base_url, ip) + cls.auth
        response = cls.session.get(url)
        if response.ok:
            data = response.json()
            if 'error' in data:
                return None
            return data
        return None

    @classmethod
    def get_ip_info(cls, ip):
        return cls.get(ip)

    @classmethod
    def get_language(cls, ip):
        ip_info = cls.get_ip_info(ip)
        if ip_info:
            language = ip_info['location']['languages'][0]['code']
        else:
            language = None
        return language
