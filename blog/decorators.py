from blog.utils import check_authentication_api
from rest_framework.response import Response
from rest_framework import status
import re


def login_required(func):
    def wrapper(*args, **kwargs):
        request = args[1]
        TOKEN = request.headers.get('token', None)
        pattern = r'^[B,b]earer\s([a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+)$'
        if not TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)
        elif not re.match(pattern, TOKEN):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        authentication_api = check_authentication_api(request, TOKEN)
        if authentication_api:
            result = func(*args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        return result

    return wrapper
