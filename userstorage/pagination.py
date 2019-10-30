# 데이터 처리 대상
#from rest_framework import viewsets
#from django.shortcuts import render
from .models import UserEssay
from .models import UserAlbum, UserFiles, UserWeather
from .serializers import UserEssaySerializer
# status에 따라 직접 Response를 처리할 것
from .serializers import UserAlbumSerializer
from .serializers import UserFileSerializer
from .serializers import UserWeatherSerializer

from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination


class UserEssayPagination(PageNumberPagination):
    page_size = 5

class UserAlbumPagination(PageNumberPagination):
    page_size = 3

class UserFilePagination(PageNumberPagination):
    page_size = 3

class UserWeatherPagination(PageNumberPagination):
    page_size = 8

# 파일을 분리하는 것이 좋다. 패키지나 메소드 분별을 좋은 개발자의 습관이다..2
