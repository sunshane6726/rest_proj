# 데이터 처리 대상
from .models import Essay
from .models import Album, Files
#from rest_framework import viewsets
#from django.shortcuts import render
from .serializers import EssaySerializer
# status에 따라 직접 Response를 처리할 것
from .serializers import AlbumSerializer
from .serializers import FileSerializer

from rest_framework import viewsets

from rest_framework.pagination import PageNumberPagination


class EssayPagination(PageNumberPagination):
    page_size = 5

class ImagePagination(PageNumberPagination):
    page_size = 3

class FilePagination(PageNumberPagination):
    page_size = 3

# 파일을 분리하는 것이 좋다. 패키지나 메소드 분별을 좋은 개발자의 습관이다..2
