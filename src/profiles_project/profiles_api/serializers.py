from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

# Automatically create a serializer that resembles fields in a model
class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for our user profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # Attributes applied to password. Make sure password field is write only
        extra_kwargs = {'password': {'write_only': True}}

        # Assign the password correctly
        def create(self, validated_data):
            """Create and return a new user"""
            user = models.UserProfile(
                email=validated_data['email'],
                name=validated_data['name'],
            )

            user.set_password(validated_data['password'])
            user.save()

            return user
