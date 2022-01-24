
from rest_framework import generics

from articles.models import Articles
from articles.serializers import ArticleSerializer

class ArticlesCreateAPI(generics.CreateAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer
    

class ArticlesListAPI(generics.ListAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesDetailAPI(generics.RetrieveAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesUpdateAPI(generics.UpdateAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesDeleteAPI(generics.DestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesFeedbackCreateAPI(generics.CreateAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesFeedbackDetailAPI(generics.RetrieveAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesFeedbackUpdateAPI(generics.UpdateAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesFeedbackDeleteAPI(generics.DestroyAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer


class ArticlesFeedbackListAPI(generics.ListAPIView):
    queryset=Articles.objects.all()
    serializer_class=ArticleSerializer