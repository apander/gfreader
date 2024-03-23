import re
import requests
from typing import Tuple, Union
import json
import pandas as pd

class Session:

    def __init__(self, email: str, defaultHeaders: str):
        self.email = email
        self.defaultHeaders = defaultHeaders

    @classmethod
    def setHeaders(cls,login_page_response):
        csrf_token = cls.get_csrf_token(login_page_response.text)

        print(f"csrf_token: {csrf_token}")
        cookies = [
            f"XSRF-TOKEN={cls.get_xsrf_token(login_page_response.cookies)}",
            f"grainfather_community_tools_session={cls.get_grainfather_session(login_page_response.cookies)}",
            "checked_for_terms_and_conditions=true",
            "menuState=false"
        ]

        print(f"login cookies: {cookies}")

        headers = {
            "Cookie": "; ".join(cookies),
            "X-CSRF-TOKEN": csrf_token,
            "Accept-Language":"en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,da;q=0.6,zh-TW;q=0.5"
        }
        cls.defaultHeaders = headers

    @classmethod
    def new(cls, email: str, password: str, url:str) -> Union['Session', str]:
        session = requests.Session()
        login_page_response = session.get(url)
        cls.setHeaders(login_page_response)

        login_response = session.post(
            url=url,
            headers=cls.defaultHeaders,
            data={"email": email, "password": password, "remember": "true"},
            allow_redirects=False
        )

        if login_response.ok:
            cls.setHeaders(login_response)
            return cls(email, cls.defaultHeaders)
        else:
            print(f"Failed to fetch login token: {login_response.text}")
            return "failed to fetch login token"

    @staticmethod
    def get_csrf_token(html: str) -> str:
        match = re.search(r'"csrfToken":"([^"]*)"', html)
        if match:
            return match.group(1)
        return ''

    @staticmethod
    def get_xsrf_token(cookies) -> str:
        return cookies.get('XSRF-TOKEN', '')

    @staticmethod
    def get_grainfather_session(cookies) -> str:
        return cookies.get('grainfather_community_tools_session', '')

    @staticmethod
    def find_cookie(cookies, name: str) -> str:
        cookie_value = cookies.get(name, '')
        return f"{name}={cookie_value}" if cookie_value else ''

    def fetch_brew_data(self,url:str) -> Union[dict, str]:
            """Fetches brew data after login."""
            if not self.defaultHeaders:
                return "Not logged in or missing cookies"

            # Assuming the data URL and that you're already logged in
            headers = self.defaultHeaders
            print(f"headers:{headers}")
            response = requests.get(url, headers=headers)

            if response.ok:
                return response.json()  # or response.text if it's not json
            else:
                return "Failed to fetch data"

