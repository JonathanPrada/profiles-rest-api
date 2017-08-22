from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of API view features"""

        an_apiview = [
        'Uses HTTP methods as functions (Get, Post, Patch, Put, Delete)',
        'It is similar to a traditional django view',
        'Gives you the most control object your object',
        'Its mapped manually to URLS'
        ]

        # A response object must be part of a dictionary to return the response
        return Response({'message': 'hello!', 'an apiview': an_apiview})
