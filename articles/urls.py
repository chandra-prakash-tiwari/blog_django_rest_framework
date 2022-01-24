from django.urls import path
from articles.api import ArticlesCreateAPI, ArticlesDetailAPI, ArticlesFeedbackListAPI, ArticlesListAPI, ArticlesDeleteAPI, ArticlesUpdateAPI, ArticlesFeedbackCreateAPI, ArticlesFeedbackDetailAPI, ArticlesFeedbackUpdateAPI, ArticlesFeedbackDeleteAPI   


urlpatterns=[
    path('create/',ArticlesCreateAPI.as_view(),name='create'),
    path('getall/',ArticlesListAPI.as_view(),name='getall'),
    path('get/<int:pk>/',ArticlesDetailAPI.as_view(),name='get'),
    path('update/<int:pk>/',ArticlesUpdateAPI.as_view(),name='update'),
    path('delete/<int:pk>/',ArticlesDeleteAPI.as_view(),name='delete'),

    path('feedback/create/',ArticlesFeedbackCreateAPI.as_view(),name='create'),
    path('feedback/getall/',ArticlesFeedbackListAPI.as_view(),name='getall'),
    path('feedback/get/<int:pk>/',ArticlesFeedbackDetailAPI.as_view(),name='get'),
    path('feedback/update/<int:pk>/',ArticlesFeedbackUpdateAPI.as_view(),name='update'),
    path('feedback/delete/<int:pk>/',ArticlesDeleteAPI.as_view(),name='delete'),
]