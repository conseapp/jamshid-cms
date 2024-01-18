from rest_framework.pagination import PageNumberPagination
from bs4 import BeautifulSoup
import requests


class CustomPostPagination(PageNumberPagination):
    page_size = 15  # Set the page size for posts


class CustomCommentPagination(PageNumberPagination):
    page_size = 7  # Set the page size for comments


def check_authentication_api(request, token):
    _, received_token = token.split()
    api_endpoint = 'https://api.mafia.jamshid.app/auth/check-token'
    headers = {'Authorization': f'Bearer {received_token}'}
    response = None
    try:
        response = requests.post(api_endpoint, headers=headers)
        response_json = response.json()
        if response_json["status"] == 200 or response_json["status"] == 201:
            return True
        elif response_json["status"] == 500:
            return False
    except Exception as err:
        print(err)
        return False


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()



