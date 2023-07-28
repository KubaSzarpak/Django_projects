from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseServerError


class GreatExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 500:
            return HttpResponseServerError('Oops! Something went wrong')
        return response
