from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'bio', 'profile_picture', 'followers')

class RegisterSerializer(serializers.ModelSerializer):
    # Include password as a CharField and specify write_only=True to hide it in responses
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()  # Uses the custom user model
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Create the user using the validated data
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )
        # Create a token for the new user
        token, created = Token.objects.get_or_create(user=user)
        # Return the user and token
        return user, token
