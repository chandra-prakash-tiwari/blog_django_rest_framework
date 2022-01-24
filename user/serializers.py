from rest_framework import serializers

from user.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"



class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')
