from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

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

    def post(self, request):
        """Create a hello message with our name"""

        # Pass in the request data to the data attribute
        serializer = serializers.HelloSerializer(data=request.data)

        # validate the data, the info stored in a dictionary called data
        if serializer.is_valid():
            name = serializer.data.get('name')
            # Create a message and format the string to include name var
            message = 'Hello {0}'.format(name)
            # Pass the response as an object
            return Response({'message': message})
        else:
            # Errors contains all the error that happened during validation
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating the whole object"""
        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Handles partially updating some fields of the object"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Handles deleting an object"""
        return Response({'method': 'delete'})
