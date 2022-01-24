from rest_framework import generics

from user.models import Users
from user.serializers import UserSerializer


class UserCreateAPI(generics.CreateAPIView):
    queryset=Users.objects.all()
    serializer_class=UserSerializer


class UserListAPI(generics.ListAPIView):
    queryset=Users.objects.all()
    serializer_class=UserSerializer


class UserDetailAPI(generics.RetrieveAPIView):
    queryset=Users.objects.all()
    serializer_class=UserSerializer


class UserUpdateAPI(generics.UpdateAPIView):
    queryset=Users.objects.all()
    serializer_class=UserSerializer


class UserDeleteAPI(generics.DestroyAPIView):
    queryset=Users.objects.all()
    serializer_class=UserSerializer
