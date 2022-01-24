from django.urls import path

from user.api import UserCreateAPI, UserDeleteAPI, UserDetailAPI, UserListAPI, UserUpdateAPI


urlpatterns=[
    path('create/',UserCreateAPI.as_view(),name='create'),
    path('getall/', UserListAPI.as_view(), name='getall'),
    path('get/<int:pk>/', UserDetailAPI.as_view(), name='get'),
    path('update/<int:pk>/', UserUpdateAPI.as_view(), name='update'),
    path('delete/<int:pk>/', UserDeleteAPI.as_view(), name='delete'),
]